"""
Etapa 2 - Resultado esperado de um prompt BEM FEITO.

Prompt usado no Copilot Chat:
"Leia o arquivo dados/extrato_conta.csv que contem um extrato bancario pessoal.
Calcule o total de gastos (debitos) e receitas (creditos).
Agrupe os gastos por categoria e mostre o total e percentual de cada.
Identifique a categoria com maior gasto.
Gere um relatorio formatado no terminal.
Use Python com o modulo csv."

Resultado: codigo funcional, organizado, mas sem funcoes nem docstrings.
"""

import csv
import os

arquivo = os.path.join(os.path.dirname(__file__), "..", "dados", "extrato_conta.csv")

with open(arquivo, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    transacoes = list(reader)

total_debitos = 0
total_creditos = 0
gastos_por_categoria = {}

for t in transacoes:
    valor = float(t["valor"])
    if t["tipo"] == "debito":
        total_debitos += valor
        cat = t["categoria"]
        if cat in gastos_por_categoria:
            gastos_por_categoria[cat] += valor
        else:
            gastos_por_categoria[cat] = valor
    else:
        total_creditos += valor

print("=" * 50)
print("     RELATORIO DE EXTRATO - MARCO 2025")
print("=" * 50)
print(f"\nTotal de receitas: R$ {total_creditos:,.2f}")
print(f"Total de gastos:   R$ {total_debitos:,.2f}")
print(f"Saldo do mes:      R$ {total_creditos - total_debitos:,.2f}")

print("\n" + "-" * 50)
print("  GASTOS POR CATEGORIA")
print("-" * 50)

categorias_ordenadas = sorted(gastos_por_categoria.items(),
                               key=lambda x: x[1], reverse=True)

for cat, valor in categorias_ordenadas:
    percentual = (valor / total_debitos) * 100
    print(f"  {cat:<15} R$ {valor:>8,.2f}  ({percentual:.1f}%)")

maior_cat = categorias_ordenadas[0]
print(f"\nMaior gasto: {maior_cat[0]} (R$ {maior_cat[1]:,.2f})")
print("=" * 50)
