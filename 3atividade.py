#Atividade 3
import os
os.system("cls")

a = int(input("Digite A: "))
b = int(input("Digite B: "))

soma = a + b
media = soma / 2
multiplicacao = a * b

#if a > b:
#    maior = a
#    menor = b
#else:
#    maior = b
#    menor = a 
maior = max(a , b)
menor = min(a , b)

print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Produto: {multiplicacao}")
print(f"Maior Numero: {maior}")
print(f"Menor Numero: {menor}")
