#!/usr/bin/env python3

'''
Присвойте значение 7 переменной guess_me и значение 1 переменной start. Напишите цикл while, который сравнивает переменные start и guess_me. Выве- дите строку 'too low', если значение переменной start меньше значения пере- менной guess_me. Если значение переменной start равно значению переменной guess_me, выведите строку 'found it!' и выйдите из цикла. Если значение пере- менной start больше значения переменной guess_me, выведите строку 'oops' и выйдите из цикла. Увеличьте значение переменной start на выходе из цикла.
'''

guess_me = 7
start = 1

while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1
