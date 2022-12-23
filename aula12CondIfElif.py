print('=' * 6, '\033[34mCONDIÇÕES ANINHADAS\033[m', '=' * 6)
print('')
# 'strip' para eliminar os espaços e 'upper' para eliminar o tipo de escrita.
# Estrutura condicional Simples:
nome = str(input('Qual o seu nome? ')).strip().upper()
if nome == 'EDCARLOS':
    print('\033[36mQue nome de cantor!\033[m')
print('Tenha um bom dia, \033[34m{}!\033[m'.format(nome))
print('')
# Estrutura Condicional Composta:
nome2 = str(input('Digite outro nome? ')).strip().upper()
if nome2 == 'MARIA':
    print('\033[31mQue nome bem escolhido!\033[m')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[33m{}!\033[m'.format(nome2))
print('')
# Estrutura Aninhadas:
nome3 = str(input('Digite mais um nome: ')).strip().upper()
if nome3 == 'ANTONIA':
    print('\033[32mQue nome lindo, ''xonei''!\033[m')
# Pode ser usado quantos 'elif' for necessário.
elif nome3 == 'JOÃO' or nome3 == 'PEDRO' or nome3 == 'FÁBIO':
    print('\033[35mSeu nome é muito popular no Brasil\033[m')
# Outro uso do 'elif in' para selecionar algum dos nomes entre aspas.
elif nome3 in 'JOSÉ GILBERTO JAIRO CARLOS':
    print('Que nomes zuados.')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, \033[35m{}!\033[m'.format(nome3))











