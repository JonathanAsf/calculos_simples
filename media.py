print("Bem vindo ao sistema de cálculo de médias")
nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))
nota_4 = int(input("Digite a quarta nota: "))
media = (nota_1 + nota_2 + nota_3 + nota_4)/4
if media <= 6:
    print("O aluno foi reprovado")
elif media >= 7:
    print("O aluno foi aprovado")
else:
    print("Erro inesperado no cálculo da média")
print(f"A média das notas é: {media}")
