import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepósitos
    [2]\tSaques
    [3]\tExtratos
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,depositos,/):
    saldo += valor
    depositos.append(valor)
    print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
    return saldo, depositos


def sacar(*, saldo, valor, saques,contador_saque_diario):
    if saldo > valor:
        saldo -= valor
        saques.append(valor)
        contador_saque_diario += 1
        print(f"\nOperação concluída! Saldo atual: R$ {saldo:.2f}.\n")
    else:
        print(f"\nSaldo insuficiente! Saldo atual: R$ {saldo:.2f}.\n")
    return saldo, saques, contador_saque_diario


def exibir_extrato(saldo,extrato, /, *, depositos,saques):
    if len(depositos) == 0 and len(saques) == 0:
        print("\n================ EXTRATO ================\n")
        print ("\nNão foram realizadas movimentações.\n")
        print(f"\nSaldo: R$ {saldo:.2f}\n")                
        print("==========================================\n")
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


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
   
    operacao = True
    AGENCIA = "0001"
    usuarios = []
    contas = []
    depositos = []
    contador_saque_diario = 0
    saques = []
    extrato = {}
    saldo = 0
   
    while operacao:
        print("\nOperações Bancárias\n")

        operacao = menu()

        #Tratamento de excessão float para o valor inserido
        try:
            #Operação depósito
            if operacao == "1":
                print("\nOperação de Depósito\n")
                deposito = input("Valor do depósito: ")
                deposito = float(deposito)
                saldo,depositos = depositar(saldo,deposito,depositos)

            #Operação saque
            elif operacao == "2":
                print("\nOperação de Saque\n")
                if contador_saque_diario <= 3:
                    saque = input("Valor do saque: ")
                    saque = float(saque)
                    saldo,saques,contador_saque_diario = sacar(
                        saldo=saldo,
                        valor=saque,
                        saques=saques,
                        contador_saque_diario=contador_saque_diario,
                    )
                else:
                    print("Você excedeu o limite de saques diário!")

            #Operação extrato
            elif operacao == "3":
                exibir_extrato(saldo,extrato,depositos=depositos,saques=saques)

            
            elif operacao == "6":
                criar_usuario(usuarios)

            elif operacao == "4":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            elif operacao == "5":
                listar_contas(contas)
            
            #Opção errada
            else:
                print("Você selecionou uma operação incorreta!\n")

        #Final da excessão
        except:
            print("\nOcorreu algum erro!!!\n")
            operacao = False

main()