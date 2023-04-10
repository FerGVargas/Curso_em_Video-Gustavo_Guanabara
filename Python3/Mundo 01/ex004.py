# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveia sobre ele.
v = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(v))
print('Só tem espaços?', v.isspace())
print('É um numérico?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('É alfanumético?', v.isalnum())
print('Está em maiuscula?', v.isupper())
print('Está em minuscula?', v.islower())
print('Está capitalizada?', v.istitle())


