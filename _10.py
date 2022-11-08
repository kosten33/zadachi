
n = int(input())
count = 0
countN = 1
i = 1

print(1)

while countN < n:
    count = 0
    for j in range(1,i):
        if i % j == 0:
            count = count + j     
    if count == i:
        print(count)
        countN = countN + 1
    i = i + 1   
