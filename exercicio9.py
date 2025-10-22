import os
import time

os.system("cls")


def limpar_tela():
    time.sleep(3)
    os.system("cls")
def calcular_imc(peso, altura):
    return peso / (altura * altura)
def classificacao(imc):
    if imc <= 18.5:
        resultado = "Abaixo do peso"
        recomendacao = "Consulte um Nutricionista para orientação"
    elif imc <= 24.9:
        resultado = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis!"
    elif imc <= 29.9:
        resultado = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e atividade fisica"
    elif imc <= 34.9:
        resultado = "Obesidade grau 1"
        recomendacao = "Procure orientação de um profissional de saúde"
    elif imc <= 39.9:
        resultado = "Obesidade grau 2"
        recomendacao = "Consulte o médico para avaliação e orientação"
    else:
        resultado = "Obesidade grau 3"
        recomendacao = "Busque assistência médica imediatamente"
    return resultado, recomendacao
def main():
    limpar_tela()
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    resultado, recomendacao = classificacao(imc)

    limpar_tela()
    print(f"Seu IMC é {imc:.2f} sua classificação é {resultado} \n{recomendacao} ")
main()