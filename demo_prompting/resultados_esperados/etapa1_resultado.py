"""
Etapa 1 - Resultado esperado de um prompt VAGO.

Prompt usado no Copilot Chat: "analisa esse CSV"

Este e o tipo de codigo que a IA gera quando o prompt e vago:
- Generico, sem contexto do dominio
- Sem formatacao de valores monetarios
- Sem funcoes (tudo no main)
- Sem tratamento de erros
- Sem docstrings
"""

import csv

with open("dados/extrato_conta.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f"Total de registros: {len(data)}")
print(f"Colunas: {list(data[0].keys())}")

for row in data:
    print(row)
