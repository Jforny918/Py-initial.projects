print ('='*30)
print ('{:^30}'.format ('BANCO FORNY'))
print ('='*30)
valor = int (input ('Informe o valor que deseja sacar o dinheiro: R$'))
total = valor 
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1 
    else:
        if totced > 0:
            print (f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print ('-'*30)
print ('Volte Sempre ao Banco Forny!')