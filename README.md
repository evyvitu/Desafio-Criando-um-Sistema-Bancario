# 💰 Sistema Bancário em Python (Terminal)

## 🧾 Sobre o Projeto

Foi desenvolvido um sistema bancário em Python, operando via terminal, que permite gerenciar usuários e contas bancárias, além de realizar operações como depósitos, saques e emissão de extratos. O programa controla limites por operação, quantidade de saques, além de registrar todas as movimentações.

Este sistema foi desenvolvido como evolução do Desafio: Criando um Sistema Bancário, que faz parte do bootcamp Santander 2025 - Back-End com Python, promovido pela DIO (Digital Innovation One).

---

## 📌 Funcionalidades

- **[1] Depositar**: Permite adicionar dinheiro a uma conta existente.
- **[2] Sacar**: Permite retirar dinheiro de uma conta, respeitando:
  - Limite de saque por operação: R$ 500,00
  - Máximo de 3 saques por conta
  - Saldo suficiente
- **[3] Extrato**: Exibe o histórico de transações e o saldo atual.
- **[4] Criar Usuário**: Cadastra um novo usuário informando:
   - Nome completo
   - Data de nascimento
   - CPF (único)
   - Endereço
- **[5] Criar Conta**: Cria uma conta vinculada a um usuário já cadastrado.
   - Agência padrão: 0001
   - Número da conta gerado automaticamente
- **[6] Listar Usuários**: Mostra todos os usuários cadastrados.
- **[7] Listar Contas**: Mostra todas as contas criadas, com titular e CPF.
- **[0] Sair**: Encerra o programa.
  
---

## ⚙️ Requisitos

- Python 3.x instalado em sua máquina.

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/evyvitu/Desafio-Criando-um-Sistema-Bancario

2. Acesse a pasta do projeto:
   ```bash
   cd Desafio-Criando-um-Sistema-Bancario
   
3. Execute o script:
   ```bash
   python desafio.py

---

## 📸 Exemplo de uso  
MENU:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Usuários
[7] Listar Contas
[0] Sair

Escolha uma opção: 4  
CPF (somente números): 12345678900  
Nome completo: João da Silva  
Data de nascimento (dd-mm-aaaa): 01-01-1990  
Endereço: Rua A, 100 - Centro - São Paulo/SP  
Usuário criado com sucesso!

Escolha uma opção: 5  
CPF do usuário: 12345678900  
Conta criada com sucesso! Agência: 0001, Conta: 1

Escolha uma opção: 1  
--- Lista de Contas ---  
Agência: 0001, Conta: 1, Titular: João da Silva (CPF: 12345678900)  
Digite o número da conta: 1  
Valor do depósito: R$ 200.00  
Depósito realizado com sucesso!

---
