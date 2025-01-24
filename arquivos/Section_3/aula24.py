# nome = 'kaua'

# print(nome[1])

# print('a' in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else: 
    print('Nao foi encontrado')