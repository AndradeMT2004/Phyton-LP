import os
os.system("cls")


lista_pedidos = []
cardapio = {
1: ("Picanha", 25.00),
2: ("Lasanha", 20.00),
3: ("Strogonoff", 18.00),
4: ("Bife acebolado", 15.00),
5: ("Pão com ovo", 5.00)
}


while True:
    print("\n--- Cardapio ---")
    for codigo, (prato, preco) in cardapio.items():
        print(f"{codigo} - {prato} R$ {preco:.2f}")
    escolha = int(input("\nDigite o codigo do prato (ou 0 para encerrar): "))

    if escolha == 0:
        break

    match escolha:
        case 1 | 2 | 3 | 4 | 5 :
            lista_pedidos.append(cardapio[escolha])
            print(f"> {cardapio[escolha][0]} adiciona!")
        case _:
            print("Opção invalida")
print("\n--- Pedido final ---")
total = 0
for prato, preco in lista_pedidos:
    print(f"{prato} - R$ {preco:.2f}")
    total += preco
print(f"\nTotal da conta: R$ {total:.2f}")