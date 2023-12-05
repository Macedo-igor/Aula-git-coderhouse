times_brasileiros = (
    'Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Corinthians',
    'Fluminense', 'Botafogo', 'Vasco da Gama', 'Grêmio', 'Internacional',
    'Atlético Mineiro', 'Cruzeiro', 'América Mineiro', 'Bahia', 'Vitória',
    'Sport', 'Santa Cruz', 'Náutico', 'Fortaleza', 'Ceará')

print(times_brasileiros[:5])
print(times_brasileiros[-4:])
print(sorted(times_brasileiros))
time = input("Qual time deseja saber a colocação na tabela? ")
print(f"O time {time} está na {times_brasileiros.index(time)}º colocação")