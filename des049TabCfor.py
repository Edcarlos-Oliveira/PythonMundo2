print('*'*6, '\033[35mTABUADA COM FOR\033[m', '*'*6)
print('')
t = int(input('Qual o número quer saber a tabuada? '))
s = 0
for c in range(1,11):
    s = t * c
    print('A tabuada de \033[32m{}\033[m x \033[32m{}\033[m = \033[34m{}\033[m'.format(t, c, s))
# Também pode ser reescrito da seguinte forma:
t2 = int(input('Qual número quer saber a tabuada? '))
for c2 in range(1, 11):
    print('A tabuada de \033[32m{}\033[m x \033[32m{}\033[m = \033[33m{}\033[m'.format(t2, c2, t2*c2))

    
    




