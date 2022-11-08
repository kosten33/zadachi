
while True:
    try:
        n = int(input())
        break;
    except ValueError:
        print('You can enter only numbers. Try again')

while True:
    try:
        m = int(input())
        break;
    except ValueError:
        print('You can enter only numbers. Try again')

print(n + m)

