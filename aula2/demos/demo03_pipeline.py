"""
=============================================================================
  DEMO 03 — Pipeline Completo de Dados Bancários
  Aula 2: Desenvolvimento Assistido por IA
=============================================================================

  OBJETIVO:
    Demonstração principal da Aula 2 — um pipeline de análise de dados
    que lê 3 meses de transações, cruza com dados de clientes e gera
    um relatório executivo completo.

  COMO USAR NA AULA:
    1. Mostre a estrutura do pipeline (funções separadas por responsabilidade)
    2. Execute e comente cada seção do relatório
    3. Destaque como o Copilot ajudou a criar funções claras e documentadas
=============================================================================
"""

import csv
import os
import sys
from collections import defaultdict

# Garante saída UTF-8 no terminal Windows
sys.stdout.reconfigure(encoding='utf-8')


# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DE CAMINHOS
# ═══════════════════════════════════════════════════════════════════════════

DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))

ARQUIVOS_TRANSACOES = {
    'Janeiro': os.path.join(DIRETORIO_BASE, '..', 'dados', 'transacoes_janeiro.csv'),
    'Fevereiro': os.path.join(DIRETORIO_BASE, '..', 'dados', 'transacoes_fevereiro.csv'),
    'Março': os.path.join(DIRETORIO_BASE, '..', 'dados', 'transacoes_marco.csv'),
}

ARQUIVO_CLIENTES = os.path.join(DIRETORIO_BASE, '..', '..', 'aula1', 'dados', 'clientes.csv')


# ═══════════════════════════════════════════════════════════════════════════
# ETAPA 1 — CARREGAMENTO DE DADOS
# ═══════════════════════════════════════════════════════════════════════════


def carregar_transacoes(caminho: str) -> list[dict]:
    """
    Carrega transações de um arquivo CSV.

    Cada transação é retornada como um dicionário com o campo 'valor'
    já convertido para float.

    Args:
        caminho: Caminho completo para o arquivo CSV.

    Returns:
        Lista de dicionários representando as transações.

    Raises:
        FileNotFoundError: Se o arquivo não existir no caminho indicado.
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    transacoes = []
    with open(caminho, encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            linha['valor'] = float(linha['valor'])
            transacoes.append(linha)

    return transacoes


def carregar_clientes(caminho: str) -> dict[str, dict]:
    """
    Carrega dados de clientes e retorna um dicionário indexado por id_cliente.

    Args:
        caminho: Caminho completo para o arquivo clientes.csv.

    Returns:
        Dicionário {id_cliente: dados_do_cliente}.
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo de clientes não encontrado: {caminho}")

    clientes = {}
    with open(caminho, encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            linha['saldo_atual'] = float(linha['saldo_atual'])
            clientes[linha['id_cliente']] = linha

    return clientes


# ═══════════════════════════════════════════════════════════════════════════
# ETAPA 2 — CONSOLIDAÇÃO
# ═══════════════════════════════════════════════════════════════════════════


def consolidar_transacoes(lista_de_listas: list[list[dict]]) -> list[dict]:
    """
    Junta múltiplas listas de transações em uma única lista.

    Args:
        lista_de_listas: Lista contendo listas de transações (uma por mês).

    Returns:
        Lista única com todas as transações consolidadas.
    """
    consolidadas = []
    for lista in lista_de_listas:
        consolidadas.extend(lista)
    return consolidadas


# ═══════════════════════════════════════════════════════════════════════════
# ETAPA 3 — CLASSIFICAÇÃO POR CATEGORIA
# ═══════════════════════════════════════════════════════════════════════════


def classificar_por_categoria(transacoes: list[dict]) -> dict[str, list[dict]]:
    """
    Agrupa transações por categoria.

    Args:
        transacoes: Lista de transações.

    Returns:
        Dicionário {categoria: [lista_de_transacoes]}.
    """
    por_categoria = defaultdict(list)
    for transacao in transacoes:
        por_categoria[transacao['categoria']].append(transacao)
    return dict(por_categoria)


# ═══════════════════════════════════════════════════════════════════════════
# ETAPA 4 — ESTATÍSTICAS POR CLIENTE
# ═══════════════════════════════════════════════════════════════════════════


def calcular_estatisticas_cliente(transacoes: list[dict],
                                  clientes: dict[str, dict]) -> dict[str, dict]:
    """
    Calcula estatísticas de transações por cliente.

    Para cada cliente que aparece nas transações, calcula:
    - nome: nome do cliente
    - total_gasto: soma dos débitos
    - total_recebido: soma dos créditos
    - num_transacoes: quantidade total de transações
    - categorias: set das categorias utilizadas

    Args:
        transacoes: Lista consolidada de transações.
        clientes: Dicionário de clientes indexado por id_cliente.

    Returns:
        Dicionário {id_cliente: estatísticas}.
    """
    stats = defaultdict(lambda: {
        'nome': 'Desconhecido',
        'total_gasto': 0.0,
        'total_recebido': 0.0,
        'num_transacoes': 0,
        'categorias': set()
    })

    for transacao in transacoes:
        id_cliente = transacao['id_cliente']

        # Recupera nome do cliente, se disponível
        if id_cliente in clientes:
            stats[id_cliente]['nome'] = clientes[id_cliente]['nome']

        # Acumula valores por tipo
        if transacao['tipo'] == 'debito':
            stats[id_cliente]['total_gasto'] += transacao['valor']
        else:
            stats[id_cliente]['total_recebido'] += transacao['valor']

        stats[id_cliente]['num_transacoes'] += 1
        stats[id_cliente]['categorias'].add(transacao['categoria'])

    return dict(stats)


# ═══════════════════════════════════════════════════════════════════════════
# ETAPA 5 — RESUMO EXECUTIVO
# ═══════════════════════════════════════════════════════════════════════════


def gerar_resumo_executivo(stats: dict[str, dict],
                           total_transacoes: int,
                           meses_info: dict[str, int]) -> str:
    """
    Gera um resumo executivo em texto corrido.

    Args:
        stats: Estatísticas por cliente.
        total_transacoes: Número total de transações processadas.
        meses_info: Dicionário {mês: quantidade_transações}.

    Returns:
        String formatada com o resumo executivo.
    """
    # Calcula totais gerais
    total_gasto = sum(s['total_gasto'] for s in stats.values())
    total_recebido = sum(s['total_recebido'] for s in stats.values())
    num_clientes = len(stats)

    # Encontra o cliente que mais gastou
    cliente_top = max(stats.items(), key=lambda x: x[1]['total_gasto'])

    # Calcula média mensal de gastos (3 meses)
    num_meses = len(meses_info)
    media_mensal = total_gasto / num_meses if num_meses > 0 else 0.0

    resumo = (
        f"No período analisado ({num_meses} meses), foram processadas "
        f"{total_transacoes} transações envolvendo {num_clientes} clientes. "
        f"O volume total de débitos foi de R$ {total_gasto:,.2f}, "
        f"enquanto os créditos somaram R$ {total_recebido:,.2f}. "
        f"A média mensal de gastos ficou em R$ {media_mensal:,.2f}. "
        f"O cliente com maior volume de débitos foi "
        f"{cliente_top[1]['nome']} (ID {cliente_top[0]}), "
        f"com R$ {cliente_top[1]['total_gasto']:,.2f} em gastos "
        f"distribuídos em {len(cliente_top[1]['categorias'])} categorias."
    )

    return resumo


# ═══════════════════════════════════════════════════════════════════════════
# EXIBIÇÃO DO RELATÓRIO
# ═══════════════════════════════════════════════════════════════════════════


def exibir_relatorio(meses_info: dict[str, int],
                     por_categoria: dict[str, list[dict]],
                     stats: dict[str, dict],
                     resumo: str) -> None:
    """Imprime o relatório completo no terminal."""

    print("\n" + "=" * 70)
    print("  📊 RELATÓRIO CONSOLIDADO — TRANSAÇÕES BANCÁRIAS (JAN-MAR 2025)")
    print("=" * 70)

    # — Seção 1: Transações por mês —
    print("\n  📅 TRANSAÇÕES POR MÊS:")
    print("  " + "-" * 40)
    total = 0
    for mes, qtd in meses_info.items():
        print(f"    {mes:<15s} {qtd:>5d} transações")
        total += qtd
    print(f"    {'TOTAL':<15s} {total:>5d} transações")

    # — Seção 2: Top 5 categorias de gasto —
    print("\n  📂 TOP 5 CATEGORIAS DE GASTO (DÉBITOS):")
    print("  " + "-" * 50)

    totais_categoria = {}
    for categoria, transacoes in por_categoria.items():
        total_debitos = sum(t['valor'] for t in transacoes if t['tipo'] == 'debito')
        if total_debitos > 0:
            totais_categoria[categoria] = total_debitos

    top_categorias = sorted(
        totais_categoria.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    for i, (categoria, valor) in enumerate(top_categorias, 1):
        barra = "█" * int(valor / max(v for _, v in top_categorias) * 20)
        print(f"    {i}. {categoria:<18s} R$ {valor:>10,.2f}  {barra}")

    # — Seção 3: Top 5 clientes por volume —
    print("\n  👤 TOP 5 CLIENTES POR VOLUME TOTAL:")
    print("  " + "-" * 50)

    volume_clientes = [
        (id_c, info['nome'], info['total_gasto'] + info['total_recebido'])
        for id_c, info in stats.items()
    ]
    volume_clientes.sort(key=lambda x: x[2], reverse=True)

    for i, (id_cliente, nome, volume) in enumerate(volume_clientes[:5], 1):
        print(f"    {i}. {nome:<30s} R$ {volume:>10,.2f}")

    # — Seção 4: Média de gastos mensais —
    total_gastos = sum(s['total_gasto'] for s in stats.values())
    num_meses = len(meses_info)
    media_mensal = total_gastos / num_meses if num_meses > 0 else 0.0

    print(f"\n  📈 MÉDIA DE GASTOS MENSAIS: R$ {media_mensal:>10,.2f}")

    # — Seção 5: Resumo executivo —
    print("\n  📝 RESUMO EXECUTIVO:")
    print("  " + "-" * 50)

    # Quebra o texto em linhas de ~65 caracteres para legibilidade
    palavras = resumo.split()
    linha_atual = "    "
    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 > 70:
            print(linha_atual)
            linha_atual = "    " + palavra
        else:
            linha_atual += " " + palavra if linha_atual.strip() else "    " + palavra
    if linha_atual.strip():
        print(linha_atual)

    print("\n" + "=" * 70)
    print("  ✅ Pipeline executado com sucesso!")
    print("=" * 70 + "\n")


# ═══════════════════════════════════════════════════════════════════════════
# FUNÇÃO PRINCIPAL — ORQUESTRAÇÃO DO PIPELINE
# ═══════════════════════════════════════════════════════════════════════════


def main():
    """
    Orquestra o pipeline completo:
      1. Carrega transações de cada mês
      2. Consolida em lista única
      3. Classifica por categoria
      4. Calcula estatísticas por cliente
      5. Gera e exibe relatório
    """
    try:
        # Etapa 1: Carregar dados
        print("\n  ⏳ Carregando dados...")
        transacoes_por_mes = {}
        meses_info = {}

        for mes, caminho in ARQUIVOS_TRANSACOES.items():
            transacoes = carregar_transacoes(caminho)
            transacoes_por_mes[mes] = transacoes
            meses_info[mes] = len(transacoes)
            print(f"    ✅ {mes}: {len(transacoes)} transações carregadas")

        clientes = carregar_clientes(ARQUIVO_CLIENTES)
        print(f"    ✅ Clientes: {len(clientes)} registros carregados")

        # Etapa 2: Consolidar
        todas_transacoes = consolidar_transacoes(list(transacoes_por_mes.values()))
        print(f"\n  📦 Total consolidado: {len(todas_transacoes)} transações")

        # Etapa 3: Classificar por categoria
        por_categoria = classificar_por_categoria(todas_transacoes)
        print(f"  📂 Categorias encontradas: {len(por_categoria)}")

        # Etapa 4: Estatísticas por cliente
        stats = calcular_estatisticas_cliente(todas_transacoes, clientes)
        print(f"  👤 Clientes com movimentação: {len(stats)}")

        # Etapa 5: Gerar resumo e exibir relatório
        resumo = gerar_resumo_executivo(stats, len(todas_transacoes), meses_info)
        exibir_relatorio(meses_info, por_categoria, stats, resumo)

    except FileNotFoundError as erro:
        print(f"\n  ❌ Erro ao carregar arquivo: {erro}")
    except Exception as erro:
        print(f"\n  ❌ Erro inesperado: {erro}")
        raise


if __name__ == '__main__':
    main()
