print('.'*6, '\033[32mDESCOBRINDO O SEXO\033[m', '.'*6)
print('')
s = str(input('Informe seu sexo [M/F]:')).strip().upper()[0] # '0' para pegar só a 1ª letra.
sm = 'M'
sf = 'F'
while s not in 'MF':
    s = str(input('Dados inválidos, por favor, informe seu sexo: ')).strip().upper()[0]
    if sm == s:
        print('Sexo \033[34m{}\033[m registrado com sucesso.'.format(s))
    elif sf == s:
        print('Sexo \033[35m{}\033[m registrado com sucesso.'.format(s))









































