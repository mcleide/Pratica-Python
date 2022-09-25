print("primeira data")
dia1 = int(input("digite o dia (1 a 31): "))
mes1 = int(input("digite o mês (1 a 12): "))
ano1 = int(input("digite o ano: "))

print("segunda data")
dia2 = int(input("digite o dia (1 a 31): "))
mes2 = int(input("digite o mês (1 a 12): "))
ano2 = int(input("digite o ano: "))

#Comparativo de Anos
if ano1 > ano2:
        print(f"a maior data é {dia1}/{mes1}/{ano1}")
elif ano2 > ano1:
        print(f"a maior data é {dia2}/{mes2}/{ano2}")

#Comparativo de Meses
if mes1 > mes2:
    if ano1 > ano2:
        print(f"a maior data é {dia1}/{mes1}/{ano1}")
    elif ano2 > ano1:
        print(f"a maior data é {dia2}/{mes2}/{ano2}")

elif mes2 > mes1:
    if ano1 > ano2:
        print(f"a maior data é {dia1}/{mes1}/{ano1}")
    elif ano2 > ano1:
        print(f"a maior data é {dia2}/{mes2}/{ano2}")

#Comparativo de dias
if dia1> dia2:
    if ano1 > ano2:
        print(f"a maior data é {dia1}/{mes1}/{ano1}")
    elif ano2 > ano1:    
        print(f"a maior data é {dia1}/{mes1}/{ano2}")

elif dia2 > dia1:
    if ano1 > ano2:
        print(f"a maior data é {dia2}/{mes1}/{ano1}")
        
    elif ano2 > ano1:
        print(f"a maior data é {dia2}/{mes1}/{ano1}")