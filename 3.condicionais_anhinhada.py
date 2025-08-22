#condicionais anhinhada

import os
os.system("cls")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de Idade")
elif idade >= 14:
    print("Adolescente")
else:
    print("Criança")
    
print("Fim.")