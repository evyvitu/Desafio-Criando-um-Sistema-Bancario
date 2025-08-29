from abc import ABC, abstractmethod
from datetime import datetime


# Classes de Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento


# Classes de Conta
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        elif valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
            return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        else:
            self.saldo += valor
            print("Depósito realizado com sucesso!")
            return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor):
        if valor > self.limite:
            print("Limite de R$ 500 por saque excedido.")
            return False
        elif self._saques_realizados >= self.limite_saques:
            print("Limite diário de 3 saques atingido.")
            return False
        elif super().sacar(valor):
            self._saques_realizados += 1
            return True
        return False


# Transações (Interface e Concretas)
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


# Funções do Sistema
clientes = []
contas = []

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


def criar_usuario():
    cpf = input("CPF (somente números): ").strip()
    if any(c.cpf == cpf for c in clientes):
        print("CPF já cadastrado!")
        return

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()

    cliente = PessoaFisica(nome, cpf, nascimento, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso!")


def criar_conta():
    cpf = input("CPF do usuário: ").strip()
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if not cliente:
        print("Usuário não encontrado! Crie o usuário primeiro.")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente(numero_conta, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {conta.agencia}, Conta: {conta.numero}")


def listar_usuarios():
    if not clientes:
        print("Nenhum usuário cadastrado.")
        return
    for c in clientes:
        print(f"Nome: {c.nome}, CPF: {c.cpf}, Nascimento: {c.nascimento}, Endereço: {c.endereco}")


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for c in contas:
        print(f"Agência: {c.agencia}, Conta: {c.numero}, Titular: {c.cliente.nome} (CPF: {c.cliente.cpf})")


def selecionar_conta():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    listar_contas()
    numero = int(input("Digite o número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if not conta:
        print("Conta não encontrada.")
    return conta


def depositar():
    conta = selecionar_conta()
    if not conta:
        return
    valor = float(input("Valor do depósito: R$ "))
    transacao = Deposito(valor)
    conta.cliente.realizar_transacao(conta, transacao)


def sacar():
    conta = selecionar_conta()
    if not conta:
        return
    valor = float(input("Valor do saque: R$ "))
    transacao = Saque(valor)
    conta.cliente.realizar_transacao(conta, transacao)


def extrato():
    conta = selecionar_conta()
    if not conta:
        return
    print("\n--- Extrato ---")
    for t in conta.historico.transacoes:
        print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"Saldo atual: R$ {conta.saldo:.2f}")


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