'''I want to make bot-helper in console. It will be give me ready answer to client\'s questions'''

from colorama import Fore, Back, Style

while True:
    print ('\n1. Магазин')
    print ('2. Доставка')
    print ('3. Благодарности')
    print ('4. Ошибки')
    print ('5. Проблемы')

    a = '\n1. Мне не привезли заказ'
    b = '2. Мне привезли плохой товар'
    c = '3. Привезли не то'
    d = '4. Не доложили в заказ'
    e = '5. Не учли комментарий'

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

    qu0 = input ('\nДля продолжения нажмите ' + Fore.RED + 'Enter' + Style.RESET_ALL + ', для выхода ' + Fore.RED + '0'
                 + Style.RESET_ALL + ': ')
    if qu0 == '0':
        print(Fore.RED + '\nДо встречи!' + Style.RESET_ALL)
        break
