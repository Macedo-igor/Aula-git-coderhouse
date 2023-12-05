while True:
    numero = int(input("Deseja ver a tabuada de qual valor? "))
    print("=-=" * 20)
    if numero < 1:
        print("Número inválido!")
        numero = int(input("Digite outro número: "))
        
    for c in range (1,11):
        print(f"{numero} x {c} = {numero * c}")
    print("=-=" * 20)
            