## -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:18:38 2023

@author: Mateus Campos
"""

import math

n = float(input("inform e um número: "))
x = n*math.pi
print("x = n*pi =", n)
print("Teto de x =", math.ceil(x))
print("Teto de x =", math.floor(x))
print("Log de x na base 10 =", math.log(x,10))
print("Raiz de x =", math.sqrt(x))
