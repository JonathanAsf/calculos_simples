print("Descubra o seu salário líquido")
salario_bruto = float(input("Digite o seu salário bruto: R$")) 
desconto_IR = salario_bruto* 0.11
print(f"O desconto do IR sobre o salario bruto é de: R${desconto_IR}")
desconto_INSS = salario_bruto*0.08
print(f"O desconto do INSS sobre o salario bruto é de: R${desconto_INSS}")
print("Você contribui para o sindicato? ")
print("Digite 1 para SIM")
print("Digite 2 para NÃO")
sindicato = int(input(""))
if sindicato == 1:
    desconto_sindicato = salario_bruto*0.05
    print(f"O desconto sindical sobre o salario bruto é de: R${desconto_sindicato}")
    descontos = (desconto_INSS + desconto_IR + desconto_sindicato)
else:
    descontos = (desconto_INSS + desconto_IR)

print("O salário líquido é de: R${}".format(salario_bruto-descontos))
