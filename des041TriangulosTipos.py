print('+'*6, '\033[34mTIPOS DE TRIÂNGULOS\033[m', '+'*6)
print('')
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input("Digite o valor do segundo lado: "))
l3 = float(input('Digite o valor do segundo lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores digitados \033[36mFORMA\033[m um: \033[36mTRIÂNGULO.\033[m')
    if l1 == l2 == l3: # Necessário manter a indentação para não dar erro.
        print('O triângulo é: \033[36mEQUILÁTERO.\033[m')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é: \033[36mESCALENO.\033[m')
    else: # Faz parte do segundo 'if'
        print('O triângulo é: \033[36mISÓSCELES.\033[m')
else:
    print('Os valores digitados \033[31mNÃO FORMA\033[m um TRIÂNGULO.')










