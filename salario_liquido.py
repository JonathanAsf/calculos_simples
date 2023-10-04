print("Descubra o seu salário líquido")
salario_bruto = float(input("Digite o seu salário bruto: "))
desconto_IR = salario_bruto* 0.11
print(f"O desconto do IR sobre o salario bruto é de: {desconto_IR}")
desconto_INSS = salario_bruto*0.08
print(f"O desconto do INSS sobre o salario bruto é de:{desconto_INSS}")
desconto_sindicato = salario_bruto*0.05
print(f"O desconto sindical sobre o salario bruto é de: {desconto_sindicato}")

descontos = (desconto_INSS + desconto_IR + desconto_sindicato)
print("O salário líquido é de: {}".format(salario_bruto-descontos))
