text_v = 'foo = 23 + 42 * 10'


token_list = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]


import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


scanner = master_pat.scanner('foo = 42')
match_val = scanner.match()
print(match_val)
print(match_val.lastgroup, match_val.group())

match_val = scanner.match()
print(match_val)
print(match_val.lastgroup, match_val.group())

match_val = scanner.match()
print(match_val)
print(match_val.lastgroup, match_val.group())

match_val = scanner.match()
print(match_val)
print(match_val.lastgroup, match_val.group())

match_val = scanner.match()
print(match_val)
print(match_val.lastgroup, match_val.group())

match_val = scanner.match()
print(match_val)


from collections import namedtuple
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    pat_scanner = pat.scanner(text)
    for m in iter(pat_scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)


token_list = (tok for tok in generate_tokens(master_pat, text_v) if tok.type != 'WS')
for tok in token_list:
    print(tok)


LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)
