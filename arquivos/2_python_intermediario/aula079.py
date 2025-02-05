letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Você acertou a letra')
        break
    print(letras)