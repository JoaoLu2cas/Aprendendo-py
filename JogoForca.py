'''jogo da forca'''
import random

print('Bem-vindo ao jogo da forca')
print('Você terá 6 chances para erras,escolha bem .')

banco_palavras = ['chuva','monitor','teclado','notebook','livro','mesa','programdor']
numero_random = random.randint(0, 7)
palavra_secreta = banco_palavras[numero_random].upper()
letras_acertadas = ''
numero_tentativa = 0
contador = 0

while True :
     letra_digitada=input('Digite uma letra : ').upper()
     if numero_tentativa == 5 :
        print('Você perdeu,errou a letra 7x')
        print(f'A palava secreta era {palavra_secreta}')
        break
     if len(letra_digitada) > 1 :
        print('Digite apenas uma letra.')
        continue
     if letra_digitada in palavra_secreta :
        letras_acertadas += letra_digitada
     if letra_digitada not in palavra_secreta:
        numero_tentativa += 1
        contador += 1
        print(f'Você já errou {contador} vezes.')
     if contador == 1 :
        print('CABEÇA')
     elif contador == 2 :
        print('CABEÇA,CORPO')
     elif contador == 3 :
        print('CABEÇA,CORPO,PERNA DIREIRA')
     elif contador == 4 :
        print('CABEÇA,CORPO,PERNA DIREIRA,PERNA ESQUERDA')
     elif contador == 5 :
        print('CABEÇA,CORPO,PERNA DIREIRA,PERNA ESQUERDA,BRAÇO DIREITO')
     elif contador == 6 :
        print('CABEÇA,CORPO,PERNA DIREIRA,PERNA ESQUERDA,BRAÇO DIREITO,BRAÇO ESQUERDO')
    
     palavra_formada =''
     for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas :
            palavra_formada += letra_secreta
        else :
            palavra_formada += '*'
     print(palavra_formada)
     if palavra_formada == palavra_secreta :
        print('Parabéns você ganhou!!')
        print(f'A palava secreta era {palavra_secreta}')
        break

