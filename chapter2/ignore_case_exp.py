import re
text_val = 'LEARN PYTHON3, like python, Good at Python'
print(re.findall('python', text_val, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text_val, flags=re.IGNORECASE))


def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(re.sub('python', match_case('snake'), text_val, flags=re.IGNORECASE))