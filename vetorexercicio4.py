import os 
os.system("cls")

lista_numero = []
par = 0
impar = 0

num = 6

for i in range(num):
    numero = int(input(f"Digite o {i+1}° numero: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    lista_numero.append(numero)


for numero in lista_numero:
    print(f"Numero: {numero}")
#for i in range(6):
    #print(f"Numeros informados: {lista_numero[i]}")

print(f"\nQuantidade de pares: {par}")
print(f"\nQuantidade de impar: {impar}")
