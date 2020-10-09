def income_exp(income_record):
    *income_pre_month, current_month = income_record
    income_avg = sum(income_pre_month) / len(income_pre_month)
    return avg_comparison(income_avg, current_month)


def avg_comparison(income_avg, current_month):
    pass
