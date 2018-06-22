#!/usr/bin/env python3

'''
Определите исключение, которое называется OopsException. Сгенерируйте его, чтобы увидеть, что произойдет. Затем напишите код, позволяющий поймать это исключение и вывести строку 'Caught an oops'.
'''

class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException:
    print('Caught an oops')
    exit(1)
