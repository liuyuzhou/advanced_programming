import re

anno_pat = re.compile(r'/\*(.*?)\*/')
text_1 = '/* this is one line annotation */'
text_2 = """/* this is
multi line annotation */
"""

print(anno_pat.findall(text_1))
print(anno_pat.findall(text_2))


anno_pat = re.compile(r'/\*((?:.|\n)*?)\*/')
print(anno_pat.findall(text_2))


anno_pat = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(anno_pat.findall(text_2))