print('Aula 15 usando BREAK')

# Nesse exemplo ficaria em loop infinito:
c = 1
while True:
    print(c, '¬ ', end='')
    c += 1
    break # Para o loop infinito não usa esse 'break'.
print('Acabou.')
print('')
# Nesse caso o 'BREAK' interrompe o loop.
c2 = 1
while True:
    print(c2, '¬ ', end='')
    c2 += 1
    break # Para interromper o loop.
print('Acabou.')
print('')
# Usando as 'f strings' em substituição ao '.format':
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')
# A mesma coisa seria assim:
print('O {} tem {} anos.'.format(nome, idade))
print('')
# Nesse exemplo abaixo o break funciona como um fleg interrompendo o loop:
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: # Nesse caso quando o usuário digita '999' aciona o break e para o programa.
        break
    s += n
print(f'A soma vale: {s}')

# Alinhamentos dentro da string ('<' alinha a esquerda, '>' alinha a direita, '^' centraliza):











