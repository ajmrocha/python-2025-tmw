texto = """
Escolha a sua água para comprar
(1) Água Mineral Natural
(2) Água Mineral com Gás
"""

opcao = input(texto)

valor_item = 0

if opcao == "1":
    valor_item = 1.5
     
elif opcao == "2":
    valor_item = 2.5
    
if valor_item == 0:
    print("Entre com a porra da opção certa")
    
else:
    
    qtde = input("Quantas unidades você deseja? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
        
    print("O valor total é: R$", valor_total)
    