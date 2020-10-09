import re
import unittest

# 美元兑换人民币汇率
DOLLER_TO_YUAN_EXCHANGE_RATE = '6.8288'

# 一年的月份数
YEAR_MONTH = 12
# 最大年薪
MAX_YEAR_SALARY = 10000000
# 最小年薪
MIN_YEAR_SALARY = 3000
MONTH_STYLE = '/月'
YEAR_STYLE = '/年'
US_DOLLAR = '美元'
CHIN_YUAN = '元'
MONTH_FMT = '元/月 * {}月'
# 区间连接符 如 5000~8000元/月 中的连接符
INTERVAL_CONN = '~'

salary_pat_a = re.compile(
    r'((?P<va1>\d{1,5}[\d.,]?\d?)\s{0,3}[万千wk0-9]?(/月|/年|/m|/y|'
    r'每年|每月)?\s{0,3}[~\-–—―－一至]\s{0,3}?(?P<va2>\d{1,5}[\d.,]?'
    r'\d?)\s{0,3}[万千wk0-9]\s{0,3}(元|人民币|美元)?(以上)?'
    r'(/月|/年|/m|/y|每年|每月)?)')
# 匹配类似 2 万千wk0 字符串
salary_pat_b = re.compile(r'(?P<va1>\d{1,6}[\d.,]?\d?)\s{0,3}'
                          r'[万千wk0-9]\s{0,3}(k|元|人民币|美元)?(以上)?'
                          r'(/月|/年|/m|/y|每年|每月)?')
digit_pattern = re.compile(r'[一二三四五六七八九十0-9]')
annual_pay_pattern = re.compile(r'\d{1,2}\.?\d{1,2}[万w]')
salary_digit_pattern = re.compile(r'\d+\.?\d*')
str_num_pat = re.compile(r'[一二三四五六七八九十]')
str_salary_pat = re.compile(r'[一二三四五六七八九十]\s{0,3}[万千wk]')
str_num_dict = {'一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
                '六': '6', '七': '7', '八': '8', '九': '9', '十': '10'}
conn_pat = re.compile(r'[~\-–—―－一至]')

pay_pattern = re.compile(r'[\d{1,4}|一二三四五六七八九十][万w千k]')


class SalaryNormalized(object):
    """
    薪资归一化，将简历中的非特殊化的薪资都归一化为 xxx元/年 的形式
    """
    def __init__(self):
        pass

    def _dollar_to_yuan(self, salary):
        """
        美元 转换为 人民币
        :param salary:
        :return:
        """
        chin_salary = float(salary) * float(DOLLER_TO_YUAN_EXCHANGE_RATE)
        # 保留 0 位小数
        chin_salary = float('{:0.0f}'.format(chin_salary))

        return chin_salary

    def _ch_num_to_number(self, salary_val):
        """
        salary_val 中的 一万字符 更改为 1万
        :param salary_val:
        :return:
        """
        if not str_num_pat.search(salary_val) or not str_salary_pat.search(salary_val):
            return salary_val

        str_num_list = str_num_pat.findall(salary_val)
        str_salary_list = str_salary_pat.findall(salary_val)

        # 满足如下 if 条件时，根据 str_num_list 中值修改 salary_val 对应字符值
        if (len(str_num_list) <= len(str_salary_list)) \
                or (len(str_num_list) == len(str_salary_list) + 1
                    and conn_pat.search(salary_val)):
            for str_num in str_num_list:
                num_val = str_num_dict.get(str_num)
                salary_val = salary_val.replace(str_num, num_val)
        else:
            # 根据 str_salary_list 中值修改 salary_val 对应字符值
            for str_num in str_salary_list:
                b_salary_val = salary_val[0: salary_val.find(str_num)]
                e_salary_val = salary_val[salary_val.find(str_num) + len(str_num):]
                find_str = salary_val[salary_val.find(str_num): salary_val.find(str_num)
                                                                + len(str_num)]
                num_s = str_num_pat.search(str_num).group()
                num_val = str_num_dict.get(num_s)
                find_str = find_str.replace(num_s, num_val)
                salary_val = b_salary_val + find_str + e_salary_val

        return salary_val

    def _salary_unified_fmt(self, salary_mat=None, salary_val=None, is_format=True):
        """
        统一格式化salary
        :param salary_mat:
        :param salary_val:
        :param is_format: 若不需要格式化结果，将得到的 salary 以字典形式返回
        :return:
        """
        if not salary_mat and not salary_val:
            return ''

        if salary_mat:
            val = salary_mat.group().replace(' ', '')
        else:
            val = salary_val.replace(' ', '')

        val = val.lower()
        if val == u'保密' or val == u'面议' or u'egotiate' in val or u'/天' \
                in val or u'/周' in val:
            return ''

        if not digit_pattern.search(val):
            return ''

        if not salary_digit_pattern.search(val):
            val = self._ch_num_to_number(val)

        sal_min = 0
        sal_max = 0

        sal_list = salary_digit_pattern.findall(val)
        if len(sal_list) == 1:
            sal_min = sal_list[0].replace(',', '')
            sal_min = float(sal_min)
            if 'k' in val:
                sal_min *= 1000
            elif 'w' in val or u'万' in val:
                sal_min *= 10000
        elif len(sal_list) == 2:
            sal_min, sal_max = sal_list[0].replace(',', ''), sal_list[1].replace(',', '')
            sal_min, sal_max = float(sal_min), float(sal_max)
            if 'k' in val:
                sal_min *= 1000
                sal_max *= 1000
            elif 'w' in val or u'万' in val:
                sal_min *= 10000
                sal_max *= 10000

        # 若 0 < sal_min < 100 且 sal_max // sal_min >= 50，sal_min不认为有效
        if 0 < sal_min < 100 and sal_max // sal_min >= 50:
            sal_min = sal_max
            sal_max = 0

        # 若不需要格式化结果，将得到的 salary 以字典形式返回。
        if not is_format:
            return {'sal_max': sal_max, 'sal_min': sal_min}

        monthly = False if (u'年' in val or u'/y' in val
                            or (u'月' not in val and u'/m' not in val)
                            or (annual_pay_pattern.match(val) and sal_min >= 80000)) \
            else True  # 当薪水是x.x万并且其值大于80000的时候，认为其是年薪

        salary = u'{0:d}~{1:d}'.format(int(sal_min), int(sal_max)) \
            if sal_max != 0 else u'{0:d}'.format(int(sal_min))
        salary = f'{salary}{US_DOLLAR}' if US_DOLLAR in val else f'{salary}{CHIN_YUAN}'
        salary = f'{salary}{MONTH_STYLE}' if monthly else f'{salary}{YEAR_STYLE}'

        if sal_min == 0 and sal_max == 0 and not re.search(r'[万千wk元月ym]', val):
            return ''

        if sal_min == 0 and sal_max != 0:
            return ''

        if monthly and (sal_min < MIN_YEAR_SALARY // YEAR_MONTH
                        or sal_min > MAX_YEAR_SALARY // YEAR_MONTH):
            return ''
        elif not monthly and (sal_min < MIN_YEAR_SALARY or sal_min > MAX_YEAR_SALARY):
            return ''

        return salary

    def _exists_plus_month_get(self, month_line):
        """
        month_line中存在 + 号字符时，根据+字符提取前面最多两位及后面最多两位数字，相加作为月份数
        需要注意 12+年终奖3.5 及 年终奖3.5+12 形式的 解析
        :param month_line:
        :return:
        """
        plus_num = month_line.find('+')
        if plus_num < 0:
            return ''

        if not (salary_digit_pattern.search(month_line[plus_num - 1:plus_num])
                or salary_digit_pattern.search(month_line[plus_num + 1: plus_num + 2])
                or (plus_num == 0 and
                    salary_digit_pattern.search(month_line[plus_num + 1: plus_num + 2]))):
            return ''

        split_results = month_line.split('+')
        left_val, right_val = split_results[0], split_results[1]
        if left_val.find('.') > -1 and salary_digit_pattern.findall(left_val):
            start_month = float(salary_digit_pattern.findall(left_val)[0])
        elif plus_num >= 2 and \
                salary_digit_pattern.search(month_line[plus_num - 2: plus_num - 1]):
            start_month = float(month_line[plus_num - 2: plus_num])
        elif plus_num > 0:
            start_month = float(month_line[plus_num - 1: plus_num])
        else:
            if left_val and salary_digit_pattern.findall(left_val):
                start_month = float(salary_digit_pattern.findall(left_val)[0])
            else:
                start_month = ''

        if right_val.find('.') > -1 and salary_digit_pattern.findall(right_val):
            end_month = float(salary_digit_pattern.findall(right_val)[0])
        elif (plus_num + 2 < len(month_line)
              and pay_pattern.search(month_line[plus_num + 1: plus_num + 3])) \
                or (plus_num + 3 < len(month_line)
                    and pay_pattern.search(month_line[plus_num + 1: plus_num + 4])):
            end_month = ''
        elif plus_num + 2 < len(month_line) \
                and salary_digit_pattern.search(month_line[plus_num + 2: plus_num + 3]):
            end_month = float(month_line[plus_num + 1: plus_num + 3])
        elif plus_num + 2 <= len(month_line) \
                and salary_digit_pattern.search(month_line[plus_num + 1: plus_num + 2]):
            end_month = float(month_line[plus_num + 1: plus_num + 2])
        else:
            if right_val and salary_digit_pattern.findall(right_val):
                end_month = float(salary_digit_pattern.findall(right_val)[0])
            else:
                end_month = ''

        if start_month and end_month:
            month_num = start_month + end_month
        elif start_month:
            month_num = start_month
        else:
            month_num = end_month

        return str(month_num)

    def _month_num(self, line):
        """
        从 line 中获取 月数，默认值 YEAR_MOUTH
        :param line:
        :return:
        """
        month_list = list()
        month_num = str(YEAR_MONTH)
        if line.find('*') < 0:
            month_list.append(month_num)
            return month_list

        month_line = line[line.find('*') + 1:].strip()
        if month_line.find('个月') > -1:
            month_num = month_line[:month_line.find('个月')]
        elif month_line.find('月') > -1:
            month_num = month_line[:month_line.find('月')]
        elif month_line.find('薪') > -1:
            month_num = month_line[:month_line.find('薪')]

        # 解析疑似月份的字符串中有+号，
        if month_num.find('+') > -1 or line.find('+') > -1:
            find_str = month_num if month_num.find('+') > -1 else month_line
            month_num = self._exists_plus_month_get(find_str)
            if not month_num:
                month_num = str(YEAR_MONTH)

        month_list = salary_digit_pattern.findall(month_num)

        return month_list


    def _month_style_fmt(self, salary):
        """
        月形式薪资格式化
        从 month_salary 中获取最大最小月薪
        :param salary:
        :return:
        """
        month_salary = salary[:salary.find(MONTH_STYLE)].strip()
        if month_salary.endswith(CHIN_YUAN) and not month_salary.endswith(US_DOLLAR):
            month_salary = month_salary[:month_salary.find(CHIN_YUAN)].strip()
            if month_salary.find(INTERVAL_CONN) > -1:
                salary_list = month_salary.split(INTERVAL_CONN)
                min_salary, max_salary = salary_list[0], salary_list[1]
                min_month_salary = float(min_salary)
                max_month_salary = float(max_salary)
            else:
                min_month_salary = float(month_salary)
                max_month_salary = min_month_salary
        elif month_salary.endswith(US_DOLLAR):
            month_salary = month_salary[:month_salary.find(US_DOLLAR)].strip()
            if month_salary.find(INTERVAL_CONN) > -1:
                salary_list = month_salary.split(INTERVAL_CONN)
                min_salary, max_salary = salary_list[0], salary_list[1]

                min_month_salary = self._dollar_to_yuan(min_salary)
                max_month_salary = self._dollar_to_yuan(max_salary)
            else:
                ch_month_salary = self._dollar_to_yuan(month_salary)
                min_month_salary = ch_month_salary
                max_month_salary = min_month_salary
        else:
            if month_salary.find(INTERVAL_CONN) > -1:
                salary_list = month_salary.split(INTERVAL_CONN)
                min_salary, max_salary = salary_list[0], salary_list[1]
                min_month_salary = float(min_salary)
                max_month_salary = float(max_salary)
            else:
                min_month_salary = float(month_salary)
                max_month_salary = min_month_salary

        return min_month_salary, max_month_salary

    def _min_max_mouth(self, month_list, is_year=True):
        """
        取得最小，最大月数，默认按一年 12 个月计算，即取默认时，
        返回的 min_month, max_month 均不可小于12
        :param month_list:
        :param is_year:
        :return:
        """
        min_month = YEAR_MONTH
        max_month = YEAR_MONTH
        if not month_list:
            return min_month, max_month

        if len(month_list) == 1:
            min_month = float(month_list[0])
            max_month = min_month
        else:
            min_month = float(month_list[0])
            max_month = float(month_list[1])

        if is_year and min_month < YEAR_MONTH:
            min_month = YEAR_MONTH
        if is_year and max_month < YEAR_MONTH:
            max_month = YEAR_MONTH

        return min_month, max_month

    def _year_style_fmt(self, salary, month_list):
        """
        年薪资格式化
        从 month_salary 中获取最大最小月薪
        :param salary:
        :param month_list:
        :return:
        """
        min_month_salary, max_month_salary = 0, 0
        year_sal = salary[:salary.find(YEAR_STYLE)].strip()
        min_month, max_month = month_list[0], month_list[1]

        if year_sal.find(US_DOLLAR) > -1:
            year_sal = year_sal[:year_sal.find(US_DOLLAR)].strip()
            if year_sal.find(INTERVAL_CONN) > -1:
                salary_list = year_sal.split(INTERVAL_CONN)
                min_salary, max_salary = salary_list[0], salary_list[1]
                min_month_salary = self._dollar_to_yuan(min_salary) // min_month
                max_month_salary = self._dollar_to_yuan(max_salary) // max_month
            else:
                min_month_salary = self._dollar_to_yuan(year_sal) // min_month
                max_month_salary = self._dollar_to_yuan(year_sal) // max_month
        elif year_sal.find(CHIN_YUAN) > -1:
            year_sal = year_sal[:year_sal.find(CHIN_YUAN)].strip()
            if year_sal.find(INTERVAL_CONN) > -1:
                salary_list = year_sal.split(INTERVAL_CONN)
                min_month_salary = float(salary_list[0]) // min_month
                max_month_salary = float(salary_list[1]) // max_month
            else:
                min_month_salary = float(year_sal) // min_month
                max_month_salary = float(year_sal) // max_month
        return min_month_salary, max_month_salary

    def _min_max_month_salary(self, salary, month_list):
        """
        取得最小 最大月薪
        :param salary:
        :param month_list:
        :return:
        """
        if salary.endswith(MONTH_STYLE):
            min_month_salary, max_month_salary = self._month_style_fmt(salary)
        elif salary.endswith(YEAR_STYLE):
            min_month_salary, max_month_salary = self._year_style_fmt(salary, month_list)
        else:
            min_month_salary = ''
            max_month_salary = ''

        return min_month_salary, max_month_salary

    def _salary_fmt(self, salary, month_list, salary_res=None,
                    salary_mat_search=None, total_salary=0.0):
        """
        薪资格式化为指定形式
        :param salary:
        :param month_list:
        :param salary_res:
        :param salary_mat_search:
        :param total_salary:
        :return:
        """
        min_month, max_month = self._min_max_mouth(month_list)
        month_list = [min_month, max_month]

        min_month_salary, max_month_salary = self._min_max_month_salary(salary, month_list)

        res_min_month_salary, res_max_month_salary = '', ''
        # 若 salary_res 不为空，从 salary_res 中取得 最大最小 月薪
        if salary_res:
            res_min_month_salary, res_max_month_salary = \
                self._min_max_month_salary(salary_res, month_list)

        mat_search_min_month_salary, mat_search_max_month_salary = '', ''
        # 若 salary_mat_search 不为空，从 salary_mat_search 中取得 最大最小 月薪
        if salary_mat_search:
            mat_search_min_month_salary, mat_search_max_month_salary = \
                self._min_max_month_salary(salary_mat_search, month_list)

        if salary_res and min_month_salary and res_min_month_salary \
                and max_month_salary and res_max_month_salary:
            # salary 比较，返回大的一个
            if res_max_month_salary > max_month_salary \
                    or res_min_month_salary > min_month_salary:
                min_month_salary = res_min_month_salary
                max_month_salary = res_max_month_salary

        if salary_mat_search and min_month_salary and mat_search_min_month_salary \
                and max_month_salary and mat_search_max_month_salary:
            # salary 比较，返回大的一个
            if mat_search_max_month_salary > max_month_salary \
                    or mat_search_min_month_salary > min_month_salary:
                min_month_salary = mat_search_min_month_salary
                max_month_salary = mat_search_max_month_salary

        if total_salary > 0 and total_salary // max_month > max_month_salary:
            min_month_salary = total_salary // max_month
            max_month_salary = min_month_salary

        if min_month_salary:
            min_month_salary = str(min_month_salary) + MONTH_FMT.format(min_month)

        if max_month_salary:
            max_month_salary = str(max_month_salary) + MONTH_FMT.format(max_month)

        return min_month_salary, max_month_salary

    def _total_salary(self, line):
        """
        总薪资计算
        对于类似 5w+12*2.5w 的形式，需要计算总薪资
        :param line:
        :return: 计算得到的总额
        """
        if line.find('+') < 0 and line.find('*') < 0:
            return 0

        line_sub = line.split('+')
        left_val, right_val = line_sub[0], line_sub[1]
        # 是否有 薪资 单位
        if not (pay_pattern.search(left_val) and pay_pattern.search(right_val)):
            return 0

        month_num = YEAR_MONTH
        left_month, right_month = 0, 0
        left_sal_val, right_sal_val = left_val, right_val
        # 对含有 * 的部分文本，取得 月份数 和 薪资值
        if left_val.find('*') > -1:
            sub_val_list = left_val.split('*')
            if pay_pattern.search(sub_val_list[0]):
                left_sal_val = sub_val_list[0]
            else:
                left_sal_val = sub_val_list[1]

            month_list = self._month_num(left_val)
            min_month, max_month = self._min_max_mouth(month_list, is_year=False)
            left_month = max_month
            month_num = left_month

        # 格式化salary，通过 is_format 参数控制返回值形式，从返回值中取得 相关值
        left_sal_dict = self._salary_unified_fmt(salary_val=left_sal_val,
                                                 is_format=False)
        if left_month > 0:
            left_salary_total = left_sal_dict.get('sal_min') * left_month
        else:
            left_salary_total = left_sal_dict.get('sal_min')

        if right_val.find('*') > -1:
            sub_val_list = right_val.split('*')
            if pay_pattern.search(sub_val_list[0]):
                right_sal_val = sub_val_list[0]
            else:
                right_sal_val = sub_val_list[1]

            month_list = self._month_num(right_val)
            min_month, max_month = self._min_max_mouth(month_list, is_year=False)
            right_month = max_month
            month_num += max_month

        right_sal_dict = self._salary_unified_fmt(salary_val=right_sal_val,
                                                  is_format=False)
        if right_month > 0:
            right_salary_total = right_sal_dict.get('sal_min') * right_month
        else:
            right_salary_total = right_sal_dict.get('sal_min')

        return left_salary_total + right_salary_total

    def get_normalized_salary(self, line, parser_salary, mat_val=None, mtype=None):
        """
        取得归一化薪资值
        :param line:
        :param parser_salary:
        :param mat_val:
        :return:
        """
        salary_res = ''
        salary_mat_search = ''

        # 匹配类似 10000-14999元/月 字段
        salary_mat_a = salary_pat_a.search(line)
        # 匹配类似 10000元/月 字段
        salary_mat_b = salary_pat_b.search(line)

        if salary_mat_a and salary_mat_b:
            # 取得匹配值的起始位置
            a_span = salary_mat_a.span()[0]
            b_span = salary_mat_b.span()[0]

            # 从起始匹配值小的位置做截取，作为 res_line的值
            if a_span <= b_span:
                salary_mat_search = salary_mat_a.group()
                res_line = line[line.find(salary_mat_a.group())
                                + len(salary_mat_a.group()):]
                primitive_salary_val = line[line.find(salary_mat_a.group()):]
            else:
                salary_mat_search = salary_mat_b.group()
                res_line = line[line.find(salary_mat_b.group())
                                + len(salary_mat_b.group()):]
                primitive_salary_val = line[line.find(salary_mat_b.group()):]
        elif salary_mat_a or salary_mat_b:
            primitive_salary_val = line[line.find(salary_mat_a.group()):] \
                if salary_mat_a else line[line.find(salary_mat_b.group()):]
            salary_mat_search = salary_mat_a.group() \
                if salary_mat_a else salary_mat_b.group()
            res_line = line[line.find(salary_mat_a.group())
                            + len(salary_mat_a.group()):] \
                if salary_mat_a else line[line.find(salary_mat_b.group())
                                          + len(salary_mat_b.group()):]
        else:
            digit_find = digit_pattern.search(line)
            res_line = line[digit_find.span()[0]:]
            primitive_salary_val = res_line

        if res_line:
            salary_mat_res = salary_pat_a.search(res_line)
            if not salary_mat_res:
                salary_mat_res = salary_pat_b.search(res_line)

            if salary_mat_res:
                salary_res = self._salary_unified_fmt(salary_mat=salary_mat_res)

            if not salary_mat_res and str_num_pat.search(res_line) \
                    and str_salary_pat.search(res_line):
                salary_res = self._salary_unified_fmt(salary_val=res_line)

        if salary_mat_search:
            salary_mat_search = self._salary_unified_fmt(salary_val=salary_mat_search)

        total_salary = 0.0
        if line.find('*') > -1 and line.find('+') > -1:
            total_salary = self._total_salary(line)

        month_list = self._month_num(line)

        # 对 parser_salary 再执行一次 统一格式化
        parser_salary = self._salary_unified_fmt(salary_val=parser_salary)

        if conn_pat.search(parser_salary) and not parser_salary.find(INTERVAL_CONN) > -1:
            parser_salary = self._salary_unified_fmt(salary_val=parser_salary)

        min_year_salary, max_year_salary = self._salary_fmt(parser_salary,
                                                            month_list,
                                                            salary_res,
                                                            salary_mat_search,
                                                            total_salary)

        return min_year_salary, max_year_salary, primitive_salary_val


test_case_str_lists = [
    # [0]
    ['目前年薪: 28.8万(24000-25000元/月 * 13个月)', '288000元/年'],
    # [1]
    ['期望薪资: 10000-14999元/月', '10000~14999元/月'],
    # [2]
    ['目前年收入 30万元(包含基本工资、补贴、奖金、股权收益等)', '300000元/年'],
    # [3]
    ['期望薪资: 30-40万 元/年', '300000~400000元/年'],
    # [4]
    ['2k以下', '2000元/月'],
    # [5]
    ['目前年薪: 30万(25000元/月 * 16个月)', '300000元/年'],
    # [6]
    ['年薪 :50w(税前)', '500000元/年'],
    # [7]
    ['目前年薪: 28.8万(24000元/月 * 13个月)', '288000元/年'],
    # [8]
    ['目职位月薪:40k/月以上 ', '40000元/月'],
    # [9]
    ['期望薪资: 30k-45k*14薪', '30000~45000元/月'],
    # [10]
    ['期望薪资: 10000-14999美元/月', '10000~14999美元/月'],
    # [11]
    ['期望薪资: 二万-三万/月', '二万-三万/月'],
    # [12]
    ['期望薪资: 30k-45k*13-14薪', '30000~45000元/月'],
    # [13]
    ['￥10000', '￥10000'],
    # [14]
    ['期望薪资: 3-5万/月', '3-5万/月'],
    # [15]
    ['期望薪资: 3-5k/月*13-14月', '3-5k/月'],
    # [16]
    ['期望薪资: 35k/月*13-14月', '35000/月'],
    # [17]
    ['1年*14,期望月薪: 35k/月', '35000/月'],
    # [18]
    ['*14-16,期望薪资: 35k/月', '35000/月'],
    # [19]
    ['期望薪资: 30k-45k*12.00薪', '30000~45000元/月'],
    # [20]
    ['薪酬状况:36万/年 ~ 60万/年(基础底薪3万/月,年终奖,提成,配股)', '360000元/年'],
    # [21]
    ['目前薪酬:税前46.8万/月,其中税前3.9万元/月*12个月', '46.8万/月'],
    # [22]
    ['期望薪资: 30k-45k*13+3', '30000~45000元/月'],
    # [23]
    ['期望薪资: 30k-45k*13+12', '30000~45000元/月'],
    # [24]
    ['期望薪资: 30k-45k*3+12', '30000~45000元/月'],
    # [25]
    ['期望薪资: 30k-45k*13+', '30000~45000元/月'],
    # [26]
    ['期望薪资: 30k-45k*+13', '30000~45000元/月'],
    # [27]
    ['期望薪资: 30k-45k*11+', '30000~45000元/月'],
    # [28]
    ['期望薪资: 30k-45k*+11', '30000~45000元/月'],
    # [29]
    ['期望薪资: 30k-45k*12+年终奖3.5', '30000~45000元/月'],
    # [30]
    ['期望薪资: 30k-45k*年终奖3.5+12', '30000~45000元/月'],
    # [31]
    ['职位薪资:2.5w*12+5w', '300000/年'],
    # [32]
    ['职位薪资:5w+12*2.5w', '300000/年'],
]


class SalaryFuncTestCase(unittest.TestCase):
    def setUp(self):
        self.normalizer = SalaryNormalized()
        self.warmUp()

    def tearDown(self):
        self.normalizer = None

    def warmUp(self):
        pass

    def runTest(self):
        for case_list in test_case_str_lists[:]:
            if len(case_list) == 2:
                salary_detail = self.normalizer.get_normalized_salary(case_list[0],
                                                                      case_list[1])
            elif len(case_list) == 3:
                salary_detail = self.normalizer.get_normalized_salary(case_list[0],
                                                                      case_list[1],
                                                                      case_list[2])
            elif len(case_list) == 4:
                salary_detail = self.normalizer.get_normalized_salary(case_list[0],
                                                                      case_list[1],
                                                                      case_list[2],
                                                                      case_list[3])
            print(f'原始文本内容: {case_list}\n格式化后结果: {salary_detail}\n')


if __name__ == "__main__":
    unittest.main()

