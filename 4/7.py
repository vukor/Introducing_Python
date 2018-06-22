#!/usr/bin/env python3

'''
Используйте включение генератора, чтобы вернуть строку 'Got' и количество чисел в диапазоне range(10). Итерируйте по нему с помощью цикла for.
'''

numbers = (number for number in range(10))

count = 0
for number in numbers:
    count += 1

print('Got', count)
