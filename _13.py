def summ(mas):
    if len(mas) == 0:
        return 0
    else:
        return mas[-1] + summ(mas[0:-1])

mas = [1,2,3,4,5]

print(summ(mas))


