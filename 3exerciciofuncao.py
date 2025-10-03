import os
os.system("cls")

def positivo_ou_negativo(num):
    if num < 0:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
    print(f"O Numero {num} é {resultado}")
num = int(input("Digite o numero: "))
positivo_ou_negativo(num)