from operator import index


valores = []
maior = 0
menor = 0

for c in range(3):
    valores.append(int(input(f"Digite um número para a posição {c}: ")))
    if c == 0:
        maior = menor = valores[c]
    else: 
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print("==" * 25)  
print(f"Você digitou os números: {valores}")
print(f"O menor valor é: {menor} nas posições:")

for i,v in enumerate(valores):
    if v == menor:
        print(f"{i}...",end='')
print(f"\nO maior valor é: {maior} nas posições:")

for i,v in enumerate(valores):
    if v == maior:
        print(f"{i}...",end='')

# Olá, como estão
    
    
