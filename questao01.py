note1 = float(input("digite a nota do trab. de laboratório: "))
note2 = float(input("digite a nota da av. semestral: "))
note3 = float(input("digite a nota do exame final: "))

media = ((note1 * 2) + (note2 * 3) + (note3 * 5)) / 10

if media < 5:
    print("conceito e")
else:
    if media < 6:
        print("conceito d")
    else:
        if media < 7:
            print("conceito c")
        else:
            if media < 8:
                print("conceito b")
            else:
                print("conceito a")