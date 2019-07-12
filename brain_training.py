#! /usr/bin/env python3

"""
    Программа случайным образом предлагает для решения либо умножение,
    либо сложение, либо вычитание двух двузначных чисел.
    Пользователю дается три попытки. Если все попытки не правильны,
    программа выводит верный ответ и предлагает новый пример для решения.
"""

from random import randint


def brain_training():
    while True:
        choice = randint(1, 3)
        number1 = randint(12, 99)
        number2 = randint(12, 99)
        if choice == 1:
            result = number1 * number2
            user_answer('*', number1, number2, result)
        elif choice == 2:
            result = number1 + number2
            user_answer('+', number1, number2, result)
        else:
            result = number1 - number2
            user_answer('-', number1, number2, result)


def user_answer(znak, number1, number2, result):
    print('Сколько будет {} {} {}'.format(number1, znak, number2))
    for i in range(3):
        answer = input('Ваш ответ: ')
        if answer == str(result):
            print('Правильно!')
            break
        else:
            print('Не совсем...')
    else:
        print('Правильный ответ: {}'.format(result))


brain_training()

