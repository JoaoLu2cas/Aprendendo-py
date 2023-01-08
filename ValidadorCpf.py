entrada = input('Digite o CPF : ')
soma_nove = entrada[:9]
contador_regressivo = 10 

resultado_digito_1 = 0

for digito in soma_nove :
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) %  11
digito_1 = digito_1 if digito_1 <= 9 else 0

soma_dez = soma_nove + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in soma_dez :
    resultado_digito_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 

cpf_gerado_pelo_calculo = f'{soma_nove}{digito_1}{digito_2}'

if entrada == cpf_gerado_pelo_calculo :
    print('CPF válido.')
else :
    print('CPF inválido')