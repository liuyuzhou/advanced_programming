test_str = 'pýtĥöñ\fis\tawesome\r\n'
print(test_str)


re_map = {ord('\t') : ' ',
          ord('\f'): ' ',
          ord('\r'): None}
print(test_str.translate(re_map))


import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b_val = unicodedata.normalize('NFD', test_str)
print(b_val)
print(b_val.translate(cmb_chrs))


digit_map = {c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'
             }

print(len(digit_map))
x = '\u0661\u0662\u0663'
print(x.translate(digit_map))

test_b = unicodedata.normalize('NFD', test_str)
print(test_b.encode('ascii', 'ignore').decode('ascii'))


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s