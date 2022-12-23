print('+'*6, '\033[34mJOGO JOKEMPÔ\033[m', '+'*6)
print('')
op = str(input('Vamos jogar jokempô, digite sua opção: ')).strip().upper()
from random import randint
from time import sleep
comp = randint(1,3)
print('\033[33mJO...\033[m', end='') # end='' para manter os 3 prints na mesma linha.
sleep(1)
print('\033[33mKEM...\033[m', end='')
sleep(1)
print('\033[33mPÔ.\033[m')
sleep(1)
# Variáveis da PEDRA e 1:
if (comp == 1) and (op == 'PEDRA'):
    print('Também pensei em \033[36mPEDRA\033[m, ninguém venceu!')
elif (comp == 1) and (op == 'TESOURA'):
    print('Pensei em \033[36mPEDRA\033[m, \033[31mVENCI!\033[m')
elif (comp == 1) and (op == 'PAPEL'):
    print('\033[34mPARABÉNS\033[m, pensei \033[36mPEDRA\033[m, você \033[34mVENCEU!\033[m')
# Variáveis do PAPEL e 2:
elif (comp == 2) and (op == 'PAPEL'):
    print('Também pensei em \033[36mPAPEL\033[m, ninguém venceu!')
elif (comp == 2) and (op == 'PEDRA'):
    print('Pensei em \033[36mPAPEL\033[m, \033[31mVENCI!\033[m')
elif (comp == 2) and (op == 'TESOURA'):
    print('\033[34mPARABÉNS\033[m, pensei \033[36mPAPEL\033[m, você \033[34mVENCEU!\033[m')
# Variáveis da TESOURA e 3:
elif (comp == 3) and (op == 'TESOURA'):
    print('Também pensei em \033[36mTESOURA\033[m, ninguém venceu!')
elif (comp == 3) and (op == 'PAPEL'):
    print('Pensei em \033[36mTESOURA\033[m, \033[31mVENCI!\033[m')
elif (comp == 3) and (op == 'PEDRA'):
    print('\033[34mPARABÉNS\033[m, pensei \033[36mTESOURA\033[m, você \033[34mVENCEU!\033[m')
else:
    print('\033[31mOPÇÃO INVÁLIDA,\033[m digite uma opção entre, \033[33mPEDRA, PAPEL e TESOURA.\033[m')

























