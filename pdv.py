compras = []

while True:
    valor_compra = float(input("Valor da compra (R$): "))

    if valor_compra == 0:
        break

    if valor_compra < 0:
        print("Valor negativo! Digite novamente.\n")
        continue

    idade = int(input("Idade do cliente: "))

    if idade < 0:
        print("Idade negativa! Digite novamente.\n")
        continue

    valor_final = valor_compra

    if idade >= 65:
        valor_final = valor_final * 0.80

    if valor_final > 100:
        valor_final = valor_final * 0.90

    desconto = valor_compra - valor_final
    compras.append([valor_compra, desconto, valor_final])

    print(f"Valor final: R$ {valor_final:.2f}\n")

total_bruto = 0
total_descontos = 0
total_final = 0

for compra in compras:
    total_bruto += compra[0]
    total_descontos += compra[1]
    total_final += compra[2]

print("\n--- RESUMO DO DIA ---")
print(f"Quantidade de compras: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
