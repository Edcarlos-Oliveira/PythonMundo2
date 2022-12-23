print('.'*6, '\033[32mCÁUCULO FATORIAL\033[m', '.'*6)
print('')
# Maneira tradicional para calcular o fatorial.
n = int(input('Digite um número para \ncalcular seu Fatorial: '))
c = n
f = 1 # Sempre que for necessária multiplicação limpa
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c),  end=' ')
    print('x ' if c > 1 else ' = ', end='') # para excluir o último 'x'.
    f *= c # Forma simplificada de 'f = f * c'
    c -= 1 # A posição do contador é importante, forma simplificada de 'c = c - 1'.
print(f)
print('')
# Maneira prática com Python, importando a biblioteca math.
n2 = int(input('Digite o número para \ncalcular o Fatorial: '))
from math import factorial
f2 = factorial(n2)
print('O fatorial de {} é {}.'.format(n2, f2))

# Calculando fatorial utilizando 'for':
print('')
n3 = int(input('Digite um número para calcular o Fatorial: '))
c3 = n
f3 = 1
for c3 in range(n, 0):
    f3 *= c3
    c -= 1
print(c, f)















