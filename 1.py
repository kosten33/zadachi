import time
import tracemalloc

tracemalloc.start()

a = int(input())
b = int(input())
c = int(input())

start_time = time.time()

mas = []
mas.append(b)
mas.append(c)
mas.append(a)

a = mas[0]
b = mas[1]
c = mas[2]

print(a,b,c)

print("--- %s seconds ---" % (time.time() - start_time))

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
