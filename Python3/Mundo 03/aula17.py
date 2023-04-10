# Não muda item na TUPLA
num = (2, 5, 9, 1)
#num [2] = 3
print(num)

# Mudando item na LISTA
num = [2, 5, 9, 1]
num [2] = 3
print(num)

# Adicionando item na LISTA

num.append(7)
print(num)

# Organizando LISTA

num.sort()
print(num)

# Organizando reverso LISTA

num.sort(reverse=True)
print(num)

# Quantos itens tem na LISTA

print(f'Essa lista tem {len(num)} elementos.')

# Inserir valor na LISTA

num.insert(2,0)
print(num)

# Eliminando  valor da LISTA

print('*'*30)
print(num)
num.pop() # ultimo posição
print(num)
num.pop(2) # 2 posição da lista
print(num)
num.pop(0) #  primeiro posição
print(num)

print('*'*30)
print(num)
num.insert(2,9) #Incluindo valores na lista
num.append(0,2) #Incluindo valores na lista
num.insert(2,0) #Incluindo valores na lista
print(num)
num.remove(2) #Incluindo valores na lista
print(num)
if 4 in num:  #Exclui o valor caso tenha ou informa que nao tem o valor na lista
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista.')

# Repete a lista
a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print((f'Lista B: {b}'))

# Faz uma copia da lista

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print((f'Lista B: {b}'))

