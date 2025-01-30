import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este indice')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Não há nenhum item a ser listado')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Escolha uma opção valida')