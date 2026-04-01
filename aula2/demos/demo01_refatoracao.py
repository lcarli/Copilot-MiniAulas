"""
=============================================================================
  DEMO 01 — Refatoração de Código com GitHub Copilot
  Aula 2: Desenvolvimento Assistido por IA
=============================================================================

  OBJETIVO:
    Mostrar como o Copilot transforma código "espaguete" em código limpo.
    O instrutor apresenta a versão original (comentada) e depois a versão
    refatorada que o Copilot ajudou a criar.

  COMO USAR NA AULA:
    1. Mostre a "Versão Original" — código confuso, sem funções, variáveis ruins
    2. Peça ao Copilot: "Refatore este código seguindo boas práticas"
    3. Compare com a "Versão Refatorada" que já está implementada abaixo
=============================================================================
"""

import csv
import os
import sys
from collections import defaultdict

# Garante saída UTF-8 no terminal Windows
sys.stdout.reconfigure(encoding='utf-8')

# ═══════════════════════════════════════════════════════════════════════════
# ❌ VERSÃO ORIGINAL — "Código Espaguete" (NÃO EXECUTE — apenas para exibir)
# ═══════════════════════════════════════════════════════════════════════════
#
# O instrutor deve descomentar este bloco para mostrar o "antes".
# Depois, selecione o bloco e peça ao Copilot: "Refatore este código."
#
# --- INÍCIO DO CÓDIGO ESPAGUETE ---
#
# import csv
#
# f = open("aula2/dados/transacoes_janeiro.csv")
# r = csv.reader(f)
# h = next(r)
# d = []
# for row in r:
#     d.append(row)
# f.close()
#
# x = 0
# y = 0
# t = {}
# for i in d:
#     v = float(i[5])
#     if i[3] == "debito":
#         x = x + v
#         y = y + 1
#     cat = i[4]
#     if cat in t:
#         t[cat] = t[cat] + v
#     else:
#         t[cat] = v
#
# print("total debitos: " + str(x))
# print("qtd: " + str(y))
# print("media: " + str(x/y))
# print("---")
# for k in t:
#     print(k + ": " + str(t[k]))
#
# # Problemas deste código:
# # - Variáveis com nomes sem sentido (x, y, d, t, k, v, i, h, r, f)
# # - Nenhuma função — tudo em um bloco só
# # - Nenhum tratamento de erro (e se o arquivo não existir?)
# # - Lógica misturada com prints
# # - Não fecha arquivo corretamente (sem with)
# # - Divisão pode dar erro se y for 0
# # - Valores hardcoded, sem reutilização
#
# --- FIM DO CÓDIGO ESPAGUETE ---


# ═══════════════════════════════════════════════════════════════════════════
# ✅ VERSÃO REFATORADA — Código limpo gerado com auxílio do Copilot
# ═══════════════════════════════════════════════════════════════════════════


def carregar_transacoes(caminho_csv: str) -> list[dict]:
    """
    Carrega transações de um arquivo CSV e retorna uma lista de dicionários.

    Args:
        caminho_csv: Caminho completo para o arquivo CSV.

    Returns:
        Lista de dicionários onde cada item representa uma transação.

    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
    """
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")

    transacoes = []
    with open(caminho_csv, encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            # Converte o valor para float já na leitura
            linha['valor'] = float(linha['valor'])
            transacoes.append(linha)

    return transacoes


def filtrar_por_tipo(transacoes: list[dict], tipo: str) -> list[dict]:
    """
    Filtra transações por tipo (débito ou crédito).

    Args:
        transacoes: Lista de transações.
        tipo: Tipo desejado ('debito' ou 'credito').

    Returns:
        Lista filtrada de transações.
    """
    return [t for t in transacoes if t['tipo'] == tipo]


def calcular_total(transacoes: list[dict]) -> float:
    """Calcula o valor total de uma lista de transações."""
    return sum(t['valor'] for t in transacoes)


def calcular_media(transacoes: list[dict]) -> float:
    """Calcula a média dos valores das transações, retornando 0 se a lista estiver vazia."""
    if not transacoes:
        return 0.0
    return calcular_total(transacoes) / len(transacoes)


def agrupar_por_categoria(transacoes: list[dict]) -> dict[str, float]:
    """
    Agrupa transações por categoria e soma os valores.

    Returns:
        Dicionário {categoria: valor_total}.
    """
    totais = defaultdict(float)
    for transacao in transacoes:
        totais[transacao['categoria']] += transacao['valor']
    return dict(totais)


def exibir_relatorio(total: float, quantidade: int, media: float,
                     totais_por_categoria: dict[str, float]) -> None:
    """Exibe o relatório formatado no terminal."""
    print("\n" + "=" * 60)
    print("  📊 RELATÓRIO DE TRANSAÇÕES — JANEIRO 2025")
    print("=" * 60)

    print(f"\n  💳 Total de débitos:    R$ {total:>10,.2f}")
    print(f"  📋 Quantidade:          {quantidade:>10d}")
    print(f"  📈 Média por transação: R$ {media:>10,.2f}")

    print("\n  " + "-" * 40)
    print("  📂 Gastos por Categoria:")
    print("  " + "-" * 40)

    # Ordena categorias por valor (maior primeiro)
    categorias_ordenadas = sorted(
        totais_por_categoria.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for categoria, valor in categorias_ordenadas:
        print(f"    {categoria:<20s} R$ {valor:>10,.2f}")

    print("\n" + "=" * 60)


def main():
    """Função principal que orquestra a execução do script."""
    # Caminho relativo ao diretório do script
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(diretorio_base, '..', 'dados', 'transacoes_janeiro.csv')

    try:
        # 1. Carregar dados
        transacoes = carregar_transacoes(caminho_csv)
        print(f"\n  ✅ {len(transacoes)} transações carregadas com sucesso!")

        # 2. Filtrar débitos
        debitos = filtrar_por_tipo(transacoes, 'debito')

        # 3. Calcular estatísticas
        total_debitos = calcular_total(debitos)
        media_debitos = calcular_media(debitos)

        # 4. Agrupar por categoria
        totais_categoria = agrupar_por_categoria(debitos)

        # 5. Exibir relatório
        exibir_relatorio(total_debitos, len(debitos), media_debitos, totais_categoria)

    except FileNotFoundError as erro:
        print(f"\n  ❌ Erro: {erro}")
    except Exception as erro:
        print(f"\n  ❌ Erro inesperado: {erro}")


# ═══════════════════════════════════════════════════════════════════════════
# COMPARAÇÃO RÁPIDA PARA O INSTRUTOR:
#
#   ANTES (Espaguete)              →  DEPOIS (Refatorado)
#   ─────────────────────────         ────────────────────────
#   Variáveis: x, y, d, t, k      →  total_debitos, media_debitos, etc.
#   Sem funções                    →  6 funções com responsabilidade única
#   Sem docstrings                 →  Docstrings em todas as funções
#   Sem tratamento de erro         →  try/except com mensagens claras
#   open() sem with                →  with open() para fechar arquivo
#   print() misturado com lógica   →  Separação: cálculo vs exibição
#   Divisão sem verificar zero     →  Verificação de lista vazia
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    main()
