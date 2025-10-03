import os
os.system("cls")

def tabuada(numero):
    print(f"a Tabuada do {numero}: ")
    for i in range(1,11):
        print(f"{i} x {numero} = {i*numero}")

numero = int(input("Digite um numero: "))
tabuada(numero)