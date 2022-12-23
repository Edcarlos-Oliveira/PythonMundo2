print('*' * 6, '\033[35mPALÍNDROMO\033[m', '*' * 6)
print('')
fr = str(input('Digite uma frase: ')).strip().upper()
sp = fr.split()  # 'sp'= separa todas as palavras digitadas usando 'split'.
j = ''.join(sp)  # 'j' juntar todas as palavras separadas por 'split', utilizando '.join'.
i = ''  # 'i' variável do inverso das palavras digitadas.
# 'len' para pegar a última letra de 'j',
# -1(para tirar uma letra pela contagem do Python de 1 a menos,
# -1 vai até a letra antes da primeira por ser (0).
# -1 vai voltando uma letra.
for l in range(len(j) - 1, -1, -1): # 'l' de letra.
    i += j[l]
print('O inverso de {} é {}'.format(j, i)) # Mostra a frase junta e a invertida.
if i == j: # Se o inverso é igual ao junto.
    print('Temos um \033[36mPALÍNDROMO!\033[m')
else:
    print('A frase digitado \033[31mNÃO É UM PALÍNDROMO!\033[m')
print('')
# Utilizando a forma SIMPLIFICADA:
print('A MANEIRA SIMPLIFICADA')
fr2 = str(input('Digite uma frase: ')).strip().upper()
sp2 = fr2.split()
j2 = ''.join(sp2)
i2 = j2[::-1] # Utilizando o fatiamento das letras.
print('O inverso de {} é {}'.format(j2, i2))
if i == j:
    print('Temos um \033[34mPALÍNDROMO!\033[m')
else:
    print('A frase digitado \033[33mNÃO É UM PALÍNDROMO!\033[m')








