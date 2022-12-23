print('.' * 6, '\033[32mSUPER PA\033[m', '.' * 6)
print(' ' * 5, '\033[33mGerador PA\033[m')
print('-=-' * 7)
p = int(input('Primeiro termo: '))
r = int(input('Razão PA: '))
t = p
c = 1
tot = 0
p2 = 10
while p2 != 0: # Para dar continuidade ao programa, encerra digitando '0'.
    tot += p2 # Inicia a PA com 10 termos.
    while c <= tot:
        print('\033[36m{}\033[m ¬'.format(t), end=' ')
        t += r
        c += 1
    print('\033[33mPAUSE\033[m')
    p2 = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com \033[34m{}\033[m termos mostrado.'.format(tot))
print('\033[31mFim...\033[m')










