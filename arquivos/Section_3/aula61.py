cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

if digito_1 > 9:
    digito_1 == 0
    
elif digito_1 <= 9:
    print(digito_1)

