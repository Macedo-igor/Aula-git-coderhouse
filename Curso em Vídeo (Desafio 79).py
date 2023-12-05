lista = []

while True:
    numeros = int(input("Digite um valor: "))
    
    if numeros in lista:
        print("Valor duplicado! Tente novamente!")
    else:
        lista.append(numeros)
        print("Valor adicionado com sucesso!")
        
    opção = input("Quer continuar? [S/N]:  ")
    if opção.upper() == 'N':
        break
    
print('=-' * 30)               
print(f"Você digitou os números {sorted(lista)}")

Olaaaaaa