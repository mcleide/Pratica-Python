print("menu de opções:")
print("    1. Somar dois números")
print("    2. Raíz quadrada de um número")
op = int(input("digite a opção desejada: "))

if op == 1:
    n1 = int(input("digite um número: "))
    n2 = int(input("digite outro número: "))

    result = n1 + n2
    print(f"o resultado da sua soma foi: {result} ")

import math
if op == 2:
    num = int(input("digite um número: "))

    print(f"a raíz quadrada do seu número é: {math.sqrt(num)}")