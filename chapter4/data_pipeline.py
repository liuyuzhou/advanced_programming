import os
import fnmatch
import gzip
import bz2
import re

def gen_find(file_pat, top):
    """
    Find all file_name_list in a directory tree that match a shell wildcard pattern
    :param file_pat:
    :param top:
    :return:
    """
    for path, dir_list, file_list in os.walk(top):
        for name in fnmatch.filter(file_list, file_pat):
            yield os.path.join(path,name)

def gen_opener(file_name_list):
    """
    Open a sequence of file_name_list one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    :param file_name_list:
    :return:
    """
    for file_name in file_name_list:
        if file_name.endswith('.gz'):
            f = gzip.open(file_name, 'rt')
        elif file_name.endswith('.bz2'):
            f = bz2.open(file_name, 'rt')
        else:
            f = open(file_name, 'rt')
        yield f
        f.close()

def gen_concatenate(iterator_list):
    """
    Chain a sequence of iterator_list together into a single sequence.
    :param iterator_list:
    :return:
    """
    for it in iterator_list:
        yield from it

def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    :param pattern:
    :param lines:
    :return:
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


log_names = gen_find('access-log*', 'www')
file_list = gen_opener(log_names)
line_list = gen_concatenate(file_list)
py_line_list = gen_grep('(?i)python', line_list)
for line in py_line_list:
    print(line)


log_names = gen_find('access-log*', 'www')
file_list = gen_opener(log_names)
line_list = gen_concatenate(file_list)
py_line_list = gen_grep('(?i)python', line_list)
bytecolumn = (line.rsplit(None,1)[1] for line in py_line_list)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))
