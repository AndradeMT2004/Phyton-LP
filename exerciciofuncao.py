import os
os.system("cls")

#função com passagem de parâmetros.

def saudacao(nome, idade, altura, peso):
    print(f"Olá, {nome}! Bem-vindo(a) ao nosso site.")
    print(f"Sua idade é {idade} anos")
    print(f"Sua altura é {altura}m")
    print(f"Seu peso é {peso}kg")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura(cm): "))
peso = float(input("Digite seu peso(kg): "))
saudacao(nome, idade, altura, peso)