#Cálculo de bônus referente a meta de vendas.
#Se o funcionário alcaçar a meta é pago 10% das vendas totais.
#Se o funcionário alcançar o dobro da meta é pago 15% das vendas totais.
#Se o funcionário não atingir a meta não haverá bônus

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
