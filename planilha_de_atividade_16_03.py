# -*- coding: utf-8 -*-
"""planilha de atividade 16-03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i8R8UqYeGaPN5WXfhVQijjN_rZoXDA8L
"""

nome = input("Qual é o seu nome?")
bingus = 0
anodenascimento= int(input("Qual ano você nasceu? "))
mesdenascimento= int(input("Qual é o mês que você nasceu "))
anocalc1 = (2022 - anodenascimento)
if mesdenascimento > 3 :
  bingus= 1
anocalc2 = (anocalc1 - bingus)
idade= anocalc2

print("Olá", nome, ", você tem" ,idade, "anos")

nota1= int(input("nota peso 2 "))

nota2= int(input("nota peso 4 "))

nota3= int(input("nota peso 6 "))

media = (nota1 + nota2 + nota3 /3)
print("média igual a", media)

custo_fabrica= float(input("Valor de fabrica "))

porcentagem_d= 0.28

impostos= 0.45

custo = custo_fabrica * porcentagem_d + custo_fabrica * impostos + custo_fabrica

print("o custo de fábrica é", custo_fabrica, "O custo para o consumidor é", custo)

refri = 1
batatinha = 2
cereal = 3
agua = 4
agua_gas = 5
achocolatado = 6
menta = 7
escolha = int(input("valor de 1 a 7"))
if(escolha == 1):
  print("Refrigerante de cola")
elif (escolha == 2):
  print("Batata-frita") 
elif (escolha == 3):
  print("Barra de cereal")
elif (escolha == 4):
  print("Água")
elif (escolha == 5):
  print("Água com gás")
elif (escolha == 6):
  print("Achocolatado")
elif (escolha == 7):
  print("Bala de menta")