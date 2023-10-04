print("Cálculo de IMC")
print("O IMC serve para identificar se o seu peso é o ideal de acordo com sua altura")
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em : "))
imc =  peso/(altura*altura) 

if imc <= 18.5:
    print("Você está ABAIXO do seu peso ideal")
elif imc >= 18.6 and imc <=24.9:
    print("Parabéns! Você está no seu peso ideal!")
elif imc >= 25 and imc <= 29.9:
    print("Você está levemente acima do peso")
elif imc >= 30 and imc <= 34.9:
    print("Você está OBESIDADE. É aconselhável a procura de um nutricionista!")
elif imc >= 35 and imc <= 39.9:
    print("Você está COM OBESIDADE SEVERA. Procure um médico")
elif imc >= 40:
    print("Você está com OBESIDADE MÓRBIDA. Procure um médico URGENTEMENTE")
else:
    print("Erro inesperado")
print(f"O seu IMC é: {imc}")
