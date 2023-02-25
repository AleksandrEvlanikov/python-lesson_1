b = input('Введите номер билета: ')
sum = 0
sum1 = 0


if len(b) == 6:
    sum = int(b[0]) + int(b[1]) + int(b[2])
    sum1 = int(b[3]) + int(b[4]) + int(b[5])
    if sum == sum1:
        print('Cчастливый')
    else:
        print('Несчастливый билет')

else:
    print('Некорректный номер билета')