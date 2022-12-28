while True:
    try:
        a = int (input('\nВведите первое число: '))
    except ValueError:
        print ('\nНе не не, тут должны быть циферки.')
        try:
            a = int(input('\nВведите первое число: '))
        except ValueError:
            print ('\nНу что ж, нет так нет!')
            break
    try:
        b = int (input('\nВведите второе число: '))
    except ValueError:
        print ('\nНе не не, тут должны быть циферки.')
        try:
            b = int (input('\nВведите второе число: '))
        except ValueError:
            print ('\nНу что ж, нет так нет!')
            break

    c = input('Выберите действие: \n1. + \n2. - \n3. * \n4. / \n')

    s = a + b
    m = a - b
    u = a * b
    try:
        d = a / b
    except ZeroDivisionError:
        print ('\nДелить на ноль нельзя! \nВот и сказочке конец..')
        break

    if c == '1':
        print ('\nВаш результат: ' + str (s))
    if c == '2':
        print ('\nВаш результат: ' + str (m))
    if c == '3':
        print ('\nВаш результат: ' + str (u))
    if c == '4':
        print ('\nВаш результат: ' + str (d))

    qw = input ('\nНажмите Enter для продолжения. Для выхода нажмите 0. ')
    if qw == '0':
        print('\nGAME OVER')
        break
