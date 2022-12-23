print('.'*6, '\033[32mMENU OPÇÕES\033[m', '.'*6)
print('')
from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''
    \033[36m[1]\033[m SOMAR
    \033[36m[2]\033[m MULTIPLICAR
    \033[36m[3]\033[m MAIOR
    \033[36m[4]\033[m NOVOS NÚMEROS
    \033[31m[5]\033[m SAIR DO PROGRAMA''')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        s = v1 + v2
        print('A soma entre \033[32m{}\033[m + \033[33m{}\033[m é \033[34m{}\033[m.'.format(v1, v2,s))
        print('=-='*10)
    elif op == 2:
        m = v1 * v2
        print('O resultado de \033[32m{}\033[m x \033[33m{}\033[m é \033[34m{}\033[m.'.format(v1, v2, m))
        print('=-=' * 10)
    elif op == 3:
        if v1 > v2:
            mai = v1
        else:
            mai = v2
        print('Entre \033[32m{}\033[m e \033[33m{}\033[m o maior é \033[34m{}\033[m.'.format(v1, v2, mai))
        print('=-=' * 10)
    elif op == 4:
        print('Informe os valores novamente')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif op == 5:
        print('\033[35mFinalizando....\033[m')
        sleep(2)
    else:
        print('\033[31mOpção inválida. Tente novamente\033[m')
        print('=-=' * 10)
print('\033[33mFim do Programa! Volte sempre!\033[m')










































