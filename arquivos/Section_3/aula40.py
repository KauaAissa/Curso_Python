# Inicio do loop infinito da calculadora
while True:

    # Codigo
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Diigite o segundo numero: ')
    operador = input('Digite o operador (+ - / *): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    # Validacao de numeros
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
            print('Algum dos valores passados estavam incorretos')
            continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
            print('O operador nao esta correto')
            continue

    if len(operador) > 1:
            print('Escolha apenas um operador')
            continue

    # Parte de calculos
    print('Confira o resultado:')

    if operador == '+':
            print(numero_1_float + numero_2_float)
    elif operador == '-':
            print(numero_1_float - numero_2_float) 
    elif operador == '/':
            print(numero_1_float / numero_2_float) 
    elif operador == '*':
            print(numero_1_float * numero_2_float) 
    else:
            print('Algo não deu certo, porfavor tente novamente')


    # Logica para sair do loop
    sair = input('Quer sair? [s]: sim ').lower().startswith('s')
    if sair is True:
        break