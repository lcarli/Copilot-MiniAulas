"""
Etapa 3 - Resultado esperado COM INSTRUCTIONS ativas.

Mesmo prompt da Etapa 2, mas agora com .github/copilot-instructions.md ativo.

Diferencas visiveis em relacao a Etapa 2:
- Codigo modularizado em funcoes
- Docstrings em todas as funcoes (Google style)
- Encoding utf-8 explicito
- Caminhos relativos com __file__
- Tratamento de erros com try/except
- Valores formatados no padrao brasileiro (R$ 1.234,56)
- Variaveis com nomes descritivos em portugues
- Main guard (if __name__ == "__main__")
"""

import csv
import os


def carregar_extrato(caminho_arquivo):
    """Carrega o extrato bancario de um arquivo CSV.

    Args:
        caminho_arquivo: Caminho para o arquivo CSV.

    Returns:
        Lista de dicionarios com as transacoes.

    Raises:
        FileNotFoundError: Se o arquivo nao for encontrado.
    """
    try:
        with open(caminho_arquivo, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Erro: Arquivo nao encontrado: {caminho_arquivo}")
        return []


def calcular_totais(transacoes):
    """Calcula o total de debitos e creditos.

    Args:
        transacoes: Lista de dicionarios com as transacoes.

    Returns:
        Tupla (total_debitos, total_creditos).
    """
    total_debitos = 0.0
    total_creditos = 0.0

    for t in transacoes:
        try:
            valor = float(t["valor"])
        except (ValueError, KeyError):
            continue

        if t.get("tipo") == "debito":
            total_debitos += valor
        elif t.get("tipo") == "credito":
            total_creditos += valor

    return total_debitos, total_creditos


def agrupar_gastos_por_categoria(transacoes):
    """Agrupa os gastos (debitos) por categoria.

    Args:
        transacoes: Lista de dicionarios com as transacoes.

    Returns:
        Dicionario {categoria: valor_total}, ordenado do maior para o menor.
    """
    gastos = {}
    for t in transacoes:
        if t.get("tipo") != "debito":
            continue
        try:
            valor = float(t["valor"])
        except (ValueError, KeyError):
            continue
        categoria = t.get("categoria", "outros")
        gastos[categoria] = gastos.get(categoria, 0.0) + valor

    return dict(sorted(gastos.items(), key=lambda x: x[1], reverse=True))


def formatar_moeda(valor):
    """Formata um valor numerico no padrao monetario brasileiro.

    Args:
        valor: Valor numerico a ser formatado.

    Returns:
        String formatada (ex: R$ 1.234,56).
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def gerar_relatorio(transacoes):
    """Gera e exibe um relatorio completo do extrato bancario.

    Args:
        transacoes: Lista de dicionarios com as transacoes.
    """
    total_debitos, total_creditos = calcular_totais(transacoes)
    gastos_por_categoria = agrupar_gastos_por_categoria(transacoes)
    saldo = total_creditos - total_debitos

    print("=" * 55)
    print("       RELATORIO DE EXTRATO - MARCO 2025")
    print("=" * 55)

    print(f"\n  Receitas (creditos): {formatar_moeda(total_creditos):>15}")
    print(f"  Gastos (debitos):    {formatar_moeda(total_debitos):>15}")
    print(f"  Saldo do mes:        {formatar_moeda(saldo):>15}")

    print("\n" + "-" * 55)
    print("  GASTOS POR CATEGORIA")
    print("-" * 55)

    for categoria, valor in gastos_por_categoria.items():
        percentual = (valor / total_debitos * 100) if total_debitos > 0 else 0
        print(f"  {categoria:<15} {formatar_moeda(valor):>15}  ({percentual:5.1f}%)")

    print("-" * 55)
    print(f"  {'TOTAL':<15} {formatar_moeda(total_debitos):>15}  (100.0%)")

    if gastos_por_categoria:
        maior_cat = next(iter(gastos_por_categoria))
        maior_val = gastos_por_categoria[maior_cat]
        print(f"\n  Maior gasto: {maior_cat} ({formatar_moeda(maior_val)})")

    print(f"  Total de transacoes: {len(transacoes)}")
    print("=" * 55)


if __name__ == "__main__":
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "dados", "extrato_conta.csv"
    )
    extrato = carregar_extrato(caminho)
    if extrato:
        gerar_relatorio(extrato)
