# Com quantidade informada

'''cont = 1
while cont <= 10:
    print(cont, ' - ', end='')
    cont += 1
print('Acabou')
'''

'''n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1'''

#Sem quantidade informada

'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))

# nova forma de formatação para print desde 2017
print(f'A soma vale {s}')
'''
#Conhecimento:
nome = 'Jose'
idade = 33

# mais antigo PYTHON 2
print('O %s tem %d anos.' % (nome, idade))
# antigo PYTHON 3
print('O {} tem {} anos.'.format(nome, idade))
# 2017 PYTHON 3.6+
print(f'O {nome} tem {idade} anos.')'''