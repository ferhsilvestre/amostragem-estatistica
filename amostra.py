N = int(input('Informe o tamanho da população: '))

Z = 0
while Z == 0:
    print()
    print('1- Nível de confiança de 90%')
    print('2- Nível de confiança de 95%')
    print('3- Nível de confiança de 95,5%')
    print('4- Nível de confiança de 99%\n') 
    Z = int(input('Escolha uma das opções acima para indicar o nível de confiança de sua pesquisa: '))

    if Z == 1:
        Z = 1.65
    elif Z == 2:
        Z = 1.96
    elif Z == 3:
        Z = 2
    elif Z == 4:
        Z = 2.57
    else:
        Z = 0

e = float(input('\nInforme, em porcentagem, o valor do erro amostral: '))
e /= 100

p = input('\nPossui estimativa da verdadeira proporção? (S/N) ').strip().upper()[0]

if p == 'S':
    p = float(input('\nInforme, em porcentagem, a estimativa da verdadeira proporção: '))
    p /= 100
else:
    p = 0.5

n = (N * (Z**2) * p * (1 - p)) / ((e**2) * (N - 1) + (Z**2) * p * (1 - p))

print(f'O tamanho da amostra deve ser de {n:.2f}')