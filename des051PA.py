print('*'*6,'\033[35mPROGRESSÃO ARITIMÉTICA\033[m', '*'*6)
print(''*6, '10 TERMOS DE UMA PA', ''*6)
print('*'*30)
pt = int(input('Digite o primeiro Termo: '))
r = int(input('Digite a razão: '))
d = pt + (11-1) * r # Fórmula para achar o enésimo termo de uma PA 'd' = décimo termo.
for t in range(pt, d, r):
    print('\033[36m{}\033[m'.format(t), end=' ¬ ')
print('Acabou.')


    





