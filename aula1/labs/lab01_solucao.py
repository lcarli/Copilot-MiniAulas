"""
Lab 1 — Solução de Referência
Análise de Transações Bancárias

Este script lê o arquivo transacoes.csv e gera um resumo completo
com totais de débito/crédito, gastos por categoria, cliente mais ativo,
média por categoria e a transação de maior valor.
"""

import csv
import os

# Caminho do arquivo CSV relativo ao diretório deste script
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_script, '..', 'dados', 'transacoes.csv')

# Ler todas as transações do CSV
transacoes = []
with open(caminho_csv, encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        linha['valor'] = float(linha['valor'])
        transacoes.append(linha)

# Calcular totais de débito e crédito
total_debito = sum(t['valor'] for t in transacoes if t['tipo'] == 'debito')
total_credito = sum(t['valor'] for t in transacoes if t['tipo'] == 'credito')

# Agrupar gastos por categoria (apenas débitos)
gastos_por_categoria = {}
contagem_por_categoria = {}
for t in transacoes:
    if t['tipo'] == 'debito':
        cat = t['categoria']
        gastos_por_categoria[cat] = gastos_por_categoria.get(cat, 0) + t['valor']
        contagem_por_categoria[cat] = contagem_por_categoria.get(cat, 0) + 1

# Identificar a categoria com maior gasto total
categoria_maior_gasto = max(gastos_por_categoria, key=gastos_por_categoria.get)

# Contar transações por cliente para encontrar o mais ativo
transacoes_por_cliente = {}
for t in transacoes:
    cliente = t['id_cliente']
    transacoes_por_cliente[cliente] = transacoes_por_cliente.get(cliente, 0) + 1

cliente_mais_ativo = max(transacoes_por_cliente, key=transacoes_por_cliente.get)

# Desafio extra: média de gastos por categoria
media_por_categoria = {
    cat: gastos_por_categoria[cat] / contagem_por_categoria[cat]
    for cat in gastos_por_categoria
}

# Desafio extra: transação de maior valor (valor absoluto)
transacao_maior = max(transacoes, key=lambda t: t['valor'])

# Imprimir resumo formatado
print("=" * 48)
print("       RESUMO DE TRANSAÇÕES BANCÁRIAS")
print("=" * 48)

print(f"\n💰 Total de DÉBITOS:  R$ {total_debito:,.2f}")
print(f"💳 Total de CRÉDITOS: R$ {total_credito:,.2f}")

print("\n📊 Gastos por categoria (débitos):")
for cat in sorted(gastos_por_categoria):
    total = gastos_por_categoria[cat]
    print(f"   {cat:<15} R$ {total:>10,.2f}")

print(f"\n🏆 Categoria com maior gasto: {categoria_maior_gasto} "
      f"(R$ {gastos_por_categoria[categoria_maior_gasto]:,.2f})")

print(f"\n👤 Cliente com mais transações: ID {cliente_mais_ativo} "
      f"({transacoes_por_cliente[cliente_mais_ativo]} transações)")

print("\n" + "-" * 48)
print("       DESAFIOS EXTRAS")
print("-" * 48)

print("\n📈 Média de gastos por categoria:")
for cat in sorted(media_por_categoria):
    media = media_por_categoria[cat]
    qtd = contagem_por_categoria[cat]
    print(f"   {cat:<15} R$ {media:>10,.2f}  ({qtd} transações)")

print(f"\n💎 Transação de maior valor:")
print(f"   ID Transação: {transacao_maior['id_transacao']}")
print(f"   Cliente:      ID {transacao_maior['id_cliente']}")
print(f"   Data:         {transacao_maior['data']}")
print(f"   Tipo:         {transacao_maior['tipo']}")
print(f"   Categoria:    {transacao_maior['categoria']}")
print(f"   Valor:        R$ {transacao_maior['valor']:,.2f}")
print(f"   Descrição:    {transacao_maior['descricao']}")

print("\n" + "=" * 48)
