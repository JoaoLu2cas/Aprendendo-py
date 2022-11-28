'''Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. 
Exiba o total de dias.'''


#Sabendo que 1 dia = 1440 min -> 144 cigarros 

cigarros = int(input('Quantos cigarros fumados por dia?: '))
anos = int(input('Quantos anos fumando ? : '))
total_cigarros = anos*365*cigarros
dias = total_cigarros//144
print(f'Você perdeu o total de : {dias:.2f} dias de vida')
