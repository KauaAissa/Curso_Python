primeiro_valor = input('Escreva o primeiro valor ')
segundo_valor = input('Escreva o segundo valor ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print('O (primeiro) valor é maior que o (segundo)')
elif segundo_valor > primeiro_valor:
    print('o (segundo) valor é maior que o (primeiro)')
elif primeiro_valor == segundo_valor:
    print('Os valores sao iguais')
else:
    print('Valor incorreto ou erro')