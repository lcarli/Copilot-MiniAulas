# ============================================================
# Demo 02 - Leitura de dados bancários a partir de CSV
# ============================================================
# Nesta demo vamos ler o arquivo clientes.csv usando apenas
# o módulo csv da biblioteca padrão do Python (sem pandas).
#
# Vamos praticar:
#   - Abrir e ler um CSV
#   - Percorrer linhas e acessar campos
#   - Filtrar dados por critério
#   - Encontrar valores máximos
# ============================================================

import csv
import os


def carregar_clientes(caminho: str) -> list:
    """Lê o CSV de clientes e retorna uma lista de dicionários."""
    clientes = []
    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            # Converte o saldo para float para podermos fazer cálculos
            linha["saldo_atual"] = float(linha["saldo_atual"])
            clientes.append(linha)
    return clientes


def listar_nomes(clientes: list) -> list:
    """Retorna a lista de nomes de todos os clientes."""
    return [c["nome"] for c in clientes]


def filtrar_por_tipo_conta(clientes: list, tipo: str) -> list:
    """Filtra clientes pelo tipo de conta (corrente ou poupanca)."""
    return [c for c in clientes if c["tipo_conta"] == tipo]


def cliente_maior_saldo(clientes: list) -> dict:
    """Retorna o cliente com o maior saldo."""
    return max(clientes, key=lambda c: c["saldo_atual"])


# ============================================================
# Bloco principal
# ============================================================
if __name__ == "__main__":
    # Caminho relativo ao arquivo — funciona em qualquer máquina
    caminho_csv = os.path.join(
        os.path.dirname(__file__), "..", "dados", "clientes.csv"
    )

    # Passo 1: Carregar os dados
    clientes = carregar_clientes(caminho_csv)

    print("=" * 55)
    print("  DEMO 02 — Leitura de dados bancários (CSV)")
    print("=" * 55)

    # Passo 2: Quantos clientes existem?
    print(f"\n📊 Total de clientes cadastrados: {len(clientes)}")

    # Passo 3: Listar todos os nomes
    nomes = listar_nomes(clientes)
    print("\n📋 Lista de clientes:")
    for i, nome in enumerate(nomes, start=1):
        print(f"  {i:>2}. {nome}")

    # Passo 4: Filtrar por tipo de conta
    corrente = filtrar_por_tipo_conta(clientes, "corrente")
    poupanca = filtrar_por_tipo_conta(clientes, "poupanca")
    print(f"\n🏦 Contas corrente: {len(corrente)}")
    print(f"💰 Contas poupança: {len(poupanca)}")

    # Passo 5: Cliente com maior saldo
    top = cliente_maior_saldo(clientes)
    print(f"\n🏆 Cliente com maior saldo:")
    print(f"   Nome:   {top['nome']}")
    print(f"   Conta:  {top['tipo_conta']}")
    print(f"   Saldo:  R$ {top['saldo_atual']:,.2f}")

    print("\n" + "=" * 55)
    print("  ✅ Demo 02 concluída com sucesso!")
    print("=" * 55)
