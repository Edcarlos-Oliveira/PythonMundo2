print('*' * 6, '\033[35mNOME e PREÇO\033[m', '*' * 6)
print('-' * 25)
print(' ' * 2, '\033[33mLOJAS SUPER BARATÃO\033[m')
print('-' * 25)
s = 0
pm = 0  # Produto maior que R$1.000,00
mp = 0 # Menor preço
nmp = '' # Nome do menor preço
c = 0 # Para achar o nome e menor preço digitado pelo usuário.
while True:
    no = str(input('Nome do Produto: ')).strip().upper()
    p = float(input('Preço:R$ '))
    c += 1 # para contar os valores dos produtos.
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[:1]
    print('>' * 25)
    s += p
    if p > 1000:
        pm += 1
    if c == 1:
        mp = p
        nmp = no
    if p < mp: # Pode ser simplificado 'if c == 1 or p < mp'.
        mp = p
        nmp = no
    if op == 'N':
        break
print('-' * 11, 'FIM PROGRAMA', '-' * 11) # Poderia ser reescrito 'print('{:-^40}'.format('FIM DO PROGRAMA'))'
print(f'O total da compra foi:\033[36mR${s:.2f}\033[m')
print(f'Temos \033[36m{pm}\033[m produtos custando mais de R$1000.00')
print(f'O produto mais barato foi \033[36m{nmp}\033[m que custa R$ \033[36m{mp:.2f}\033[m')







