#!/usr/bin/env python3

'''
Используйте функцию zip(), чтобы создать словарь movies, который объединяет в пары эти списки: titles = ['Creature of Habit', 'Crewel Fate'] и plots = ['A nun turns into a monster', 'A haunted yarn shop'].
'''

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)
