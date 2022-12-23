print('*' * 6, '\033[35mPESO MAIOR e MENOR\033[m', '*' * 6)
print('')
ma = 0  # maior
me = 0  # menor
for ps in range(1, 6):  # ps = pessoas
    pe = float(input('Peso da \033[35m{}ª\033[m pessoa(Kg): '.format(ps)))  # pe = de peso
    if ps == 1:  # A primeira pessoa terá o maior e menor peso.
        ma = pe
        me = pe
    else:
        if pe > ma: # Se peso for maior que o maior digitado então se torna o maior
            ma = pe
        if pe < me: # Se peso recebe o menor então menor recebe peso.
            me = pe
print('O \033[36mMAIOR\033[m peso foi de \033[36m{}\033[m Kg:'.format(ma))
print('O \033[32mMENOR\033[m peso foi de \033[32m{}\033[m Kg:'.format(me))

