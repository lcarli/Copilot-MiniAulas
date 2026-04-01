"""
Lab 1 — Solução de Referência: Refatoração com Copilot

Versão refatorada do código monolítico de análise de clientes.
Demonstra boas práticas: funções com responsabilidade única,
nomes descritivos, tratamento de exceções e docstrings.
"""

import csv
import os


def carregar_clientes(caminho_csv: str) -> list[dict]:
    """Lê o arquivo CSV de clientes e retorna uma lista de dicionários.

    Args:
        caminho_csv: Caminho para o arquivo CSV de clientes.

    Returns:
        Lista de dicionários com os dados de cada cliente.

    Raises:
        FileNotFoundError: Se o arquivo CSV não for encontrado.
    """
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")

    clientes = []
    with open(caminho_csv, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                linha["saldo_atual"] = float(linha["saldo_atual"])
            except (ValueError, KeyError) as e:
                print(f"⚠️  Dado inválido ignorado na linha: {linha} — Erro: {e}")
                continue
            clientes.append(linha)

    return clientes


def calcular_estatisticas(clientes: list[dict]) -> dict:
    """Calcula estatísticas dos saldos dos clientes.

    Args:
        clientes: Lista de dicionários com dados dos clientes.

    Returns:
        Dicionário com total, média, menor e maior saldo, e quantidade.
    """
    if not clientes:
        return {"total": 0, "media": 0, "menor": 0, "maior": 0, "quantidade": 0}

    saldos = [cliente["saldo_atual"] for cliente in clientes]
    total = sum(saldos)
    quantidade = len(saldos)

    return {
        "total": total,
        "media": total / quantidade,
        "menor": min(saldos),
        "maior": max(saldos),
        "quantidade": quantidade,
    }


def agrupar_por_agencia(clientes: list[dict]) -> dict[str, float]:
    """Agrupa os saldos dos clientes por agência.

    Args:
        clientes: Lista de dicionários com dados dos clientes.

    Returns:
        Dicionário com o saldo total por agência.
    """
    totais_por_agencia = {}
    for cliente in clientes:
        agencia = cliente["agencia"]
        totais_por_agencia[agencia] = (
            totais_por_agencia.get(agencia, 0) + cliente["saldo_atual"]
        )
    return totais_por_agencia


def verificar_alertas(clientes: list[dict]) -> list[str]:
    """Verifica condições de alerta nos saldos dos clientes.

    Args:
        clientes: Lista de dicionários com dados dos clientes.

    Returns:
        Lista de mensagens de alerta.
    """
    alertas = []
    for cliente in clientes:
        nome = cliente["nome"]
        saldo = cliente["saldo_atual"]

        if saldo > 10000:
            alertas.append(f"🔔 SALDO ALTO: {nome} — R$ {saldo:,.2f}")
        if saldo < 0:
            alertas.append(f"🚨 SALDO NEGATIVO: {nome} — R$ {saldo:,.2f}")

    return alertas


def exibir_relatorio(estatisticas: dict, totais_agencia: dict, alertas: list[str]) -> None:
    """Exibe o relatório formatado no terminal.

    Args:
        estatisticas: Dicionário com as estatísticas calculadas.
        totais_agencia: Dicionário com os totais por agência.
        alertas: Lista de mensagens de alerta.
    """
    print("=" * 50)
    print("      RELATÓRIO DE CLIENTES — BANCO PYTHON")
    print("=" * 50)

    print(f"\n📊 Estatísticas Gerais:")
    print(f"   Quantidade de clientes: {estatisticas['quantidade']}")
    print(f"   Saldo total:   R$ {estatisticas['total']:>12,.2f}")
    print(f"   Saldo médio:   R$ {estatisticas['media']:>12,.2f}")
    print(f"   Menor saldo:   R$ {estatisticas['menor']:>12,.2f}")
    print(f"   Maior saldo:   R$ {estatisticas['maior']:>12,.2f}")

    print(f"\n🏦 Saldo por Agência:")
    for agencia in sorted(totais_agencia):
        print(f"   Agência {agencia}: R$ {totais_agencia[agencia]:>12,.2f}")

    if alertas:
        print(f"\n⚠️  Alertas ({len(alertas)}):")
        for alerta in alertas:
            print(f"   {alerta}")
    else:
        print("\n✅ Nenhum alerta encontrado.")

    print("\n" + "=" * 50)


def main():
    """Função principal que orquestra a execução do relatório."""
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(diretorio_base, "..", "..", "aula1", "dados", "clientes.csv")

    try:
        clientes = carregar_clientes(caminho_csv)
    except FileNotFoundError as e:
        print(f"❌ Erro: {e}")
        return

    if not clientes:
        print("⚠️  Nenhum cliente encontrado no arquivo.")
        return

    estatisticas = calcular_estatisticas(clientes)
    totais_agencia = agrupar_por_agencia(clientes)
    alertas = verificar_alertas(clientes)

    exibir_relatorio(estatisticas, totais_agencia, alertas)


if __name__ == "__main__":
    main()
