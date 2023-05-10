# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:07:09 2023

@author: Mateus Campos
"""

n = int(input('Informe o número de elementos do conjuto: '))

print('Elementos: ', end=' ')
for cont in range (1, n+1):
    print(cont, end=' ')
    
print('\nSubconjuntos: ', end=' ')
for cont in range(1, n+1):
    for cont2 in range(cont+1, n+1):
        print('(', cont, ', ', cont2, ')', sep='', end=' ')
