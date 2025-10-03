import os
os.system("cls")

valores = []

for i in range(5):
    numero=int(input(f"Digite o {i+1}° numero: "))
    if numero < 0:
        numero = 0
    valores.append(numero)

for i, numero in enumerate(valores, start=1):
    print(f"{i}° Valor: {numero}")
    
