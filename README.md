# Desafio Nível 1 — PDV com Descontos

## O que o código faz

O programa simula um ponto de venda (PDV) simples. Ele recebe o valor da compra e a idade do cliente, calcula os descontos quando o cliente tem direito e mostra o preço final. Também permite registrar várias compras e, quando encerrado, apresenta um resumo do dia.

## Como ele faz

1. Pede o valor da compra. Se for `0`, encerra as compras.
2. Se o valor for negativo, avisa e pede uma nova compra.
3. Pede a idade. Se for negativa, avisa e começa novamente.
4. Se a idade for maior ou igual a 65 anos, aplica 20% de desconto.
5. Se o valor **depois do desconto por idade** for maior que R$ 100,00, aplica mais 10% sobre ele.
6. Mostra o valor final com duas casas decimais e guarda o valor original, o desconto e o valor final em uma lista usando `.append()`.
7. Quando o usuário digita `0`, percorre a lista e mostra quantas compras foram feitas, o total bruto, os descontos e o total final.

## Como rodar

Abra o terminal na pasta `nivel_1` e execute:

```bash
python pdv.py
```

Digite o valor da compra e a idade do cliente. Para terminar e ver o resumo, digite `0` no valor da compra.

## Casos de teste

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|-----------:|------:|---------------:|---------------:|---------------------:|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

**Atenção:** no caso 5, `125 × 0.8 = 100`. Como o valor ficou igual a 100, e não maior, o desconto extra de 10% não é aplicado. No caso 10, a idade 64 não dá desconto por idade.
