def crial_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = crial_multiplicador(2)
triplicar = crial_multiplicador(3)
quadruplicar = crial_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))