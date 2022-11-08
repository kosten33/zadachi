import numpy as np

n = int(input())
m = int(input())

table = []

for i in range(1,m+1):
    table.append([])
    for j in range(1, n+1):
        table[-1].append(i*j)

for i in range(0,m):
    print(table[i])
        

