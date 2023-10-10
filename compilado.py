#Compilado de todos os cálculos
print("Escreva a opção de cálculo que deseja fazer: ")
print("Digite 1 para AREA QUADRADA")
print("Digite 2 para MEDIA DE NOTAS")
print("Digite 3 para CONVERSOR DE TEMPERATURA")
print("Digite 4 para SALARIO BRUTO")
print("Digite 5 para SALARIO LIQUIDO")
print("Digite 6 para BONIFICAÇÃO")
print("Digite 7 para INDICE DE MASSA CORPORAL (IMC)")
print("Digite 8 para CONTROLE DE ESTOQUE")
escolha = int(input(""))

if escolha > 8 or escolha <= 0:
    print("Opção inválida")
else:
    pass

if escolha == 1:
    print("Descubra a área quadrada")
    altura = float(input("Digite a altura: "))
    base = float(input("Digite a base: "))
    print(f"De acordo com os dados, a área quadrada é: {base*altura}")
    
elif escolha == 2: 
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

elif escolha == 3: 
    print("Bem vindo ao programa de conversão de unidades de temperaturas")

    print("Selecione a unidade de media inicial")

    print("Digite 1 se deseja converter de GRAUS CELSIUS (°C) para outra unidade de medida")
    print("Digite 2 se deseja converter de GRAUS FAHRENHEIT (°F) para outra unidade de medida")
    print("Digite 3 se deseja converter de GRAUS KELVIN (°K) para outra unidade de medida")

    opcao = int(input(""))
    if opcao == 1 or opcao == 2 or opcao == 3:
        temperatura = float(input("Digite a temperatura que deseja converter: "))
        #Celsius
        if opcao == 1 :
            print("Digite 1 se deseja converter para °F")
            print("Digite 2 se deseja converter para °K")
            conversao_1 = (int(input("")))
            if conversao_1 == 1:
                print(f"{temperatura}°C é igual a {temperatura*1.8 + 32}°F") 
            elif conversao_1 == 2:
                print(f"{temperatura}°C é igual a {temperatura + 273}°K") 
            else:
                print("Valor incorreto")  
        #FAHRENHEIT
        if opcao == 2 :
            print("Digite 1 se deseja converter para °C")
            print("Digite 2 se deseja converter para °K")  
            conversao_2 = (int(input("")))
            if conversao_2 == 1:
                print(f"{temperatura}°F é igual a {(temperatura - 32)/1.8}°C")
            elif conversao_2 ==2:
                print(f"{temperatura}°F é igual a {(((temperatura - 32) * 5/9) + 273.15)}°K")
            else: 
                print("Valor incorreto")    
        #KELVIN
        if opcao == 3 :
            print("Digite 1 se deseja converter para °F")
            print("Digite 2 se deseja converter para °K")
            conversao_3 = (int(input("")))
            if conversao_3 == 1:
                print(f"{temperatura}°K é igual a {temperatura - 273.15}°C") 
            elif conversao_3 ==2:
                print(f"{temperatura}°K é igual a {(((temperatura - 273.15)*9/5)+32)}°F") 
            else: 
                print("Valor incorreto")
        else:
            print("Opção inválida")
      
elif escolha == 4:
    print("Descubra quanto é o seu salario bruto com base nas horas trabalhadas mensalmente e o valor da hora")
    ganho_hora = float(input("Digite quanto você ganhar por hora: R$"))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas semanalmente: "))
    print(f"O seu salário é: R$ {(horas_trabalhadas*4)*ganho_hora:.2f}")


elif escolha == 5:
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

    print(f"O salário líquido é de: R${(salario_bruto-descontos)}")
    
elif escolha == 6:
    meta = int(input("Digite o valor da meta de vendas: "))
    vendas_funcionario = int(input("Valor gerado nas vendas do funcionário: "))

    if vendas_funcionario >= meta:
        print("O funcionário tem direito ao bônus!")
        if vendas_funcionario >= (meta*2):  
            print("O bônus do funcionário é de: R$ {} (15% sobre o valor total)".format(vendas_funcionario*0.15))
            print(f"O total a receber é: {(vendas_funcionario*0.15)+vendas_funcionario:.2f}")
        else :
            print("O bônus do funcionário é de: R$ {}  (10% sobre o valor total)".format(vendas_funcionario*0.10))
            print(f"O total a receber é: {( vendas_funcionario*0.10)+vendas_funcionario:.2f}")
    else:
        print("O funcionário não teve bônus, pois suas vendas não alcançam a meta")

elif escolha == 7:
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
    
elif escolha == 8:
    print("Controle de Estoque")
    nome_do_produto = input("Digite o nome do produto: ")
    print("Digite a categoria do produto")
    print("1 - Alimentos")
    print("2 - Bebidas")
    print("3 - Limpeza")
    categoria = int(input(""))

    if categoria == 1 or categoria == 2 or categoria == 3:
        quantidade = int(input("Digite a quantidade do produto presente no estoque: "))
        
        #Alimentos
        if categoria == 1:
            if quantidade < 50:
                print("Estoque baixo, contate a equipe de reposição, temos apenas {} {} e o mínimo esperado é 50".format(quantidade,nome_do_produto))
            else:
                print("Não há problemas de estoques. A quantidade mínima esperada é 50 e temos {}".format(quantidade))
        #Bebidas
        elif categoria == 2:
            if quantidade < 75:
                print("Estoque baixo, contate a equipe de reposição, temos apenas {} {} e o mínimo esperado é 75".format(quantidade, nome_do_produto))
            else:
                print("Não há problemas de estoques. A quantidade mínima esperada é 75 e temos {}".format(quantidade))    

        #Limpeza
        elif categoria == 3:
            if quantidade < 30:
                print("Estoque baixo, contate a equipe de reposição, temos apenas {} {} e o mínimo esperado é 30".format(quantidade, nome_do_produto))
            else:
                print("Não há problemas de estoques. A quantidade mínima esperada é 30 e temos {}".format(quantidade))    
        else:
            print("Erro inesperado. Tente novamente")
    else:
        print("Opção inválida")


