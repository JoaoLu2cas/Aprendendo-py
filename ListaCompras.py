import os

lista = []

print('Bem-vindo a sua lista de compras.')
while True :
    print('Selecione uma das opções')
    opcao = input('[I]nserir,[L]istar,[A]pagar ou [S]air: ').lower()
    if opcao =='s' :
        print('Bye Bye.')
        break
    elif opcao == 'i' :
        os.system('cls')

        while True :
            print('Digite ''e'' para sair de inserir')
            inseir_loop = input('Item: ').lower()
            lista.append(inseir_loop)
            if inseir_loop == 'e':
                break
    elif opcao == 'l' :
        os.system('cls')

        if len(lista) == 0 :
            print('Não tem nada na lista')
        for i, inseir_loop in enumerate(lista) :
            print(i, inseir_loop)    
    elif opcao == 'a':
       indice_str = input(
        'Escolha um indice para apagar: '
       )
       try :
           indice = int(indice_str)
           del lista[indice]
       except ValueError :
            print('Não foi possivel apagar esse indice.')
       except IndexError :
            print('Esse indice nao existe.')
       except Exception :
            print('Erro desconhecido.')
    else:
        print('Por favor , escolha uma das opções')