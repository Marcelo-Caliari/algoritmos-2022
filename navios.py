# -*- coding: utf-8 -*-
"""Navios.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQiiTnKpLreUDMN512aZ-HFxFC9rsZOP
"""

import time

status = "AGUARDANDO"

while ( status == "AGUARDANDO" ):
    grupos = [
        {
            "codigo": 1,
            "nome": "Grupo 1",
            "herois": "Dr. Estranho, Wanda, Aquaman, Thor.",
            "historia": "Wanda levanta a areia do fundo, Dr estranho abre um portal e leva embora, Thor Cria uma chuva torrencial e Aquaman cria uma onda de água com o aumento de água criado por Thor"
        },
        {
            "codigo": 2,
            "nome": "Grupo 2",
            "herois": "Cyborg, Hulk, Capitão América, Mulher Maravilha.",
            "historia": "Mulher maravilha engata o laço puxando o navio, Capitão América usa o escudo para quebrar a parede, Hulk levanta o navio."
        },
        {
            "codigo": 3,
            "nome": "Grupo 3",
            "herois": "Flash, Batman, Homem de Ferro, Homem Aranha.",
            "historia": "Batman e Homem de ferro usam pequenos robôs que filtram a areia, Flash tira as pessoas abordo, e junto com o homem aranha empurram o navio."
        }
    ]

    print("SISTEMA ABERTO")

    print('Insira o login administrador')
    auth = False

    while auth == False:
        nome = input("Insira o nome de usuário: ")
        senha = input("Insira a sua senha: ")
        if(senha == 'admin'):
            print('você está logado')
            auth = True
        else:
            print('Usuario ou senha incorretos')
            auth = False


    print("ALERTA!")
    print("SR(A)", nome, ", RECEBEMOS UMA NOTIFICAÇÃO DE EMERGÊNCIA NO CANAL DE SUEZ (EGITO), UM NAVIO CHAMADO EVER GIVEN ENCALHOU ENQUANTO NAVEGAVA \n PARA O MEDITERRÂNEO, COMO MEMBRO DA AGÊNCIA DE HERÓIS, PEDIMOS PARA QUE ENVIEM UM GRUPO DE SUPER-HERÓIS AO LOCAL PARA LIBERAR A PASSAGEM!")

    print("No momento temos os seguintes grupos disponiveis:")

    confirmar_escolha_grupo = "N"

    while confirmar_escolha_grupo == "N":
        # Escolha dos herois
        for temp_grupo in grupos:
            print("[", temp_grupo["codigo"], "]",
                temp_grupo["nome"], ": ", temp_grupo["herois"])

        grupo_selecionado = {}
        grupo_resp = int(input("Digite o número para escolher uma equipe: "))
        for temp_grupo in grupos:
            if temp_grupo["codigo"] == grupo_resp:
                grupo_selecionado = temp_grupo
        if grupo_selecionado["codigo"]:
            print("Equipe selecionada: ", grupo_selecionado["nome"])
            print("Herois: ", grupo_selecionado["herois"])

        confirmar_escolha_grupo = input("Deseja confirmar sua escolha? (S/N): ")

    # Mostrar história das equipes
    print("A equipe foi enviada para o local da emergência e os herois logo entraram em ação.")
    print(grupo_selecionado["historia"])

    # Viloes aparecem
    print("AVISO URGENTE! \n UM GRUPO DE VILÕES CHEGOU ATÉ O LOCAL DO CONVÉS!")
    time.sleep(1)
    print("Inicializando escaneamento facial... \n por favor aguarde...")
    time.sleep(2)
    print("Escaneamento concluido!")
    time.sleep(1)
    print("ULTRON, CORINGA, ABUTRE, DOUTOR OCTOPUS.")
    time.sleep(1)

    resposta_permitido_atacar = input(
        "Deseja liberar o grupo de super-heróis para contra atacar? (S/N): ")
    is_permitido_atacar = False
    if(resposta_permitido_atacar == "S"):
        is_permitido_atacar = True
        print("os heróis vão atacar")
    if(resposta_permitido_atacar == "N"):
        print("os vilões vão atacar o navio")

    herois_vencem = is_permitido_atacar

    if (herois_vencem):
        print("Os herois derrotaram os vilões, porém a missão continua.")
        # Caminho Herois Vencem
        pontuacao = 0
        angulo_atual = 45
        angulo_ideal = 180
        is_navio_preso = True

        print('Herois: - Qual é o relatório da situação?')
        print('==================DADOS DO SCANNER====================')
        print("Navio está preso: ", ("SIM" if is_navio_preso else "NÃO"))
        print("Angulo em relação ao canal: ",
            angulo_atual, "º ideal(", angulo_ideal, "º)")
        print('======================================================')

        desprender_navio = ""
        if (is_navio_preso):
            desprender_navio = input(
                "Deseja enviar forças para desprender o navio? (S/N): ")

        is_navio_preso = not (desprender_navio == "S")

        print('==================DADOS DO SCANNER====================')
        print("Navio está preso: ", ("SIM" if is_navio_preso else "NÃO"))
        print("Angulo em relação ao canal: ",
            angulo_atual, "º ideal(", angulo_ideal, "º)")
        print('======================================================')

        print("Você ainda precisa corrigir o angulo do navio para desencalhá-lo")
        while angulo_atual != angulo_ideal:
            angulo_restante = int(
                input("Adicione quantos angulos faltam para o navio chegar ao angulo ideal:"))
            angulo_atual = angulo_atual + angulo_restante
            print('==================DADOS DO SCANNER====================')
            print("Navio está preso: ", ("SIM" if is_navio_preso else "NÃO"))
            print("Angulo em relação ao canal: ",
                angulo_atual, "º ideal(", angulo_ideal, "º)")
            print('======================================================')

        pontuacao_navio_preso = 40 if not is_navio_preso else 0
        pontuacao_angulo = 60 if angulo_atual == angulo_ideal else 0
        pontuacao = pontuacao_navio_preso + pontuacao_angulo

        if (pontuacao == 100):
            print("Parabens! Você e a equipe escolhida desencalharam o navio e com combateram os vilões")
        else:
            print("Que pena! Você combateu os vilões porem o navio ainda não foi desencalhado")

        print('======================================================')
        print("Sua pontuação foi ", pontuacao)
        print('======================================================')
        status = "FINALIZADO"
    else:
        # Caminho Herois Perdem
        opcao = input ("Você permite que o Doutor Estranho volte no tempo? (S/N): ")
        if (opcao == "S"):
            print("Permissão Concedida! Doutor Estranho irá rebobinar o tempo: ")
        else: 
            print("Que Pena! Missão fracassou e o navio foi destruido")
            status = "FINALIZADO"