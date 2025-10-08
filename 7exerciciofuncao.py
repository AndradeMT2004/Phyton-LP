import os
import time

def limpartela():
    time.sleep(2)
    os.system("cls")
    
def infracao(preco):
    if preco >= 100:
        preco_total = preco + (preco * 0.2)
    else:
        preco_total = preco + (preco * 0.1)
    print(f"O valor final do produto é {preco_total}")
    return preco_total

limpartela()

valor_produto = int(input("Digite o preço do produto: "))
preco_total = infracao(valor_produto)