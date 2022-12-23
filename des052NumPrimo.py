print('*'*6, '\033[35mNÚMERO PRIMO\033[m', '*'*6)
print('')
n = int(input('Digite um número: '))
t = 0 # Para saber o número de divisíveis.
for c in range(1, n + 1): # 'n + 1' pela contagem do Python de 1 número a menos.
    if n % c == 0: # Verifica os números digitados são divisíveis pelo contador.
        print('\033[33m', end='') # Colore em amarelo todos os que são divisíveis
        t += 1
    else:
        print('\033[31m', end='') # Colore em vermelho os que não são divisíveis.
    print('{}'. format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, t))
if t == 2: # Verifica se o número digitado é PRIMO ou NÃO.
    print('O número é \033[36mPRIMO!\033[m')
else:
    print('O número \033[31mNÃO É PRIMO!\033[m')








