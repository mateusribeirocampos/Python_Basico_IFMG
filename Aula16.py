# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:42:40 2023

@author: Mateus Campos
"""

try: 
    print('Informe dois números')
    n1 = float(input('n1: '))
    n2 = float(input('n2: '))
    r = n1 / n2
    print(n1, '/', n2, '=', r)
except:
    print('Ocorreu um erro!')