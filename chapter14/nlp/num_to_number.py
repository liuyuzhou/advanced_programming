import re

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


if __name__ == "__main__":
    fmt_result = ch_num_to_number('二万')
    print(fmt_result)
    fmt_result = ch_num_to_number('二万-三万')
    print(fmt_result)