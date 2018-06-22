#!/usr/bin/env python3

'''
Определите декоратор test, который выводит строку 'start', когда вызывается функция, и строку 'end', когда функция завершает свою работу.
'''

def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('Result:', result)
        print('end')
        return result
    return new_function

@test
def hello():
    return 'Hello!'

print(hello())
