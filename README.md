Sistema Bancário em Python
Descrição
Este projeto é um sistema bancário em Python que simula operações básicas de um banco, incluindo criação de usuários e contas, depósitos, saques e visualização do histórico de transações. O sistema é projetado para usar boas práticas de programação, como encapsulamento e abstração, e utiliza classes e métodos para organizar e gerenciar as funcionalidades.

Funcionalidades
Criação de Usuário: Permite a criação de novos usuários com informações como nome, CPF, data de nascimento e endereço.
Criação de Conta Corrente: Permite a criação de contas correntes associadas a usuários, com limite e número máximo de saques diários configuráveis.
Depósito: Permite adicionar dinheiro à conta.
Saque: Permite retirar dinheiro da conta, respeitando o saldo e o limite configurados.
Histórico de Transações: Permite visualizar o histórico de transações realizadas na conta.
Estrutura do Código
Classes
Cliente: Classe base para clientes, com atributos e métodos para gerenciar contas e realizar transações.
PessoaFisica: Herda de Cliente e adiciona atributos específicos como nome, CPF e data de nascimento.
Historico: Gerencia o histórico de transações realizadas.
Conta: Representa uma conta bancária, com métodos para depósitos e saques.
ContaCorrente: Herda de Conta e adiciona funcionalidades específicas para contas correntes, como limites de saque e de crédito.
Transacao: Classe abstrata para transações, com subclasses Deposito e Saque.
Banco: Gerencia clientes e contas, com métodos para adicionar e buscar informações.
Métodos Importantes
Cliente.adicionar_conta: Adiciona uma conta ao cliente.
Cliente.realizar_transacao: Realiza uma transação em uma conta específica.
Conta.depositar: Deposita um valor na conta.
Conta.sacar: Realiza um saque da conta.
ContaCorrente.sacar: Realiza um saque, considerando limites específicos.
Historico.adicionar_transacao: Adiciona uma transação ao histórico.
Historico.exibir: Exibe o histórico de transações.
Instruções de Uso
Criação de Usuário: No menu principal, selecione a opção para criar um usuário e informe as informações necessárias.
Criação de Conta: Após criar um usuário, você pode criar uma conta corrente associada a esse usuário.
Depósito: Selecione a opção de depósito e informe o valor a ser depositado.
Saque: Selecione a opção de saque e informe o valor a ser retirado.
Histórico de Transações: Visualize o histórico de transações da conta selecionada.
Exemplo de Execução
Ao executar o script, você verá um menu com opções para criar usuários, contas, realizar depósitos e saques, e exibir o histórico de transações. Basta seguir as instruções fornecidas pelo menu para interagir com o sistema.
