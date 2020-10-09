import re

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

digit_pattern = re.compile(r'[一二三四五六七八九十0-9]')
annual_pay_pattern = re.compile(r'\d{1,2}\.?\d{1,2}[万w]')
salary_digit_pattern = re.compile(r'\d+\.?\d*')
str_num_pat = re.compile(r'[一二三四五六七八九十]')
str_salary_pat = re.compile(r'[一二三四五六七八九十]\s{0,3}[万千wk]')
str_num_dict = {'一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
                '六': '6', '七': '7', '八': '8', '九': '9', '十': '10'}
conn_pat = re.compile(r'[~\-–—―－一至]')


def ch_num_to_number(salary_val):
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


def salary_unified_fmt(salary_mat=None, salary_val=None, is_format=True):
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
    if val == u'保密' or val == u'面议' or u'egotiate' in val \
            or u'/天' in val or u'/周' in val:
        return ''

    if not digit_pattern.search(val):
        return ''

    if not salary_digit_pattern.search(val):
        val = ch_num_to_number(val)

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

    monthly = False if (u'年' in val or u'/y' in val or
                        (u'月' not in val and u'/m' not in val)
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


if __name__ == "__main__":
    fmt_result = salary_unified_fmt(salary_val='30万元/年')
    print(fmt_result)
    fmt_result = salary_unified_fmt(salary_val='35k/月')
    print(fmt_result)
