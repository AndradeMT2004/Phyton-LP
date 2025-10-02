import os
os.system("cls")

numeros = []
num_positivo = []
num_negativo = []

for i in range(5):
    num = int(input(f"Digite o {i+1} numero: "))
    if num < 0:
        num_negativo.append(num)
    else:
        num_positivo.append(num)
        soma = sum(num_positivo)

    numeros.append(num)
print(f"Soma dos numeros positivos: {soma}")
print(f"Numeros Negativos: {len(num_negativo)}")
