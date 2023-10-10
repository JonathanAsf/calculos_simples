nome = input("Digite o seu nome: ")
email =input("Digite o seu email: ")
if nome and email:
    if "@"in email:
        confere_ponto = (email.find("") - 1)
        if "."in email[:confere_ponto]:
            print("Cadastro concluído")
        else:
            print("Email sem ponto")
    else:
        print("Digite um email válido")
else:
    print("Digite o nome e o email corretamente")