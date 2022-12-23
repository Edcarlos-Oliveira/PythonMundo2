print('*' * 6, '\033[35mSOMA ÍMPARES MULTÍPLUS DE 3\033[m', '*' * 6)
print('')
s = 0 # Para acumular a soma do 'if'.
c = 0 # Para acumular o contador
for imp in range(1, 501):
    if (imp % 2 == 1) and (imp % 3 == 0):
        c += 1 # Sempre que for usado o contador soma + 1.
        s += imp
print('A soma dos \033[36m{}\033[m números ímpares multíplos de 3 são: \033[36m{}\033[m '.format(c,s))
print('')
# Também pode ser reescrito da seguinte forma:
s1 = 0 # para acumular a soma do 'if'.
c1 = 0
for imp2 in range(1, 501, 2): # Conta de 1 a 501 de 2 em 2.
    if imp2 % 3 == 0:
        c1 += 1
        s1 += imp2
print('A soma dos \033[33m{}\033[m números ímpares multíplos de 3 são: \033[33m{}\033[m '.format(c1,s1))











