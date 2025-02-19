def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce não pode dividir um numero por zero')
    return True

def deve_ser_int_ou_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} Deve ser um numero inteiro ou flutuante')
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, 2))