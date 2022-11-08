
n = int(input())

if n % 2 == 0:
    nechCount = n // 2 
else:
    nechCount = n // 2 + 1

chCount = n - nechCount

summ = (1+n)/2 * n

print('nech', nechCount)
print('ch', chCount)
print('summ', summ)

