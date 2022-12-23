print('+' * 10, '\033[34mJOGO JOKEMPÔ\033[m', '+' * 10)
print('')
print('=' * 34)
print(' ' * 10,'\033[4;33mRegras do Jogo\033[m')
print('=' * 34)
print('Quem marcar \033[31m3\033[m pontos primeiro, vence o jogo.')
from random import randint
from time import sleep
rodada = cont1 = cont2 = 0

while rodada < 3:
    while True:
        comp = randint(1, 3)
        rodada += 1
        print(f'\033[4;35m{rodada}ª Rodada:\033[m')
        op = str(input('Vamos jogar jokempô, digite sua opção: ')).strip().upper()
        print('\033[33mJO...\033[m', end='')  # end='' para manter os 3 prints na mesma linha.
        sleep(1)
        print('\033[33mKEM...\033[m', end='')
        sleep(1)
        print('\033[33mPÔ.\033[m')
        sleep(1)
# Variáveis da PEDRA e 1:
        if (comp == 1) and (op == 'PEDRA'):
            print('Também pensei em \033[36mPEDRA\033[m, ninguém venceu!')
        elif (comp == 1) and (op == 'TESOURA'):
            cont2 += 1
            print('Pensei em \033[36mPEDRA\033[m, \033[31mVENCI!\033[m')
            print('=' * 34)
            print(' ' * 12, '\033[33mPlacar\033[m')
            print('=' * 34)
            print('=-' * 19)
            print(
                f'''
        Rodada {rodada}ª Finalizada!
        Jogador: \033[36m{cont1}\033[m
        Computador: \033[31m{cont2}\033[m''')
            print('=-' * 19)

        elif (comp == 1) and (op == 'PAPEL'):
            cont1 += 1
            print('\033[34mPARABÉNS\033[m, pensei \033[36mPEDRA\033[m, você \033[34mVENCEU!\033[m')
            print('=' * 34)
            print(' ' * 12, '\033[33mPlacar\033[m')
            print('=' * 34)
            print('=-' * 19)
            print(
                f'''
        Rodada {rodada}ª Finalizada!
        Jogador: \033[36m{cont1}\033[m
        Computador \033[31m{cont2}\033[m
        ''')
            print('=-' * 19)

# Variáveis do PAPEL e 2:
        elif (comp == 2) and (op == 'PAPEL'):
            print('Também pensei em \033[36mPAPEL\033[m, ninguém venceu!')
        elif (comp == 2) and (op == 'PEDRA'):
            cont2 += 1
            print('Pensei em \033[36mPAPEL\033[m, \033[31mVENCI!\033[m')
            print('=' * 34)
            print(' ' * 12, '\033[33mPlacar\033[m')
            print('=' * 34)
            print('=-' * 19)
            print(
                f'''
        Rodada {rodada}ª Finalizada!        
        Jogador: \033[36m{cont1}\033[m
        Computador: \033[31m{cont2}\033[m''')
            print('=-' * 19)

        elif (comp == 2) and (op == 'TESOURA'):
            cont1 += 1
            print('\033[34mPARABÉNS\033[m, pensei \033[36mPAPEL\033[m, você \033[34mVENCEU!\033[m')
            print('=' * 34)
            print(' ' * 12, '\033[33mPlacar\033[m')
            print('=' * 34)
            print('=-' * 19)
            print(
                f'''
        Rodada {rodada}ª Finalizada! 
        Jogador: \033[36m{cont1}\033[m
        Computador: \033[31m{cont2}\033[m''')
            print('=-' * 19)

# Variáveis da TESOURA e 3:
        elif (comp == 3) and (op == 'TESOURA'):
            print('Também pensei em \033[36mTESOURA\033[m, ninguém venceu!')
        elif (comp == 3) and (op == 'PAPEL'):
            cont2 += 1
            print('Pensei em \033[36mTESOURA\033[m, \033[31mVENCI!\033[m')
            print('=' * 34)
            print(' ' * 12, '\033[33mPlacar\033[m')
            print('=' * 34)
            print('=-' * 19)
            print(
                f'''
        Rodada {rodada}ª Finalizada! 
        Jogador: \033[36m{cont1}\033[m
        Computador: \033[31m{cont2}\033[m''')
            print('=-' * 19)

        elif (comp == 3) and (op == 'PEDRA'):
            cont1 += 1
            print('\033[34mPARABÉNS\033[m, pensei \033[36mTESOURA\033[m, você \033[34mVENCEU!\033[m')
            print('=' * 34)
            print(' ' * 12, '\033[33mPlacar\033[m')
            print('=' * 34)
            print('=-' * 19)
            print(f'''
            Rodada {rodada}ª Finalizada!             
            Jogador: \033[36m{cont1}\033[m
            Computador: \033[31m{cont2}\033[m''')
            print('=-' * 19)

        else:
            print('\033[31mOPÇÃO INVÁLIDA,\033[m digite uma opção entre, \033[33mPEDRA, PAPEL e TESOURA.\033[m')
            print('Rodada Anulada!')

        if cont1 == 3:
            print('\033[36mJogador Venceu!!\033[m na \033[32m{}ª\033[m rodada.'.format(rodada))
            break
        elif cont2 == 3:
            print('\033[31mComputador Venceu!!\033[m na \033[32m{}ª\033[m rodada'.format(rodada))
            break
print('\033[31mFim de jogo!\033[m, foi um prazer jogar com você.')
