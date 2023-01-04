import random
user_win = 0
bot_win = 0
opcao = ['1','2','3','4','5','6']
while True :
    user_input = input('Bem vindo a roleta russa, voce tem coragem de brincar, escolha um numero de 1 a 6 ou digite [s]air: ').lower()
    if user_input =='s' :
        print('Você peidou na farofa hahaha')
        break
    if user_input not in opcao :
        print('escolha um numero de 1 a 6 .')
        continue
    user_input_int = int(user_input)
    random_number = random.randint(0, 5)

    bot_pick = opcao[random_number]

    if bot_pick == user_input :
        print('BANG!! Você morreu. :/ ')
        bot_win += 1
    else :
        print('Continue se tiver coragem.')
        user_win += 1

print(f'Você sobreviveu {user_win} vezes.')
print(f'Você morreu {bot_win} vezes.')
print('BYE BYE medroso !')
