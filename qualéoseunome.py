# -*- coding: utf-8 -*-
"""qualéoseunome.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17GA0TPsbul7zUx3CiPTjBPCRDEH_wJda
"""

nome = input("Qual é o seu nome? ")
print("Olá",nome)

salario = input("digite o seu salário: \n")
imposto = float(salario) * 0.25
print(imposto)

print("Qual é o seu rendimento anual?")
rendimento = float(input() )
if(rendimento <= 28000):
  print("Você está isento.")
  porcentagem = 0
elif(rendimento > 28000 and rendimento <= 35000):
  print("Você vai pagar 10%")
  porcentagem = 10
else:
  print("Você vai pagar 25%")
  porcentagem = 25
if(porcentagem > 0):
  imposto_pagar = rendimento * (porcentagem / 100)
  print("Você vai pagar", imposto_pagar)