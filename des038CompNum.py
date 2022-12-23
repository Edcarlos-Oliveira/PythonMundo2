print('+'*6, '\033[34mCOMPARANDO NÚMEROS\033[m','+'*6)
print('')
n1 = int(input("Digite o primeiro número: "))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O \033[33mPrimeiro Número\033[m é o \033[34mMAIOR.\033[m')
elif n1 == n2:
    print('\033[33mNão existe\033[m número maior, os dois são \033[34miguais.\033[m')
else:
    print('O \033[33mSegundo Número\033[m é o \033[34mMAIOR.\033[m')





