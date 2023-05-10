# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:34:23 2023

@author: Mateus Campos
"""

total_horas = int(input("Informe os minutos para serem convertidos em horas: "))

minutos = total_horas//60
segundos = total_horas%60
horas = minutos%60
minutos %= 60
print(horas,":",minutos,":",segundos) 