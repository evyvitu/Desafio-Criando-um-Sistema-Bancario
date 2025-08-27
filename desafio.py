usuarios = []
contas = []
AGENCIA = "0001"

def menu():
    print("\n--- MENU ---")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Criar Usuário")
    print("[5] Criar Conta")
    print("[6] Listar Usuários")
    print("[7] Listar Contas")
    print("[0] Sair")
    return input("Escolha uma opção: ")

# Funções de Usuário

def criar_usuario():
    cpf = input("CPF (somente números): ").strip()
    if any(u['cpf'] == cpf for u in usuarios):
        print("CPF já cadastrado! Usuário não criado.")
        return
    
    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    
    usuario = {"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("\n--- Lista de Usuários ---")
    for u in usuarios:
        print(f"Nome: {u['nome']}, CPF: {u['cpf']}, Nascimento: {u['nascimento']}, Endereço: {u['endereco']}")

# Funções de Conta

def criar_conta():
    cpf = input("CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado! Crie o usuário primeiro.")
        return
    
    numero_conta = len(contas) + 1
    conta = {"agencia": AGENCIA, "numero": numero_conta, "usuario": usuario, "saldo": 0.0, "extrato": "", "saques": 0}
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {AGENCIA}, Conta: {numero_conta}")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print("\n--- Lista de Contas ---")
    for c in contas:
        print(f"Agência: {c['agencia']}, Conta: {c['numero']}, Titular: {c['usuario']['nome']} (CPF: {c['usuario']['cpf']})")

def selecionar_conta():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    listar_contas()
    numero = int(input("Digite o número da conta: "))
    conta = next((c for c in contas if c['numero'] == numero), None)
    if not conta:
        print("Conta não encontrada.")
    return conta

# Funções de Operações

def depositar():
    conta = selecionar_conta()
    if not conta:
        return
    valor = float(input("Valor do depósito: R$ "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")

def sacar():
    conta = selecionar_conta()
    if not conta:
        return
    valor = float(input("Valor do saque: R$ "))
    
    if valor <= 0:
        print("Valor inválido.")
    elif valor > conta['saldo']:
        print("Saldo insuficiente.")
    elif valor > 500:
        print("Limite de R$ 500 por saque excedido.")
    elif conta['saques'] >= 3:
        print("Limite diário de 3 saques atingido.")
    else:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
        conta['saques'] += 1
        print("Saque realizado com sucesso!")

def extrato():
    conta = selecionar_conta()
    if not conta:
        return
    print("\n--- Extrato ---")
    print(conta['extrato'] if conta['extrato'] else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

# Programa Principal

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            extrato()
        elif opcao == "4":
            criar_usuario()
        elif opcao == "5":
            criar_conta()
        elif opcao == "6":
            listar_usuarios()
        elif opcao == "7":
            listar_contas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()