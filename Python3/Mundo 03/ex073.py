#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoence',
        'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atletico-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoence está na {times.index("Chapecoence")} posição')