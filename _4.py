

fib = []

fib.append(1)
fib.append(1)

while fib[-1] + fib[-2] < 250:
    fib.append(fib[-1] + fib[-2])

a = int(input())

print(a in fib)
print(fib)
