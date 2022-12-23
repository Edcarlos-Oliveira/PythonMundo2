print('*' * 6, '\033[35mSIMULADOR CAIXA ELETRÔNICO\033[m', '*' * 6)
print('=' * 35)
print(' ' * 10, '\033[33mBANCO HEDDY\033[m', ' ' * 10)
print('=' * 35)
vs = int(input('Qual valor você quer sacar? R$'))
t = vs # Total será o valor digitado pelo usuário.
cdl = 50
totcdl = 0 # Contador das cédulas.
while True:
    if t >= cdl:
        t -= cdl
        totcdl += 1
    else:
        if totcdl > 0: # Para não mostrar as cedulas que não foram usadas.
            print(f'Total de \033[33m{totcdl}\033[m cédulas de \033[36mR${cdl}\033[m')
        if cdl == 50: # quando o valor for igual a 50 a próxima cédulas será 20 e assim sucessivamente.
            cdl = 20
        elif cdl == 20:
            cdl = 10
        elif cdl == 10:
            cdl = 1
        totcdl = 0
        if t == 0:
            break
print('='*30)
print('\033[32mVolte Sempre....\033[m')















