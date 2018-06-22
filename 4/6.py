#!/usr/bin/env python3

'''
Используйте включение множества, чтобы создать множество odd, которое содержит четные числа в диапазоне range(10).
'''

odd = { number for number in range(10) if number % 2 == 0 }
print(odd)
