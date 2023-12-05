from random import randint
numero = (randint(1,1000),randint(1,1000),randint(1,1000),randint(1,1000),randint(1,1000))
print("Os valores sorteados foram:")

for c in numero:
    print(c, end= ' ')
print(f"\nO maior valor desta tupla é: {max(numero)}")
print(f"O menor valor desta tupla é: {min(numero)}")

