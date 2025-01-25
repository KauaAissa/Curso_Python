# 1 exercicio

# numero_str = input('Digite um numero inteiro: ')

# try:
#     numero_int = int(numero_str)
#     if (numero_int % 2) == 0:
#         print('Seu numero é par')
#     else:
#         print('Seu numero é impar')
# except:
#     print('Você nao digitou um numero')


# 2 exercicio

# hora_atual_str = input('Digite a hora atual: ')

# try:
#     hora_atual_int = int(hora_atual_str)

#     if hora_atual_int >= 0 and  hora_atual_int <= 11:
#         print('Bom dia')

#     elif hora_atual_int >= 12 and hora_atual_int <= 17:
#         print('Boa tarde')
    
#     elif hora_atual_int >= 18 and hora_atual_int <= 23:
#         print('Boa noite')
#     else:
#         print('Voce nao digitou um horario entre 0 e 23 horas')
# except:
#     print('Voce nao digitou a hora corretamente')


# 3 exercicio

nome = input('Escreva seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é medio')
elif len(nome) > 6:
    print('Seu nome é grande')
