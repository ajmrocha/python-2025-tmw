
soma = 0
qtde_entradas = 4

for i in range(qtde_entradas):
    altura = float(input("Digite a altura: "))
    soma += altura
    
print("A média das alturas é: ", round(soma/qtde_entradas, 2))