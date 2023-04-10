# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
v = int(input('Digite um valor: '))
d = v * 2
t = v * 3
r = v ** (1/2)
print('O dobro de {} é {}.'.format(v, d))
print('O triplo de {} é {}.'.format(v, t))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(v, r))

# RESULTADO GUANABARA

print('O triplo de {} é {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(v, (v*3), v, (v**(1/2))))