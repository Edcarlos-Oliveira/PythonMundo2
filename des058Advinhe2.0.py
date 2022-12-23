print('.'*6, '\033[32mADVINHE v2.0\033[m', '.'*6)
print('')
from random import randint
from time import sleep
print('Sou seu computador...\nAcabei de pensar em um número entre \033[33m0 e 10\033[m.\nSerá que você consegue adivinhar qual foi?')
comp = randint(0, 10)
cj = 0
jog = 0
while jog != comp:
    jog = int(input('Qual o seu palpite? '))
    cj += 1 # Conta o número de tentativas.
    if jog < comp:
        print('\033[35mVamos ver....\033[m')
        sleep(2)
        print('É \033[34mMAIS\033[m...Tente novamente')
    elif jog > comp:
        print('\033[32mSerá que foi dessa vez....\033[m')
        sleep(2)
        print('É \033[33mMENOS\033[m... Tente novamente')
    else:
        print('\033[34mAgora foi!\033[m')
        print('Acertou com \033[36m{}\033[m tentativas. \033[36mPARABÉNS!\033[m'.format(cj))


















