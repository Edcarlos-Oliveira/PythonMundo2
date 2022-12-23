print('*'*6, '\033[35mSOMANDO NÚMEROS E CONTANDO\033[m', '*'*6)
print('')
c = s = 0
while True:
    n = int(input('Digite um número [\033[31m999\033[m para parar]: '))
    if n == 999: # Encerra quando digitado '999'
        break
    s += n # Soma os valores digitados, a indentação é importante.
    c += 1 # Conta os valores digitados, a indentação é importante.
print(f'A soma dos \033[32m{c}\033[m valores digitados foi: \033[36m{s}\033[m.')






