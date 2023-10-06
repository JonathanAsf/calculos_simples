print("Apresentacao dos valores declarados de forma decrescente")
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceironúmero: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(numero_1)
    if numero_2 > numero_3:
        print(numero_2)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_2)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(numero_2)
    if numero_1 > numero_3:
        print(numero_1)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_1)
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(numero_3)
    if numero_1 > numero_2:
        print(numero_1)
        print(numero_2)
    else:
        print(numero_2)
        print(numero_1)
else:
    print("Os números são iguais")
