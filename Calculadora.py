# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:09:50 2023

@author: Mateus Campos
"""

while True:
    print('Calculadora (+, -, *, /) ')
    print('s: sair')
    resp = input('Informe a operação desejada (s para sair): ')
    if resp == 's':
        break
    print('Informe dois números: ')
    n1 = float(input())
    n2 = float(input())
    if resp == '+':
        r = n1 + n2
    elif resp == '-':
        r = n1 - n2
    elif resp == '*':
        r = n1 * n2
    elif resp == '/':
        r = n1 / n2
    elif resp == '**':
        r = n1 ** n2
    else:
        print('Operação inválida!')
        continue
    print(n1, resp, n2, '=', r)
        