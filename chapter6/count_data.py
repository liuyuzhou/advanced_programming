import pandas

rats = pandas.read_csv('rats.csv', skip_footer=1)
print(rats)

print(rats['Current Activity'].unique())
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print(len(crew_dispatched))
print(crew_dispatched['ZIP Code'].value_counts()[:10])
dates = crew_dispatched.groupby('Completion Date')
print(len(dates))

date_counts = dates.size()
date_counts[0:10]
date_counts.sort()
print(date_counts[-10:])
