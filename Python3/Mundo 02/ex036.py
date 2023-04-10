#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (12 * anos)
minimo = salario / 30 * 100
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}.'.format(casa, anos, prestação))

