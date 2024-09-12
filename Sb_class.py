from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def exibir(self):
        if not self._transacoes:
            print("Nenhuma transação registrada.")
        else:
            print("Histórico de transações:")
            for transacao in self._transacoes:
                print(f" - {transacao['data']} - {transacao['tipo']} de R$ {transacao['valor']:.2f}")

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        cliente.adicionar_conta(self)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n!!! Operação falhou! O valor informado é inválido. !!!")
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n!!! Operação falhou! Saldo insuficiente ou valor inválido. !!!")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self._historico.transacoes if transacao["tipo"] == "Saque"]
        )

        excedeu_limite = valor > self._saldo + self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_saques:
            print("\n!!! Operação falhou! Número máximo de saques excedido. !!!")
            return False

        if excedeu_limite:
            print("\n!!! Operação falhou! O valor do saque excede o limite. !!!")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self._cliente.nome}
        """

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

class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def buscar_cliente(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_conta(self, numero_conta):
        for conta in self._contas:
            if conta.numero == numero_conta:
                return conta
        return None

# Interface do usuário
banco = Banco()

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ").strip()
    if banco.buscar_cliente(cpf):
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/estado): ").strip()
    
    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    banco.adicionar_cliente(cliente)
    print("Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do cliente: ").strip()
    cliente = banco.buscar_cliente(cpf)
    
    if cliente:
        numero_conta = input("Informe o número da conta: ")
        limite = float(input("Informe o limite da conta corrente: "))
        limite_saques = int(input("Informe o limite de saques diários: "))
        
        nova_conta = ContaCorrente(numero_conta, cliente, limite, limite_saques)
        banco.adicionar_conta(nova_conta)
        print(f"Conta {numero_conta} criada com sucesso!")
    else:
        print("Cliente não encontrado.")

def realizar_saque():
    numero_conta = input("Informe o número da conta: ")
    conta = banco.buscar_conta(numero_conta)
    
    if conta:
        valor = float(input("Informe o valor do saque: "))
        saque = Saque(valor)
        saque.registrar(conta)
    else:
        print("Conta não encontrada.")

def realizar_deposito():
    numero_conta = input("Informe o número da conta: ")
    conta = banco.buscar_conta(numero_conta)
    
    if conta:
        valor = float(input("Informe o valor do depósito: "))
        deposito = Deposito(valor)
        deposito.registrar(conta)
    else:
        print("Conta não encontrada.")

def exibir_historico():
    numero_conta = input("Informe o número da conta: ")
    conta = banco.buscar_conta(numero_conta)
    
    if conta:
        conta.historico.exibir()
    else:
        print("Conta não encontrada.")

def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Criar usuário")
        print("2. Criar conta")
        print("3. Realizar saque")
        print("4. Realizar depósito")
        print("5. Exibir histórico de transações")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            criar_conta()
        elif opcao == '3':
            realizar_saque()
        elif opcao == '4':
            realizar_deposito()
        elif opcao == '5':
            exibir_historico()
        elif opcao == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
