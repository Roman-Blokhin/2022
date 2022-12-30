'''I want to make bot-helper in console. It will be give me ready answer to client\'s questions'''

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
        print ('\nВаш ответ 1')
    if qu1 == '2':
        print ('Ваш ответ 2')
    if qu1 == '3':
        print ('Ваш ответ 3')
    if qu1 == '4':
        print ('Ваш ответ 4')
    if qu1 == '5':
        print ('Ваш ответ 5')
