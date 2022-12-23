print('+'*6, '\033[34mALISTAMENTO MILITAR\033[m','+'*6)
print('')
nas = int(input('Digite sua data de nascimento: '))
from datetime import date
at = date.today().year - nas # Ano alistamento.
tf = 17 - at # Tempo que falta.
af = nas + at + tf # Ano do alistamento.
tp = at - 18 # Tempo que passou.
ap = nas + at - tp  # Ano que passou.
if at <= 17:
    print('Ainda \033[4;32mnão é a hora\033[m do seu alistamento militar, falta: \033[32m{}\033[m anos.'.format(tf))
    print('O ano do alistamento será: \033[32m{}\033[m'.format(af))
elif at == 18:
    print('\033[4;34mChegou a hora\033[m do seu alistamento militar.')
else:
    print('\033[4;31mPerdeu o prazo\033[m do seu alistamento militar em: \033[31m{}\033[m anos.'.format(tp))
    print('O ano que deveria ter se alistado é: \033[31m{}\033[m'.format(ap))












