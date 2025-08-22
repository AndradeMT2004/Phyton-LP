#Atividade 2
import os
os.system("cls")

nota_1 = float(input("Digite sua Nota de Matematica: "))

nota_2 = float(input("Digite sua Nota de Portugues: "))

nota_3 = float(input("Digite sua Nota de Geografia: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Media Final: {media:.2f}")

if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Resultado: {resultado}")