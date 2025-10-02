import os
os.system("cls")

valores = []

for i in range(5):
    numero=int(input(f"Digite o {i+1}° numero: "))
    valores.append(numero)
    if numero < 0:
        numero == 0

for i in range(5):
    print(f"\nNumeros informados: {valores[i]}")