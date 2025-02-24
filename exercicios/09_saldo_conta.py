
saldo_total = 0

while True:
    saldo = input('Digite o saldo da conta: ')
    if saldo == '':
        break

    saldo_total += float(saldo)
    
print(f'O saldo total da conta é: {saldo_total}')
    
    