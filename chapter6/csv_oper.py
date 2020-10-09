import csv
with open('course.csv') as f:
    f_csv = csv.reader(f)
    header_list = next(f_csv)
    for row in f_csv:
        print(f'course name: {row[0]}, total class: {row[5]}')


from collections import namedtuple
with open('course.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(f'course name: {row.CourseName}, total class: {row.TotalClass}')


import csv
with open('course.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(f'dict read: {row}')


header_list = ['CourseName','Score','Date','Time','Finished','TotalClass']
row_list = [('python', 0.5, '6/1/2020', '8:30am', 3, 30),
            ('java', 0.2, '6/1/2020', '9:30am', 2, 20),
            ('php', 0.25, '6/1/2020', '10:30am', 5, 10),
            ]

with open('course.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header_list)
    f_csv.writerows(row_list)


header_list = ['CourseName','Score','Date','Time','Finished','TotalClass']
row_list = [{'CourseName': 'python', 'Score': 0.5, 'Date': '6/1/2020',
             'Time': '8:30am', 'Finished': 3, 'TotalClass': 30},
            {'CourseName': 'java', 'Score': 0.2, 'Date': '6/1/2020',
             'Time': '9:30am', 'Finished': 2, 'TotalClass': 20},
            {'CourseName': 'php', 'Score': 0.25, 'Date': '6/1/2020',
             'Time': '10:30am', 'Finished': 5, 'TotalClass': 10},
            ]

with open('course.csv','w') as f:
    f_csv = csv.DictWriter(f, header_list)
    f_csv.writeheader()
    f_csv.writerows(row_list)


with open('course.csv') as f:
    for line in f:
        row_list = line.split(',')
        print(f'split row: {row_list}')


with open('course.csv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        print(f'read row: {row}')


import re
with open('course.csv') as f:
    f_csv = csv.reader(f)
    header_list = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', header_list)
    for r in f_csv:
        row = Row(*r)
        print(f'named tuple read: {row}')


col_types = [str, float, str, str, int, int]
with open('course.csv') as f:
    f_csv = csv.reader(f)
    header_list = next(f_csv)
    for row in f_csv:
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(f'row read: {row}')


print('Reading as dicts with type conversion')
field_types = [ ('Score', float),
                ('Finished', float),
                ('TotalClass', int) ]

with open('course.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                for key, conversion in field_types)
        print(f'update row: {row}')