
# numero = int(input("Digite um número: "))
# max_numero = int(input("Digite o número máximo: "))

# for i in range(1, max_numero + 1):
#     print(f"{numero} x {i} = {numero * i}")

numero_inicial = int(input("Digite um número: "))
divisivel_por = int(input("Digite o número para saber quais são divisíveis: "))

for i in range(1, divisivel_por + 1):
    if i % numero_inicial == 0:
        print(i)