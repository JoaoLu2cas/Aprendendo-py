'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.'''

quilometros_rodados = float(input('Quantos Km foram percorridos? : '))
dias = int(input('Quantos dias o carro foi alugado ?: '))
carro_dia = 60
total_a_pagar = carro_dia*dias + 0.15*quilometros_rodados

print(f'Você irá pagar um total de R$ : {total_a_pagar:.2f}')
