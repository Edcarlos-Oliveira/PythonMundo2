print('+'*6, '\033[34mCÁUCULO IMC\033[m', '+'*6)
print('')
p = float(input('Digite seu peso:(kg) '))
a = float(input('Digite sua altura:(m) '))
ind = p / (a ** 2)

if ind < 18.5:
    print('Seu IMC de \033[33m{:.1f}, CUIDADO,\033[m você está \033[33mABAIXO DO PESO\033[m.'.format(ind))
elif (ind >= 18.5) and (ind <= 25):
    print('Parabéns, seu IMC de \033[36m{:.1f},\033[m você está no peso \033[36mIDEAL\033[m.'.format(ind))
elif (ind > 25) and (ind <= 30):
    print('Seu IMC de \033[35m{:.1f}, ALERTA,\033[m você está \033[35mSOBREPESO\033[m.'.format(ind))
elif (ind > 30) and (ind <= 40):
    print('Seu IMC de \033[32m{:.1f}, CUIDADOS MÉDICOS,\033[m você está \033[32mOBESO\033[m.'.format(ind))
else:
    print('Seu IMC de \033[31m{:.1f}, ATENÇÃO MÁXIMA,\033[m você está com \033[31mOBESIDADE MÓRBIDA\033[m.'.format(ind))



