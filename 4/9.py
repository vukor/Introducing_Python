#!/usr/bin/env python3

'''
Определите функцию генератора get_odds, которая возвращает четные числа из диапазона range(10). Используйте цикл for, чтобы найти и вывести третье воз вращенное значение.
'''

def get_odds():
    for number in range(10):
        if number % 2 == 0:
            yield number

index = 0
for odd in get_odds():
    index += 1
    if index == 3:
        print(odd)
