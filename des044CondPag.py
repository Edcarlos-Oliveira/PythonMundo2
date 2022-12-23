print('+'*6, '\033[34mDESCONTO PAGAMENTO\033[m', '+'*6)
print('')
v = float(input('Digite o valor do produto:R$ '))
avdc = v - (v * 10/100) # a vista no dinheiro ou cheque.
avc = v - (v * 5/100) # a vista no cartão.
p2xc = v/2 # parcelado em 2 vezes no cartão.
p3xc = v + (v * 20/100) # parcelado em 3x no cartão.
print('[1] À vista, \033[34mDinheiro ou Cheque\033[m: \033[33m10%\033[m de desconto.')
print('[2] À vista, \033[34mCartão\033[m: \033[33m5%\033[m de desconto.')
print('[3] Em \033[34m2x Cartão\033[m: \033[33mPreço Normal\033[m')
print('[4] Em \033[34m3x ou mais no Cartão\033[m; \033[33m20%\033[m de acréscimo.')
fp = int(input('\033[33mESCOLHA A FORMA DE PAGAMENTO:\033[m'))


if fp == 1:
    print('Você escolheu a opção \033[32m{}\033[m como desconto, o valor ficou em:\033[34mR${:.2f}\033[m'.format(fp,avdc))
elif fp == 2:
    print('Você escolheu a opção \033[32m{}\033[m como desconto, o valor ficou em:\033[34mR${:.2f}\033[m'.format(fp,avc))
elif fp == 3:
    print('Você escolheu a opção \033[32m{}\033[m como desconto, o valor ficou em 2x de:\033[34mR${:.2f}\033[m'.format(fp,p2xc))
elif fp == 4:
    tp = int(input('Quantas Parcelas? '))  # Total de Parcelas para ser executado quando for escolhida a opção 4.
    p = p3xc / tp  # Para calcular o valor de cada parcela conforme a quantidade escolhida pelo usuário.
    print('Você escolheu a opção \033[32m{}\033[m parcelado em \033[32m{}\033[m vezes de:\033[34mR${:.2f}\033[m'.format(fp,tp, p))
else:
    print('Opção: \033[31mINVÁLIDA\033[m, escolha entre 1 e 4.')










