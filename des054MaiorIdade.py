print('*'*6, '\033[35mMAIOR e MENOR IDADE\033[m', '*'*6)
print('')
from datetime import date
at = date.today().year
tma = 0 # Total de maiores.
tme = 0 # Total de menores.
for pes in range(1,8):
    nas = int(input('Digite que ano a {}ª pessoa nasceu: '.format(pes)))
    i = at - nas # Idade recebe ano atual menos o ano de nascimento digitado.
    if i >= 21: # Idade escolhida para ser considerado como maior.
        tma += 1
        nas += 1
    else:
        tme += 1
print('Tivemos \033[36m{}\033[m pessoas \033[36mMAIORES\033[m de idade.'.format(tma))
print('Tivemos \033[32m{}\033[m pessoas \033[32mMENORES\033[m de idade.'.format(tme))
























