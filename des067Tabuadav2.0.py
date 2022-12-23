print('*' * 6, '\033[35mTABUADAv2.0\033[m', '*' * 6)
print('')

while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if t < 0:
        break
    for c in range(1, 11):
        print(f'\033[32m{t} x {c}\033[m = \033[36m{t*c}\033[m')
    print('-'*35)
print('Programa \033[31mTABUADA ENCERRADO!\033[m')








