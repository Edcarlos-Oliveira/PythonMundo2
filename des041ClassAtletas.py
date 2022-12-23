print('+'*6, '\033[34mCLASSIFICAÇÃO ATLETAS\033[m','+'*6)
print('')
nas = int(input('Qual o seu ano de nascimento? '))
from datetime import date
aa = date.today().year
cat = aa - nas
print('Com \033[32m{}\033[m anos sua CATEGORIA é:'.format(cat))
if cat <= 9:
    print('\033[4;34mMIRIM.\033[m')
elif (cat > 9) and (cat <= 14):
    print('\033[4;34mINFANTIL.\033[m')
elif (cat > 14) and (cat <= 19):
    print('\033[4;34mJUNIOR.\033[m')
elif (cat > 19) and (cat <= 25):
    print('\033[4;34mSÊNIOR.\033[m')
else:
    print('\033[4;36mMASTER.\033[m')

# Poderia ser reescrito só com '(cat <= 14)' desnecessários os '(cat > 9) e assim sucessivamente.






