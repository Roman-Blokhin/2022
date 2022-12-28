while True:
    a = int (input('Введите первое число: '))
    b = int (input('Введите второе число: '))
    c = input('Выберите действие: \n1. + \n2. - \n')

    s = a + b
    m = a - b

    if c == '1':
        print ('Ваш результат: ' + str (s))
    if c == '2':
        print ('Ваш результат: ' + str (m))

    d = input ('')
