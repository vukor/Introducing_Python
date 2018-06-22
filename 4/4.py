#!/usr/bin/env python3

'''
Используйте включение списка, чтобы создать список, который содержит не- четные числа в диапазоне range(10).
'''

odd_list = [item for item in range(10) if item % 2 == 1]
print(odd_list)
