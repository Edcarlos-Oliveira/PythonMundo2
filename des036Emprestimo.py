print('+'*6, '\033[34mEMPRÉSTIMO\033[m', '+'*6)
print('')
v = float(input('Qual o valor do imóvel?R$ '))
s = float(input('Qual o valor do seu salário?R$ '))
a = int(input('Em quantos anos quer pagar? '))
# 'pm' prestação mensal,'lp' limite prestaçao.
pm = v / (a * 12)
lp = s * 30/100

if pm <= lp:
    print('\033[34mPARABÉNS\033[m, seu financiamento foi \033[34mAPROVADO\033[m, durante {:.0f} anos \nO valor mensal será de:\033[34mR${:.2f}\033[m '.format(a, pm))
else:
    print('Lamentamos, a parcela de \033[31m{:.2f},\033[m excede \033[31m30%\033[m do seu sálario e\nSeu financiamento foi \033[31mNEGADO.\033[m'.format(pm))










