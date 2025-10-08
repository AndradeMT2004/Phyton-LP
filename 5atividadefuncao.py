import os
import time

def limpar_tela():
    time.sleep(3)
    os.system("cls")

def somar(n1, n2):
   return n1 + n2

def subtrair(n1, n2):
    return n1 - n2
  

def dividir(n1, n2):
    return n1 / n2 if n2 != 0 else "Divisão por zero."

def multiplicar(n1, n2):
    return n1 * n2

def mostrar_resultado(posicao1, posicao2, posicao3, posicao4):
    print(f"O resultado da soma é {posicao1}")
    print(f"O resultado da Subtração é {posicao2}")
    print(f"O resultado da divisão é {posicao3:.2f}")
    print(f"O resultado da multiplicação é {posicao4}")
    

limpar_tela()    

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))

soma = somar(primeiro_numero, segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)
produto = multiplicar(primeiro_numero, segundo_numero)

mostrar_resultado(soma,subtracao,divisao,produto)