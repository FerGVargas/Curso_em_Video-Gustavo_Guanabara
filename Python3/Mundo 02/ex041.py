#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 9 a 14 anos: INFANTIL
#Até 14 a 19 anos: JÚNIOR
#Até 19 a 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
from datetime import date
nascimento = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade < 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


