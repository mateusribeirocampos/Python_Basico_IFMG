# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:57:16 2023

@author: Mateus Campos
"""

soma = 0
while True:
    n = float(input('Informe um número: '))
    if n == 0:
        break
    soma += n
print('Soma dos números: ', soma)