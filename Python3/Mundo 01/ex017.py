#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


'''oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hi = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente:'))
hi = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hi))