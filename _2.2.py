import numpy as np


print('Enter size')
while True:
    try:
        n = int(input())
        break;
    except ValueError:
        print('You can enter only numbers. Try again')

array = []
count = 0

while count < n:
    while True:
        try:
            m = int(input())
            count = count + 1
            array.append(m)
            break;
        except ValueError:
            print('You can enter only numbers. Try again')

print(np.array(array).sum())

