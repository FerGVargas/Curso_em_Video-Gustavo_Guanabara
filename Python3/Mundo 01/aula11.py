#ANSI
#STYLE-0/1/4/7
#TEXT-30/31/32/33/34/35/36/37
#BACK-40/41/42/43/44/45/46/47
print('\033[4;30;43mOlá, mundo!\033[m')
print('\033[1;36Olá, mundo!\033[m')
print('\033[7;30;45mOlá, mundo!\033[m')
print('\033[1;31mOlá, mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
nome = 'Guanabara'

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#Diciorario
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;40m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))



