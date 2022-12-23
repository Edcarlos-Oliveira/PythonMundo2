print('*'*6, '\033[35mCADASTRO PESSOAS\033[m', '*'*6)
mai18 = mu20 = h = 0
while True:
    print('-'*25)
    print('\033[33m   CADASTRE UMA PESSOA\033[m')
    print('-'*25)
    i = int(input('Idade: '))
    s = op = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[:1]
    print('-'*25)
    while op not in 'SN':
        op = str(input('Quer continuar \033[32m[S/N]\033[m? ')).strip().upper()[:1]
    if i > 18:
        mai18 += 1
    if s in 'M':
        h += 1
    if s in 'F' and i < 20:
        mu20 += 1
    if op == 'N':
        break
print('='*6, '\033[31mFIM PROGRAMA\033[m', '='*6)
print(f'Total de pessoas com mais de \033[34m18\033[m anos: \033[36m{mai18}\033[m')
print(f'Ao todo temos \033[36m{h}\033[m homens cadastrados.')
print(f'E temos \033[36m{mu20}\033[m mulheres com menos de \033[34m20\033[m anos.')
















