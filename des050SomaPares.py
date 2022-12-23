print('*'*6, '\033[35mSOMA DOS PARES\033[m', '*'*6)
print('')
soma = 0
cont = 0 # Para contar os números digitados pelo usuário.
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} números PARES é: \033[36m{}\033[m'.format(cont, soma))










