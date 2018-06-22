#!/usr/bin/env python3

'''
Присвойте значение 7 переменной guess_me. Далее напишите условные провер- ки (if, else и elif), чтобы вывести строку 'too low', если значение переменной guess_me меньше 7, 'too high', если оно больше 7, и 'just right', если равно 7.
'''

try:
    guess_me = int(input('Type guess_me: '))
except Exception as err:
    print('Something wrong:', err)
    exit(1)

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')
