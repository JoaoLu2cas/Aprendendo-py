'''Ecreva um programa que registre o caixa de um banco.
O programa começa perguntando se o usuário quer criar uma conta ou fechar o programa.
Se ele escolher fechar,escreva uma mensagem de agradecimento e feche.
Caso contrario ele pedirá que o usuário insira um número de 6 dígitos
e,entao,se o número não existir no banco,ele irá pedir um valor de depósito
depois o banco pergunta se deseja ver o valor do saldo,se sim ele deverá
imprime o balanço geral do banco,senão ele entrará em looping'''

contas = []
depositos = []
saldo = 0

def main():
    opçao = bool(int(input('Deseja ver ou criar um programa (1) ou fechar o programa(0): ')))
    while opçao :
        criarContas()
        verSaldo()
        opçao = bool(int(input('Deseja ver ou criar um programa (1) ou fechar o programa(0): ')))

def criarContas():
    global contas, depositos, saldo
    num_conta = int(input('Digite o número da conta: '))

    while num_conta in contas :
        print('Conta já existente,digite novamente.')
        num_conta = int(input('Digite o número da conta: '))

    contas.append(num_conta)
    deposito = float(input('Digite o valor do primeiro depósito: '))
    while deposito <= 0 :
        print('Valor do depósito inválido')
        deposito = float(input('Digite o valor do primeiro depósito: '))
    depositos.append(deposito)
    saldo += deposito

def verSaldo():
    global saldo 
    opçao = bool(int(input('Deseje ver o saldo do banco - Sim(1) / Não(0): ')))
    if opçao :
        print('O saldo do banco é R$',saldo)

main()
        
