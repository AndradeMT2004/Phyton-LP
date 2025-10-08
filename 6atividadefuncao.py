import os
import time

def limpartela():
    time.sleep(2)
    os.system("cls")
    
def metros_para_centimetros(metros):
    return metros * 100
    
    
def mostrar_conversao(metros, centimetros):
    print(f"A conversão de {metros} para centimetros é = {centimetros}cm")

limpartela()    
    
numero_em_metros = float(input("Digite quantos metros quer converter: "))
centimetros = metros_para_centimetros(numero_em_metros)
mostrar_conversao(numero_em_metros, centimetros)