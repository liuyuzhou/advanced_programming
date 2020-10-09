text_val = 'life is short, I use python, what about you'
print(text_val.replace('use', 'choice'))


text_date = 'Today is 04/21/2020. Python2 stop maintain from 01/01/2020.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text_date))


date_pat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(date_pat.sub(r'\3-\1-\2', text_date))


from calendar import month_abbr
def change_date(group_val):
    mon_name = month_abbr[int(group_val.group(1))]
    return f'{group_val.group(2)} {mon_name} {group_val.group(3)}'

print(date_pat.sub(change_date, text_date))


new_text, rep_num = date_pat.subn(r'\2-\1-\2', text_date)
print(f'after replace text:{new_text}')
print(f'replace value num:{rep_num}')