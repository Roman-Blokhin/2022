while True:
    a = int (input('Введите первое число: '))
    b = int (input('Введите второе число: '))
    c = input('Выберите действие: \n1. + \n2. - \n3. * \n4. / \n')

    s = a + b
    m = a - b
    u = a * b
    d = a / b

    if c == '1':
        print ('Ваш результат: ' + str (s))
    if c == '2':
        print ('Ваш результат: ' + str (m))
    if c == '3':
        print ('Ваш результат: ' + str (u))
    if c == '4':
        print ('Ваш результат: ' + str (d))

    qw = input ('Нажмите Enter для продолжения. Для выхода нажмите 0. ')
    if qw == '0':
        print('GAME OVER')
        break
