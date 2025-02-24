
soma = 0

qtde_entradas = 4

while qtde_entradas > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    qtde_entradas -= 1
    
print("A média das alturas é: ", round(soma / 4, 2))