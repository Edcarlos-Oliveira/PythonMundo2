print('*'*6, '\033[35mJOGO PAR ou IMPAR\033[m', '*'*6)
print('=-' * 15)
print('VAMOS JOGAR \033[33mPAR OU IMPAR?\033[m')
print('=-' * 15)
from random import randint
s = 0
vit = 0 # Contador das vitórias.
while True:
    v = int(input('Digite um valor: '))
    if v > 10:
        print('\033[31mOPÇÃO INVÁLIDA\033[m, escolha entre \033[32m1 e 10\033[m.')
        break
    c = randint(1, 10)
    s = v + c
    j = ' '
    while j not in 'PI': # Enquanto não for digitado 'P ou I' o programa não avança.
        j = str(input('Qual sua opção, \033[31m[P/I]\033[m? ')).strip().upper()[:1]
    print(f'Você jogou \033[32m{v}\033[m e o computador \033[31m{c}\033[m. Total de \033[36m{s}.', end='')
    print(' DEU PAR' if s % 2 == 0 else ' DEU IMPAR') # Para mostrar se foi par ou impar.
    if j == 'P':
        if s % 2 == 0:
            print('Parabéns! \033[36mVOCÊ VENCEU.\033[m')
            vit += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    elif j == 'I':
        if s % 2 == 1:
            print('Parabéns! \033[36mVOCÊ VENCEU.\033[m')
            vit += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    print('Vamos jogar novamente...')
print(f'\033[31mGAME OVER!\033[m, Você venceu \033[36m{vit}\033[m, vezes.')



















