# Faça um algoritmos que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
produto = float(input('Qual é o preço do produto? R$'))
novo = produto - (produto * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto,novo))