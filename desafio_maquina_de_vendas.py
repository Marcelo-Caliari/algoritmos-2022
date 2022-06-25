# -*- coding: utf-8 -*-
"""Desafio_Vending_Machine_Solved.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ywJCg4n8LinvW5WgkZVXnvbsAOxL5-6w
"""

opcoes = {
    "1": "Refrigerante de cola",
    "2": "Batata-frita",
    "3": "Barra de cereal",
    "4": "Água",
    "5": "Água com gás",
    "6": "Achocolatado",
    "7": "Bala de Menta",    
}

status = "AGUARDANDO"


while ( status == "AGUARDANDO" ):
  opcao = input( "Digite INICIAR para escolher um produto: " )
  if ( opcao != "INICIAR" ):
    print( "Você Digitou uma opção inválida, o programa terminou!" )
    status = "FINALIZADO"
  else:
    print( "Escolha um produto: " )
  
    for chave, valor in opcoes.items():
      print( chave + " = " + valor )
  
    print( "ou digite CANCELAR para retornar ao começo" )

    opcao = input("Digite o código do produto: ")

    if ( opcao != "CANCELAR" ):
      if ( opcao in opcoes ):
        print( "Você escolheu " + opcoes[opcao])
        confirmacao = input( "Digite CONFIRMAR para receber o produto: " )
        if (confirmacao == "CONFIRMAR"):
          print( "Obrigado por usar nossa máquina!" ) 
      else:
        print("Esse produto não existe")