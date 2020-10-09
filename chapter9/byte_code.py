def count_down(n):
    while n > 0:
        print(f'T-minus: {n}')
        n -= 1
    print('Blastoff!')

import dis
dis.dis(count_down)


print(f'co code:\n{count_down.__code__.co_code}')


c = count_down.__code__.co_code
import opcode
print(f'opname is: {opcode.opname[c[0]]}')
print(f'opname c[2]: {opcode.opname[c[2]]}')


import opcode

def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i+1]*256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)


for op, oparg in generate_opcodes(count_down.__code__.co_code):
    print(f'op is: {op}, opname: {opcode.opname[op]}, oparg: {oparg}')


# def add(x, y):
#     return x + y
#
# c = add.__code__
# print(f'{c}')
# print(f'co code: {c.co_code}')
# import types
# new_byte_code = b'xxxxxxx'
# nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount,
#     c.co_nlocals, c.co_stacksize, c.co_flags, new_byte_code, c.co_consts,
#     c.co_names, c.co_varnames, c.co_filename, c.co_name,
#     c.co_firstlineno, c.co_lnotab, c.co_freevars)
#
# print(f'{nc}')
# add.__code__ = nc
# print(f'{add(3, 5)}')