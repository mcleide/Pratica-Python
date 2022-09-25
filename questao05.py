print("°Digite três números em ordem crescente e outro aleatório :)")
n1 = int(input(f"digite um primeiro número: "))
n2 = int(input(f"digite um segundo número: "))
n3 = int(input(f"digite um terceiro número: "))
n4 = int(input(f"digite um quarto número diferente dos outros três: "))

if n4 > n3:
    print(f"a ordem decrescente dos números é: {n1}, {n2}, {n3} e {n4}")
if n4 > n2 and n3 > n4:
    print(f"a ordem decrescente dos números é: {n3}, {n4}, {n2} e {n1}")
if n4 > n1 and n2 > n4:
    print(f"a ordem decrescente dos números é: {n4}, {n2}, {n3} e {n1}")
if n4 > n1:
    print(f"a ordem crescente dos números é: {n3}, {n2}, {n1} e {n4}")
