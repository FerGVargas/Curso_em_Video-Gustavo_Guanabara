# Usando FOR para contagem de números, quando sabe o limite
'''for c in range(1, 10):
    print(c)
print('Fim')'''

# Usando WHILE para contagem de números, quando nao sei o limite
'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

# Usando FOR para perguntas, com limite

'''for n in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

# Usando WHILE para perguntas, com limite informado pelo ususario

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

# Usando WHILE para perguntas com limite informado pelo ususario

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
print('Fim')'''

#Digitando números com analise par e impar

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares  e {} números ímares!'.format(par, impar))