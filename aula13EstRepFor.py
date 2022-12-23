print('*'*6,'\033[34mESTRUTURAS DE REPETIÇÃO\033[m', '*'*6)
print('')
# Obs: O Python sempre escreve um número a menos.
for c in range(0,6): # Escreve até 6, 'range' significa intervalo.
    print('Oi') # Para escrever 'oi' por 6 vezes.
print('Fim...') # Não escreve 'fim' por 6 vezes, pois não está indentado, ou seja está fora do laço.
# Nesse caso escreve de '0 até 5 utilizando 'print(c)'.
for c2 in range(0,6):
    print(c2)
print('Fim2...')
# Nesse caso escreve de 6 até 0 'range(0, 6, -1):'.
for c3 in range(0,6,-1):
    print(c3)
print('Fim3...')
# Nesse caso escreve de 0 até 6 de 2 em 2 'range(0, 7, 2):'.
for c4 in range(0,7,2):
    print(c4)
print('Fim4...')
# Nesse caso escreve a contagem conforme o número digitado pelo usuário
# #para ser igual, ou seja sem 1 a menos 'range(0,n+1):
n = int(input('Digite um número: '))
for c5 in range(0, n+1):
    print(c5)
print('Fim5...')
# Nesse caso escreve o 'inicio' o 'fim' e o 'passo ou intervalo', '´range(i, f+1, p':.
i = int(input('Inicio: '))
f = int(input("Fim: "))
p = int(input('Passo ou Intervalo: '))
for c6 in range(i, f+1, p):
    print(c6)
print('Fim6...')
# Nesse caso com o 'for c7 in range(0,3) vai ler os comandos embaixo por 3 vezes:
s = 0 # Para somar os valores digitados.
for c7 in range(0,3):
    n = int(input('Digite um valor: '))
    s += n # Soma todos os valores digitados
print('A soma dos valores digitados é: {}'.format(s))


