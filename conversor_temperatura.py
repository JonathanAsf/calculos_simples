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
      
