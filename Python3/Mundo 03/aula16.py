# TUPLAS (tupla) [lista] {Dicionario} - são imutaveis
lanche = 'Hamburguer'
lanche = ('Hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-2:])
print(len(lanche))
print(sorted((lanche)))

#for comida in lanche:
#    print(f'Eu vou comer {comida}')
#print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

# Com numeros

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(c.count(5))
print(d.index(8))
print(d.index(5,1))

# tuplas com tipos de dados diferente

pessoa = ('Fernanda', 34, 'F', 80.2)
#del(pessoa) # apaga a tupla da memoria
print(pessoa)