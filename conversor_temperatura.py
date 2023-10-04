print("Bem vindo ao programa de conversão de unidades de temperaturas")
print("Selecione a unidade de media inicial")
print("Digite 1 para converter de GRAUS CELSIUS para GRAUS FAHRENHEIT")
print("Digite 2 para converter de GRAUS FAHRENHEIT para GRAUS CELSIUS")
opcao = int(input(""))

if opcao != 1 and 2:
      print("Opção inválida")
      
temperatura = float(input("Digite a temperatura que deseja converter: "))   
         
if opcao == 1:
    print(f"{temperatura}°C é igual a {temperatura*1.8 + 32}°F") 
else:
  print(f"{temperatura}°F é igual a {(temperatura - 32)/1.8}°C")
