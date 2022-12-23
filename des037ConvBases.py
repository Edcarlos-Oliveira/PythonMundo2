print('+'*6, '\033[34mCONVERSOR DE BASES NÚMERICAS\033[m', '+'*6)
print('')
n = int(input('Digite um número qualquer: '))
# Poderia usar ''' no inicio e na última opção a ser escolhida assim eliminava os 3 'print'.
print('\033[4;32mEscolha uma das opções abaixo:\033[m')
print('[1] para \033[33mBINÁRIO.\033[m')
print('[2] para \033[33mOCTAL.\033[m')
print('[3] para \033[33mHEXADECIMAL.\033[m')
es = int(input('Qual a sua escolha para conversão? '))
op = es
# Utiliza '[2:]' para eliminar a posição 1 e 2 dos números convertidos.
if op == 1:
    print('O valor \033[35m{}\033[m convertido em Binário é: \033[36m{}\033[m'.format(n, bin(n)[2:])) # O Python tem o conversor.
elif op == 2:
    print('O valor \033[35m{}\033[m convertido em OCTAL é: \033[36m{}\033[m.'.format(n, oct(n)[2:]))
elif op == 3:
    print('O valor \033[35m{}\033[m convertido em HEXADECIMAL é: \033[35m{}\033[m.'.format(n, hex(n)[2:]))
else:
    print('Opção \033[31mINVÁLIDA\033[m, escolha um número entre \033[33m1, 2 e 3.\033[m')









