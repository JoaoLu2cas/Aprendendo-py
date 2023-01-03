import random

user_win = 0
bot_win = 0

options = ['pedra','papel','tesoura']

while True :
    user_input = input('Escolha pedra/papel/tesoura ou pressione S para sair: ').lower()
    if user_input == 's' :
        break
    if user_input not in options :
        print('Escolha uma das opções pedra/papel/tesoura ')
        continue
    random_number = random.randint(0, 2)
    #0pedra 1papel 2tesoura
    bot_pick = options[random_number]
    print('O bot escolheu', bot_pick + '.')

    if user_input == 'pedra' and bot_pick == 'tesoura':
        print('Você ganhou!!')
        user_win += 1
    elif user_input == 'papel' and bot_pick =='pedra' :
        print('Você ganhou!!')
        user_win += 1
    elif user_input == 'tesoura' and bot_pick == 'papel' :
        print('Você ganhou!!')
        user_win += 1
    elif user_input == bot_pick :
        print('Uau!! Vocês pensaram igual!')
        continue
    else :
        print('Você perdeu!') 
        bot_win += 1   
print(f'Você ganhou : {user_win} vezes!')
print(f'Você perdeu : {bot_win} vezes!')
print('Foi divertido,byebye!!')


