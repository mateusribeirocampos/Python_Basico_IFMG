# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:45:02 2023

@author: Mateus Campos
"""

n1 = int(input("informe um número: "))
n2 = int(input("informe outro número: "))
p = (n1 > n2)
q = (n1 != n2)
r = not(p or q) and (not p)
print("p =", p)
print("q =", q)
print("r =", r)