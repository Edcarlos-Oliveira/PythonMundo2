print('.'*6, '\033[32mUTILIZANDO WHILE\033[m', '.'*6)
print('')
# Exemplo com 'for' contando de 1 até 9, IDEAL QUANDO SABEMOS O LIMITE:
print('Resultado utilizando FOR:')
for c in range(1,10):
    print('\033[33m{}\033[m'.format(c), end=' ')
print('Fim...')
print('ESTRUTURA COM WHILE:')
# Exemplo com 'while', contando de 1 até 9, IDEAL QUANDO NÃO SABEMOS O LIMITE:
c2 = 1
print('Resultado utilizando WHILE:')
while c2 < 10:
    print('\033[36m{}\033[m'.format(c2), end=' ')
    c2 += 1
print('Fim...')
# Exemplo com 'while' com interrupção, nesse caso '0' finaliza(condição de parada).:
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim...')
r = 'S'
print('INTERROMPE O SISTEMA COM S ou N')
while r == 'S':
    n2 = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim...')
print('NOVO EXEMPLO COM WHILE')
n3 = 1
par = 0
imp = 0
while n3 != 0:
    n3 = int(input('Digite um valor: '))
    if n3 != 0: # Dessa forma não considera o '0' como digitado.
        if n3 % 2 == 0: # Para achar os pares
            par += 1
        else:
            imp += 1
print('Você digitou \033[36m{}\033[m números PARES e \033[31m{}\033[m números ÍMPARES!'.format(par, imp))















