'''I want to make bot-helper in console. It will be give me ready answer to client\'s questions'''

from colorama import Fore, Back, Style

while True:
    print ('\n1. Магазин')
    print ('2. Доставка')
    print ('3. Благодарности')
    print ('4. Ошибки')
    print ('5. Проблемы')
    print ('0. Выход')

    a = '\n1. Ситуация 1'
    b = '2. Ситуация 2'
    c = '3. Ситуация 3'
    d = '4. Ситуация 4'
    e = '5. Ситуация 5'

    qu = input ('\nВыберите действие: ')

    if qu == '1':
        print (a)
        print (b)
        print (c)
        print (d)
        print (e)

        qu1 = input ('\nВыберите действие: ')
        if qu1 == '1':
            print (Fore.RED + '\nВаш ответ 1' + Style.RESET_ALL)
        if qu1 == '2':
            print (Fore.RED + '\nВаш ответ 2' + Style.RESET_ALL)
        if qu1 == '3':
            print (Fore.RED + '\nВаш ответ 3' + Style.RESET_ALL)
        if qu1 == '4':
            print (Fore.RED + '\nВаш ответ 4' + Style.RESET_ALL)
        if qu1 == '5':
            print (Fore.RED + '\nВаш ответ 5' + Style.RESET_ALL)

        quu = input('\nДля продолжения нажмите ' + Fore.RED + 'Enter: ' + Style.RESET_ALL)

    '''add other module of the menu'''

    aa = '\n1. Ситуация 1'
    bb = '2. Ситуация 2'
    cc = '3. Ситуация 3'
    dd = '4. Ситуация 4'
    ee = '5. Ситуация 5'

    if qu == '2':
        print(aa)
        print(bb)
        print(cc)
        print(dd)
        print(ee)

        qu1 = input('\nВыберите действие: ')
        if qu1 == '1':
            print(Fore.RED + '\nВаш ответ 1' + Style.RESET_ALL)
        if qu1 == '2':
            print(Fore.RED + '\nВаш ответ 2' + Style.RESET_ALL)
        if qu1 == '3':
            print(Fore.RED + '\nВаш ответ 3' + Style.RESET_ALL)
        if qu1 == '4':
            print(Fore.RED + '\nВаш ответ 4' + Style.RESET_ALL)
        if qu1 == '5':
            print(Fore.RED + '\nВаш ответ 5' + Style.RESET_ALL)

        quu = input('\nДля продолжения нажмите ' + Fore.RED + 'Enter: ' + Style.RESET_ALL)

    """than you can add other modules of the menu as you want"""

    '''finish question'''

    if qu == '0':
        print(Fore.RED + '\nДо встречи!' + Style.RESET_ALL)
        break
