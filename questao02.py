nota1 = float(input("digite a primeira média: "))
nota2 = float(input("digite a segunda média: "))
nota3 = float(input("digite a terceria média: "))

media = (nota1 + nota2 + nota3) / 3
exame = 6 - media

if media < 3:
    print("reprovado")
elif media >= 3 and media < 6:
    print(f"você precisa de {round(exame,2)} para ser aprovado")
elif media >= 6:
    print("aprovado")

elif media >= 7:
    print("aprovado")