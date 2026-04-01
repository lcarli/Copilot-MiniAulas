"""
Lab 2 — Solução de Referência: Relatório Mensal de Gastos por Categoria (Opção A)

Consolida transações de Janeiro a Março de 2025 e gera um relatório
de gastos (débitos) agrupados por categoria com total, média e percentual.
"""

import csv
import os


def carregar_transacoes(caminho_csv: str) -> list[dict]:
    """Lê um arquivo CSV de transações e retorna uma lista de dicionários.

    Args:
        caminho_csv: Caminho para o arquivo CSV de transações.

    Returns:
        Lista de dicionários com os dados de cada transação.

    Raises:
        FileNotFoundError: Se o arquivo CSV não for encontrado.
    """
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")

    transacoes = []
    with open(caminho_csv, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                linha["valor"] = float(linha["valor"])
            except (ValueError, KeyError) as e:
                print(f"⚠️  Dado inválido ignorado: {linha} — Erro: {e}")
                continue
            transacoes.append(linha)

    return transacoes


def consolidar_transacoes(diretorio_dados: str) -> list[dict]:
    """Consolida os 3 arquivos mensais de transações em uma lista única.

    Args:
        diretorio_dados: Caminho para o diretório que contém os CSVs.

    Returns:
        Lista consolidada com todas as transações dos 3 meses.
    """
    arquivos = [
        "transacoes_janeiro.csv",
        "transacoes_fevereiro.csv",
        "transacoes_marco.csv",
    ]

    todas_transacoes = []
    for arquivo in arquivos:
        caminho = os.path.join(diretorio_dados, arquivo)
        try:
            transacoes = carregar_transacoes(caminho)
            todas_transacoes.extend(transacoes)
            print(f"✅ {arquivo}: {len(transacoes)} transações carregadas")
        except FileNotFoundError as e:
            print(f"❌ {e}")

    return todas_transacoes


def filtrar_debitos(transacoes: list[dict]) -> list[dict]:
    """Filtra apenas as transações de débito (gastos).

    Args:
        transacoes: Lista de todas as transações.

    Returns:
        Lista contendo somente as transações do tipo 'debito'.
    """
    return [t for t in transacoes if t.get("tipo") == "debito"]


def agrupar_por_categoria(debitos: list[dict]) -> dict[str, dict]:
    """Agrupa débitos por categoria e calcula estatísticas.

    Args:
        debitos: Lista de transações de débito.

    Returns:
        Dicionário onde cada chave é uma categoria e o valor é um dict
        com 'total', 'quantidade', 'media' e 'percentual'.
    """
    totais = {}
    for transacao in debitos:
        categoria = transacao["categoria"]
        valor = transacao["valor"]

        if categoria not in totais:
            totais[categoria] = {"total": 0.0, "quantidade": 0, "valores": []}

        totais[categoria]["total"] += valor
        totais[categoria]["quantidade"] += 1
        totais[categoria]["valores"].append(valor)

    total_geral = sum(dados["total"] for dados in totais.values())

    resultado = {}
    for categoria, dados in totais.items():
        resultado[categoria] = {
            "total": dados["total"],
            "quantidade": dados["quantidade"],
            "media": dados["total"] / dados["quantidade"],
            "percentual": (dados["total"] / total_geral * 100) if total_geral > 0 else 0,
        }

    return resultado


def exibir_relatorio(categorias: dict[str, dict], total_transacoes: int) -> None:
    """Exibe o relatório de gastos por categoria formatado no terminal.

    Args:
        categorias: Dicionário com estatísticas por categoria.
        total_transacoes: Número total de transações (débitos).
    """
    total_geral = sum(dados["total"] for dados in categorias.values())

    # Ordena por total (maior para menor)
    categorias_ordenadas = sorted(
        categorias.items(), key=lambda x: x[1]["total"], reverse=True
    )

    print()
    print("═" * 65)
    print("   RELATÓRIO DE GASTOS POR CATEGORIA — JAN a MAR/2025")
    print("═" * 65)
    print()
    print(f" {'Categoria':<18} {'Total (R$)':>12} {'Média (R$)':>12} {'Qtd':>5} {'%':>7}")
    print(" " + "─" * 60)

    for categoria, dados in categorias_ordenadas:
        print(
            f" {categoria:<18} "
            f"{dados['total']:>12,.2f} "
            f"{dados['media']:>12,.2f} "
            f"{dados['quantidade']:>5} "
            f"{dados['percentual']:>6.1f}%"
        )

    print(" " + "─" * 60)
    print(f" {'TOTAL GERAL':<18} {total_geral:>12,.2f} {'':>12} {total_transacoes:>5} {'100.0%':>7}")
    print()
    print("═" * 65)
    print()


def main():
    """Função principal que orquestra a geração do relatório."""
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    diretorio_dados = os.path.join(diretorio_base, "..", "dados")

    print()
    print("📂 Carregando transações...")
    print()

    todas_transacoes = consolidar_transacoes(diretorio_dados)

    if not todas_transacoes:
        print("⚠️  Nenhuma transação encontrada. Verifique os arquivos.")
        return

    debitos = filtrar_debitos(todas_transacoes)

    if not debitos:
        print("⚠️  Nenhuma transação de débito encontrada.")
        return

    print(f"\n📊 Total de transações carregadas: {len(todas_transacoes)}")
    print(f"💳 Transações de débito (gastos): {len(debitos)}")

    categorias = agrupar_por_categoria(debitos)
    exibir_relatorio(categorias, len(debitos))


if __name__ == "__main__":
    main()
