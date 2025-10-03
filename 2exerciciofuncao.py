import os
os.system("cls")

def par_ou_impar(num):
    if num % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"
    print(f"{num} é um numero {resultado}")

num = int(input("Digite o numero: "))

par_ou_impar(num)