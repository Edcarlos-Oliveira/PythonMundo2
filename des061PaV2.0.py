print('.'*6, '\033[32mPROGRESSÃO ARITIMÉTICA\033[m', '.'*6)
print(' '*9, '\033[33mGerador de PA\033[m')
print('-=-' * 12)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p # Recebe o primeiro número digitado
c = 1
while c <= 10:
    print('\033[36m{}\033[m ¬ '.format(t),end='')
    t += r # A posição do termo e contador deve ser nessa ordem.
    c += 1
print('\033[31mFim...\033[m')












