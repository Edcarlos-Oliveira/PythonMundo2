print('.'*6, '\033[32mTRATANDO VALORES\033[m', '.'*6)
print('')
c = 0
s = 0
n = 0
n = int(input('Digite um número \033[32m[999 para parar]\033[m: ')) # Para eliminar a soma do 'flag'.
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número \033[32m[999 para parar]\033[m: ')) # A posição é importante para o 'while' não considerar o '999'.
    if n == 999:
        print('\033[33mFinalizando...\033[m')
        print('Você digitou \033[34m{}\033[m números e a soma deles é: \033[36m{}\033[m'.format(c, s))















