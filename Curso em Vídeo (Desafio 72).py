

numeros_por_extenso = ('zero','Um','Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  numero_escolhido = int(input("Digite um número: "))
  if 0 <= numero_escolhido <= 20:
    print(f"Voçê digitou o número {numeros_por_extenso[numero_escolhido]}")
  else:
    print("Número fora da faixa de 0 a 20. Tente novamente.", end=' ')
