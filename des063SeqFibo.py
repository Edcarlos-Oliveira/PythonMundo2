print('.'*6, '\033[32mSEQUÊNCIA DE FIBONACCI v1.0\033[m', '.'*6)
print('-'*35)
print('\033[33mSequência de Fibonacci\033[m')
print('-' * 35)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 35)
print('\033[36m{} ¬ {}\033[m'.format(t1, t2),end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' ¬ \033[36m{}\033[m'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' ¬ \033[31mFim...\033[m')








