from docx import Document
import re

ch_pat = re.compile(r'一-龥')
en_pat = re.compile(r'a-zA-Z')
num_pat = re.compile(r'0-9')

document = Document('/Users/lyz/Documents/writebook/python高级编程/正文/test.docx')
for para in document.paragraphs:
    # print(para.text)
    # print(len(para.text))
    p_text = para.text
    for num, ch in enumerate(p_text):
        # if num < len(para.text) - 1 and ch and para.text[num + 1] == ' ':
        #     print('-----')
        # print(num, ch)
        if 0 < num < len(p_text) - 2 and p_text[num + 1] == ' ' and p_text[num + 2] and ch:
            p_text[num + 1] = ''