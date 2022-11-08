import time

a = int(input())

start_time1 = time.time()

print(a**5)

print("--- %s seconds ---" % (time.time() - start_time1))

start_time2 = time.time()

print(a*a*a*a*a)

print("--- %s seconds ---" % (time.time() - start_time2))
