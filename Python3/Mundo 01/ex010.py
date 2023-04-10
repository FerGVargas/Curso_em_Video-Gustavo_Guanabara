#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Cosidere US$ 1,00 = R$3,27

dinheiro = float(input('Quanto dinheiro você tem carteira? '))
conversao = dinheiro / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, conversao))