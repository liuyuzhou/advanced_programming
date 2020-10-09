from struct import Struct

def write_records(record_list, format, f):
    """
    Write a sequence of tuples to a binary file of structures.
    :param record_list:
    :param format:
    :param f:
    :return:
    """
    record_struct = Struct(format)
    for r in record_list:
        f.write(record_struct.pack(*r))

# Example
if __name__ == '__main__':
    records = [(1, 3.3, 7.5),
                (5, 9.8, 11.0),
                (16, 18.4, 66.7)]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


# def read_records(format, f):
#     record_struct = Struct(format)
#     chunks = iter(lambda: f.read(record_struct.size), b'')
#     return (record_struct.unpack(chunk) for chunk in chunks)
#
# # Example
# if __name__ == '__main__':
#     with open('test.b','rb') as f:
#         for rec in read_records('<idd', f):
#             pass
#
#
# from struct import Struct
#
# def unpack_records(format, data):
#     record_struct = Struct(format)
#     return (record_struct.unpack_from(data, offset)
#             for offset in range(0, len(data), record_struct.size))
#
#
# if __name__ == '__main__':
#     with open('test.b', 'rb') as f:
#         data = f.read()
#     for rec in unpack_records('<idd', data):
#         pass
#
#
# record_struct = Struct('<idd')
#
#
# from struct import Struct
# record_struct = Struct('<idd')
# print(f'record struct size: {record_struct.size}')
# print(f'pack: {record_struct.pack(1, 3.0, 6.0)}')
#
#
# import struct
# print(f"struct pack: {struct.pack('<idd', 1, 3.0, 6.0)}")
#
#
# f = open('test.b', 'rb')
# chunks = iter(lambda: f.read(20), b'')
# print(chunks)
# for chk in chunks:
#     print(f'chk is: {chk}')
#
#
# def read_records(format, f):
#     record_struct = Struct(format)
#     while True:
#         chk = f.read(record_struct.size)
#         if chk == b'':
#             break
#         yield record_struct.unpack(chk)
#
#
# def unpack_records(format, data):
#     record_struct = Struct(format)
#     return (record_struct.unpack(data[offset:offset + record_struct.size])
#             for offset in range(0, len(data), record_struct.size))
#
#
# from collections import namedtuple
#
# Record = namedtuple('Record', ['kind','x','y'])
#
# with open('test.p', 'rb') as f:
#     record_list = (Record(*r) for r in read_records('<idd', f))
#
# for r in record_list:
#     print(f'kind:{r.kind}, x: {r.x}, y: {r.y}')
#
#
# import numpy as np
# f = open('test.b', 'rb')
# record_list = np.fromfile(f, dtype='<i,<d,<d')
# print(f'records: {record_list}')
# print(f'records 0: {record_list[0]}')
# print(f'records 1: {record_list[1]}')
