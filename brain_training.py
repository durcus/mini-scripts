#! /usr/bin/env python3

"""
    Программа случайным образом предлагает для решения либо умножение,
    либо сложение, либо вычитание двух двузначных чисел.
    Пользователю дается три попытки. Если все попытки не правильны,
    программа выводит верный ответ и предлагает новый пример для решения.
"""

from random import randint


def brain_training():
    choice = randint(1, 3)
    number1 = randint(12, 99)
    number2 = randint(12, 99)
    if choice == 1:
        result = number1 * number2
        user_answer(choice, number1, number2, result)
    elif choice == 2:
        result = number1 + number2
        user_answer(choice, number1, number2, result)
    else:
        result = number1 - number2
        user_answer(choice, number1, number2, result)


def user_answer(choice, number1, number2, result):
    pass


def compare(answer, result):
    pass


brain_training()

