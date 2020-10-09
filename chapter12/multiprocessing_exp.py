import multiprocessing
from chapter12.count_down import CountdownTask

c = CountdownTask()
p = multiprocessing.Process(target=c.run)
p.start()