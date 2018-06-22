#!/usr/bin/env python3

e2f = {'cat': 'chat', 'dog': 'chien', 'walrus': 'morse'}
f2e = {}

for i in e2f.items():
    f2e[i[1]] = i[0]

print(e2f['walrus'])
print(f2e['chien'])
