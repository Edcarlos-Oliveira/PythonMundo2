print('*'*6, '\033[35mNOME, IDADE e SEXO\033[m', '*'*6)
print('')
si = 0 # Soma da Idade.
mi = 0 # Média das Idades.
mai = 0 # Maior idade.
nv = '' # nome do mais velho.
tm20 = 0 # Total de Mulheres.
for p in range(1,5):
    print('-'*5, '\033[33m{}ª\033[m' ' PESSOA'.format(p), '-'*5)
    n = str(input('NOME: ')).strip().upper()
    i = int(input('IDADE: '))
    s = str(input('SEXO[M/F]: ')).strip().upper()
    si += i # Soma da idade recebe idade, permanece dentro do laço.
# Para achar a maior idade, o sexo e o nome do mais velho.
    if p == 1 and s == 'M': # Pode ser escrito 's in 'Mm' para diferenciar maiúsculas de minúsculas.
        mai = i
        nv = n
    if s == 'M' and i > mai:
        mai = i
        nv = n
    if s == 'F' and i < 20: # para encontrar o número de mulheres com menos de 20 anos.
        tm20 += 1
mi = si / 4 # Média da idade recebe soma da idade dividido por 4 que o número de pessoas, fora do laço.
print('A média de idade do grupo é de \033[36m{}\033[m anos'.format(mi))
print('O homem mais velho tem \033[33m{}\033[m e se chama \033[33m{}\033[m.'.format(mai, nv))
print('O total de \033[35m{}\033[m mulheres com menos de \033[35m20\033[m anos: '.format(tm20))








