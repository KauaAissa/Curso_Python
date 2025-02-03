def mul(*args):
    resultado = 1
    for quantidade in args:
        resultado *= quantidade
    return resultado

multiplicacao = mul(10,2,3,4,5,1)
print(multiplicacao)
print(10*2*3*4*5)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(3))
print(par_impar(15))