# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:57:34 2023

@author: Mateus Campos
"""

nome_completo = input("informe seu nome completo: ")
sobrenome = input("informe seu sobre nome: ")

pos = nome_completo.find(sobrenome)

if pos != -1:
    print("Seu sobrenome começa na posição ", pos)
else:
    print("Sobrenome não encontrado")
    
n = float(input("informe um número: "))
print("{n:.8f}".format(n=n))