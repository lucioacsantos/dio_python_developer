'''
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 

O objetivo é implementar três operações essenciais: depósito, saque e extrato. 

O sistema será desenvolvido para um banco que busca monetizar suas operações. 

Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação 
Python e criar um sistema funcional que simule as operações bancárias.

Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver 
soluções práticas e eficientes.

Serão permitidas 3 operações de saque e o valor do saldo deve ser apresentado no formato R$ 1234.56

'''

#Lista com Operações de Depósito
depositos = []

#Lista com Operações de Saque máximo de três por dia
contador_saque_diario = 0
saques = []

#Dicionário com Extrato e Saldo no modelo R$ 1234.56
extrato = {}
saldo = 0

#Operação para início
operacao = True

while operacao:
    print("\nOperações Bancárias\n")

    #Tratamento de excessão float para o valor inserido
    try:
        #Operação depósito
        if operacao == "1":
            print("\nOperação de Depósito\n")
            deposito = input("Valor do depósito: ")
            deposito = float(deposito)
            saldo += deposito
            depositos.append(deposito)
            print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
            operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
            if operacao == "0":
                print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                operacao = False

        #Operação saque
        elif operacao == "2":
            print("\nOperação de Saque\n")
            if contador_saque_diario <= 3:
                saque = input("Valor do saque: ")
                saque = float(saque)
                if saldo > saque:
                    saldo -= saque
                    saques.append(saque)
                    contador_saque_diario += 1
                    print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                    operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
                    if operacao == "0":
                        print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                        operacao = False
                else:
                    print(f"\nSaldo insuficiente! Saldo atual: R$ {saldo:.2f}.\n")
                    operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
            else:
                print("Você excedeu o limite de saques diário!")
                operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
                if operacao == "0":
                    print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                    operacao = False     

        #Operação extrato
        elif operacao == "3":
            if len(depositos) == 0 and len(saques) == 0:
                print ("\nNão foram realizadas movimentações.\n")
                operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
                if operacao == "0":
                    print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                    operacao = False
            else:
                extrato["Depositos"] = depositos
                extrato["Saques"] = saques
                if len(depositos) != 0:
                    for valor in extrato["Depositos"]:
                        print(f"Depósito: R$ {valor:.2f}")
                if len(saques) != 0 :
                    for valor in extrato["Saques"]:
                        print(f"Saque: R$ {valor:.2f}")
                print(f"Saldo: R$ {saldo:.2f}\n")
                operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
                if operacao == "0":
                    print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                    operacao = False

        #Opção errada
        else:
            print("Você selecionou uma operação incorreta!\n")
            operacao = input("Selecione a operação desejada (1-Depósitos 2-Saques 3-Extratos 0-Sair): ")
            if operacao == "0":
                print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
                operacao = False

    #Final da excessão
    except:
        print("\nOcorreu algum erro!!!\n")
        operacao = False
