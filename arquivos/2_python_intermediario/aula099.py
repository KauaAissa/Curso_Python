from sys import path
print(__name__)

import aula099_package.modulo
from aula099_package import modulo
from aula099_package.modulo import *

print(soma_do_modulo(1,2))
print(aula099_package.modulo.soma_do_modulo(1,2))
print(variavel)
print(nova_variavel)