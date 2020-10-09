from operator import itemgetter
from itertools import groupby

done_record = [
    {'done': 'read book', 'date': '07/01/2020'},
    {'done': 'work', 'date': '07/04/2020'},
    {'done': 'family chat', 'date': '07/02/2020'},
    {'done': 'run', 'date': '07/03/2020'},
    {'done': 'sport', 'date': '07/02/2020'},
    {'done': 'read 20 pages', 'date': '07/02/2020'},
    {'done': 'run 5km', 'date': '07/01/2020'},
    {'done': 'sport 2 hours', 'date': '07/04/2020'},
]

# Sort by the desired field first
done_record.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(done_record, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)


from collections import defaultdict
record_by_date = defaultdict(list)
for record in done_record:
    record_by_date[record['date']].append(record)

for record in record_by_date['07/01/2012']:
    print(record)