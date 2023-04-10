# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é MENOR
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = b
if c > a and c > b:
    maior = c
print('O MAIOR valor digitado foi {}'.format(maior))
print('O MENOR valor digitado foi {}'.format(menor))