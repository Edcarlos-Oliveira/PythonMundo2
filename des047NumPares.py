print('*'*6, '\033[35mNÚMEROS PARES\033[m', '*'*6)
print('')
for p in range(1,51):
    if p % 2 == 0:
        print('\033[36m{}\033[m'.format(p), end=' ')
print('Acabou.')
print('')
# Também pode ser reescrito da seguinte forma simplificada,
# Nessa forma elimina os laços que seria necessários,
# # Para mostrar todos os números de 1 a 50.
for p2 in range(2, 51, 2):
    print(p2, end=' ')
print('Acabou P2.')












