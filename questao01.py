trabalho = float(input("digite a nota do trab. de laboratório: "))
avaliação = float(input("digite a nota da av. semestral: "))
exame = float(input("digite a nota do exame final: "))

mediapond = ((trabalho * 2) + (avaliação * 3) + (exame * 5)) / 10

if mediapond < 5:
    print("conceito e")
else:
    if mediapond < 6:
        print("conceito d")
    else:
        if mediapond < 7:
            print("conceito c")
        else:
            if mediapond < 8:
                print("conceito b")
            else:
                print("conceito a"                   
