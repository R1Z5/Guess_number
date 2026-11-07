# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

from decimal import Decimal, getcontext 
from math import pi

flag = False

if flag: 

    # Получаем случайное число в диапазоне от 1 до 100.
    number = randint(1, 100)
    print('Угадайте число от 1 до 100')

    while True:
        # Получаем число от пользователя и сохраняем его в переменную.
        guess = int(input('Введите число: '))

        # Если число меньше загаданного...
        if guess < number:
            # ...выводим сообщение.
            print('Ваше число меньше того, что загадано.')

        # Если число больше загаданного...
        elif guess > number:
            # ...выводим сообщение.
            print('Ваше число больше того, что загадано.')

        # Если число угадано...
        else:
            # ...выводим сообщение и прерываем выполнение программы.
            print('Отличная интуиция! Вы угадали число :)')
            break



for number in range(1, 100):
    if number % 10 == 1 and number != 11:
        print('плитка')
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        print('плитки')
    else:
        print('плиток')


print(number)
