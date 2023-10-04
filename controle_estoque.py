# Controle de estoque
# Não há conexão com banco de dados
# O estoque mínimo do produto condiz com sua categoria



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


