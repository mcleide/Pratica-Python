media1 = float(input("digite a primeira média: "))
media2 = float(input("digite a segunda média: "))
media3 = float(input("digite a terceria média: "))

mediaA = (media1 + media2 + media3) / 3
exame = 6 - mediaA

if mediaA < 3:
       print("reprovado")
    elif mediaA >= 3 and mediaA < 6:
         print(f"você precisa de {round(exame,2)} para ser aprovado")
        elif mediaA >= 6:
             print("aprovado")
            elif mediaA >= 7:
                print("aprovado")
