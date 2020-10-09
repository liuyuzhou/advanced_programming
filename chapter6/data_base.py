course_list = [
    ('pyton', 30, 0.3),
    ('java', 20, 0.25),
    ('go', 20, 0.2),
    ('c', 25, 0.15),
]


import sqlite3
db = sqlite3.connect('database.db')


c = db.cursor()
create_str = 'create table course_info (course_name text, total_class integer, score real)'
print(f'create execute: {c.execute(create_str)}')
db.commit()


c.executemany('insert into course_info values (?,?,?)', course_list)
db.commit()


for row in db.execute('select * from course_info'):
    print(f'read row: {row}')


min_score = 0.25
for row in db.execute('select * from course_info where score >= ?',(min_score,)):
    print(f'read row: {row}')