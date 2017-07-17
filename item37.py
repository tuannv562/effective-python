import select
from time import time


def slow_systemcall():
    select.select([],	[],	[],	0.1)


start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)
