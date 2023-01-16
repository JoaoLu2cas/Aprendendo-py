import random

print('Bem-vindo ao gerador de senhas')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&()-_+^,.?0123456789'

numero = input('Quantidade de de senhas desejadas: ')
numero = int(numero)

tamanho = input('Quantas letras essa senha deve ter?  ')
tamanho = int(tamanho)

for pwd in range(numero):
    senha = ''
    for c in range((tamanho)):
        senha += random.choice(chars)
    print(senha)



print('\nAqui está(m) sua(s) senha(s)')
