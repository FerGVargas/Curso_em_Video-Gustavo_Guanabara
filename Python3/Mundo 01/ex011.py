#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura
print('Sua parede tem dimensão de {:.1f}x{:.2f} e sua área de {}m.'.format(largura, altura, (area)))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
