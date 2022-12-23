print('+'*6, '\033[34mMÉDIAS\033[m','+'*6)
print('')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m < 5:
    print('Sua média foi \033[31m{}\033[m, você está \033[4;31mREPROVADO.\033[m'.format(m))
elif (m >= 5) and (m < 7):
    print('Sua média foi \033[33m{}\033[m, você está em \033[4;33mRECUPERAÇÃO.\033[m'.format(m))
else:
    print('Parabéns, sua média foi \033[36m{}\033[m, você está \033[4;36mAPROVADO.\033[m'.format(m))





