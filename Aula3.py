# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:31:41 2023

@author: Mateus Campos
"""

print("Informe dois números")
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
r = n1 + n2
print(n1, "+", n2, "=", r)
r = n1 - n2
print(n1, "-", n2, "=", r)
r = n1 * n2
print(n1, "*", n2, "=", r)
r = n1 / n2
print(n1, "/", n2, "=", r)

print("Informe os dados")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = int(input("Idade: "))
mensagem = nome + " " + sobrenome + ", " + str(idade)
print(mensagem)