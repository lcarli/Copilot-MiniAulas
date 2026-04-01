# ============================================================
# Demo 03 - Relatório de transações bancárias
# ============================================================
# Nesta demo vamos cruzar os dados de clientes e transações
# para gerar um relatório completo no terminal.
#
# Vamos praticar:
#   - Ler múltiplos CSVs
#   - Agrupar e somar valores
#   - Formatar saída de relatório profissional
# ============================================================

import csv
import os
from collections import defaultdict
from datetime import datetime


def carregar_csv(caminho: str) -> list:
    """Lê um arquivo CSV e retorna uma lista de dicionários."""
    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def calcular_totais(transacoes: list) -> dict:
    """Calcula o total de débitos e créditos."""
    total_debitos = sum(
        float(t["valor"]) for t in transacoes if t["tipo"] == "debito"
    )
    total_creditos = sum(
        float(t["valor"]) for t in transacoes if t["tipo"] == "credito"
    )
    return {
        "debitos": round(total_debitos, 2),
        "creditos": round(total_creditos, 2),
        "saldo": round(total_creditos - total_debitos, 2),
    }


def agrupar_por_categoria(transacoes: list) -> dict:
    """Agrupa transações por categoria e soma os valores."""
    categorias = defaultdict(float)
    for t in transacoes:
        categorias[t["categoria"]] += float(t["valor"])
    # Arredonda os valores
    return {cat: round(val, 2) for cat, val in categorias.items()}


def encontrar_maior_transacao(transacoes: list) -> dict:
    """Retorna a transação de maior valor."""
    return max(transacoes, key=lambda t: float(t["valor"]))


def buscar_nome_cliente(clientes: list, id_cliente: str) -> str:
    """Busca o nome do cliente pelo id."""
    for c in clientes:
        if c["id_cliente"] == id_cliente:
            return c["nome"]
    return "Desconhecido"


# ============================================================
# Bloco principal — Geração do relatório
# ============================================================
if __name__ == "__main__":
    # Caminhos relativos ao arquivo
    pasta_dados = os.path.join(os.path.dirname(__file__), "..", "dados")
    caminho_clientes = os.path.join(pasta_dados, "clientes.csv")
    caminho_transacoes = os.path.join(pasta_dados, "transacoes.csv")

    # Carregar dados
    clientes = carregar_csv(caminho_clientes)
    transacoes = carregar_csv(caminho_transacoes)

    # Calcular métricas
    totais = calcular_totais(transacoes)
    categorias = agrupar_por_categoria(transacoes)
    maior = encontrar_maior_transacao(transacoes)
    nome_maior = buscar_nome_cliente(clientes, maior["id_cliente"])

    # Top 5 categorias por valor total
    top5 = sorted(categorias.items(), key=lambda x: x[1], reverse=True)[:5]

    # ---- Impressão do relatório ----
    data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M")
    largura = 55

    print("=" * largura)
    print("  RELATÓRIO DE TRANSAÇÕES BANCÁRIAS".center(largura))
    print(f"  Gerado em: {data_hoje}".center(largura))
    print("=" * largura)

    # Resumo geral
    print("\n📊 RESUMO GERAL")
    print("-" * largura)
    print(f"  Total de transações:  {len(transacoes)}")
    print(f"  Total de débitos:     R$ {totais['debitos']:>12,.2f}")
    print(f"  Total de créditos:    R$ {totais['creditos']:>12,.2f}")
    print(f"  Saldo (créd - déb):   R$ {totais['saldo']:>12,.2f}")

    # Top 5 categorias
    print(f"\n📂 TOP 5 CATEGORIAS POR VALOR")
    print("-" * largura)
    print(f"  {'Categoria':<20} {'Total (R$)':>15}")
    print(f"  {'─' * 20} {'─' * 15}")
    for categoria, valor in top5:
        print(f"  {categoria:<20} {valor:>15,.2f}")

    # Maior transação
    print(f"\n💰 MAIOR TRANSAÇÃO")
    print("-" * largura)
    print(f"  Valor:      R$ {float(maior['valor']):,.2f}")
    print(f"  Tipo:       {maior['tipo']}")
    print(f"  Categoria:  {maior['categoria']}")
    print(f"  Cliente:    {nome_maior}")
    print(f"  Descrição:  {maior['descricao']}")
    print(f"  Data:       {maior['data']}")

    print("\n" + "=" * largura)
    print("  ✅ Relatório gerado com sucesso!".center(largura))
    print("=" * largura)
