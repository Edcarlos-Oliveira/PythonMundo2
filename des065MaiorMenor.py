print('\033[34m=\033[m\033[31m-\033[m' * 14)
print('.'*6, '\033[32mMAIOR e MENOR\033[m', '.'*6)
print('\033[31m=\033[m\033[34m-\033[m' * 14)
op = 'S'
c = m = s = mai = men = 0
while op == 'S':
    n = int(input('Digite um número: '))
    op = str(input('Quer continuar? \033[33m[S/N]\033[m ')).strip().upper()[0] # '0' para considerar só a primeira letra.
    c += 1
    s += n
    m = s / c
    if c == 1:
        mai = men = n
    else:
        if n > mai:
            mai = n
        if n < men:
            men = n
    if op == 'N':
        print('\033[33mFinalizando...\033[m')
        print('Você digitou \033[34m{}\033[m números e a média deles são: \033[36m{}.\033[m'.format(c, m))
        print('O maior valor foi \033[34m{}\033[m e o menor foi \033[36m{}.\033[m'.format(mai, men))















