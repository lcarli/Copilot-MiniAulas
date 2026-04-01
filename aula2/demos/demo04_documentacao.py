"""
=============================================================================
  DEMO 04 — Geração Automática de Documentação com GitHub Copilot
  Aula 2: Desenvolvimento Assistido por IA
=============================================================================

  OBJETIVO:
    Mostrar como o Copilot gera documentação de qualidade automaticamente.
    O instrutor apresenta funções SEM docstrings e pede ao Copilot para
    documentá-las.

  COMO USAR NA AULA:
    1. Mostre as funções sem documentação (abaixo)
    2. Selecione todas as funções e peça ao Copilot:
       "Gere docstrings para todas as funções deste arquivo"
    3. Compare com a versão documentada no final do arquivo
    4. Mostre o template de README.md gerado por IA
=============================================================================
"""

import csv
import os
import sys
from datetime import datetime

# Garante saída UTF-8 no terminal Windows
sys.stdout.reconfigure(encoding='utf-8')


# ═══════════════════════════════════════════════════════════════════════════
# 🔴 FUNÇÕES SEM DOCUMENTAÇÃO
#    Peça ao Copilot: "Gere docstrings para todas as funções deste arquivo"
# ═══════════════════════════════════════════════════════════════════════════


def validar_cpf(cpf):
    cpf_limpo = ''.join(c for c in cpf if c.isdigit())

    if len(cpf_limpo) != 11:
        return False

    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    # Calcula primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    if int(cpf_limpo[9]) != digito1:
        return False

    # Calcula segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf_limpo[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if int(cpf_limpo[10]) != digito2:
        return False

    return True


def formatar_valor_monetario(valor, moeda="R$", decimais=2):
    if not isinstance(valor, (int, float)):
        raise TypeError(f"Esperado número, recebido {type(valor).__name__}")

    valor_formatado = f"{abs(valor):,.{decimais}f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")

    sinal = "-" if valor < 0 else ""
    return f"{sinal}{moeda} {valor_formatado}"


def calcular_media_movel(valores, janela=3):
    if not valores:
        return []

    if janela < 1:
        raise ValueError("A janela deve ser pelo menos 1")

    if janela > len(valores):
        janela = len(valores)

    medias = []
    for i in range(len(valores)):
        inicio = max(0, i - janela + 1)
        subset = valores[inicio:i + 1]
        medias.append(sum(subset) / len(subset))

    return medias


def filtrar_transacoes_por_periodo(transacoes, data_inicio, data_fim,
                                   formato_data="%Y-%m-%d"):
    inicio = datetime.strptime(data_inicio, formato_data)
    fim = datetime.strptime(data_fim, formato_data)

    if inicio > fim:
        raise ValueError("Data de início não pode ser posterior à data de fim")

    filtradas = []
    for transacao in transacoes:
        data_transacao = datetime.strptime(transacao['data'], formato_data)
        if inicio <= data_transacao <= fim:
            filtradas.append(transacao)

    return filtradas


# ═══════════════════════════════════════════════════════════════════════════
# DEMONSTRAÇÃO — Executando as funções para provar que funcionam
# ═══════════════════════════════════════════════════════════════════════════


def main():
    """Demonstra o uso de cada função."""
    print("\n" + "=" * 60)
    print("  📝 DEMO DE DOCUMENTAÇÃO — Funções Utilitárias Bancárias")
    print("=" * 60)

    # --- Teste 1: Validação de CPF ---
    print("\n  🔍 Teste: validar_cpf()")
    print("  " + "-" * 40)

    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    caminho_clientes = os.path.join(diretorio_base, '..', '..', 'aula1', 'dados', 'clientes.csv')

    with open(caminho_clientes, encoding='utf-8') as f:
        clientes = list(csv.DictReader(f))

    for cliente in clientes[:5]:
        cpf = cliente['cpf']
        valido = validar_cpf(cpf)
        status = "✅ Válido" if valido else "❌ Inválido"
        print(f"    {cliente['nome']:<30s} CPF: {cpf}  → {status}")

    # --- Teste 2: Formatação monetária ---
    print("\n  💰 Teste: formatar_valor_monetario()")
    print("  " + "-" * 40)

    valores_teste = [1234.56, -789.10, 0.0, 1000000.00, 42.5]
    for valor in valores_teste:
        print(f"    {valor:>15,.2f}  →  {formatar_valor_monetario(valor)}")

    # --- Teste 3: Média móvel ---
    print("\n  📈 Teste: calcular_media_movel()")
    print("  " + "-" * 40)

    # Usa valores reais de transações
    caminho_transacoes = os.path.join(diretorio_base, '..', 'dados', 'transacoes_janeiro.csv')
    with open(caminho_transacoes, encoding='utf-8') as f:
        transacoes = list(csv.DictReader(f))

    valores = [float(t['valor']) for t in transacoes[:10]]
    medias = calcular_media_movel(valores, janela=3)

    print(f"    Valores originais (10 primeiras):")
    for i, (v, m) in enumerate(zip(valores, medias)):
        print(f"      [{i+1:>2d}] Valor: R$ {v:>8,.2f}  |  Média Móvel (3): R$ {m:>8,.2f}")

    # --- Teste 4: Filtrar por período ---
    print("\n  📅 Teste: filtrar_transacoes_por_periodo()")
    print("  " + "-" * 40)

    filtradas = filtrar_transacoes_por_periodo(
        transacoes,
        data_inicio="2025-01-10",
        data_fim="2025-01-15"
    )
    print(f"    Período: 10/01/2025 a 15/01/2025")
    print(f"    Transações encontradas: {len(filtradas)}")
    for t in filtradas[:5]:
        print(f"      {t['data']}  {t['categoria']:<15s}  R$ {float(t['valor']):>8,.2f}")

    print("\n" + "=" * 60)
    print("  ✅ Todas as funções executadas com sucesso!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()


# ═══════════════════════════════════════════════════════════════════════════
# 🟢 VERSÃO COM DOCSTRINGS — Como ficaria após pedir ao Copilot
#    (O instrutor mostra este bloco DEPOIS de pedir ao Copilot para gerar)
# ═══════════════════════════════════════════════════════════════════════════

# def validar_cpf(cpf):
#     """
#     Valida um número de CPF brasileiro.
#
#     Verifica se o CPF tem 11 dígitos, não é uma sequência repetida
#     e se os dígitos verificadores estão corretos conforme o algoritmo
#     oficial da Receita Federal.
#
#     Args:
#         cpf (str): CPF a ser validado. Aceita formatos com ou sem
#                    pontuação (ex: "123.456.789-09" ou "12345678909").
#
#     Returns:
#         bool: True se o CPF é válido, False caso contrário.
#
#     Examples:
#         >>> validar_cpf("123.456.789-09")
#         True
#         >>> validar_cpf("111.111.111-11")
#         False
#     """

# def formatar_valor_monetario(valor, moeda="R$", decimais=2):
#     """
#     Formata um valor numérico como moeda brasileira.
#
#     Converte um número em string formatada com separador de milhar (ponto),
#     separador decimal (vírgula) e símbolo de moeda. Valores negativos
#     recebem o sinal de menos antes do símbolo.
#
#     Args:
#         valor (int | float): Valor numérico a ser formatado.
#         moeda (str): Símbolo da moeda. Padrão: "R$".
#         decimais (int): Número de casas decimais. Padrão: 2.
#
#     Returns:
#         str: Valor formatado como moeda (ex: "R$ 1.234,56").
#
#     Raises:
#         TypeError: Se valor não for int ou float.
#
#     Examples:
#         >>> formatar_valor_monetario(1234.5)
#         'R$ 1.234,50'
#         >>> formatar_valor_monetario(-50)
#         '-R$ 50,00'
#     """

# def calcular_media_movel(valores, janela=3):
#     """
#     Calcula a média móvel de uma lista de valores numéricos.
#
#     Para cada posição i, calcula a média dos últimos 'janela' valores
#     (ou menos, se não houver valores suficientes no início da lista).
#
#     Args:
#         valores (list[float]): Lista de valores numéricos.
#         janela (int): Tamanho da janela da média móvel. Padrão: 3.
#
#     Returns:
#         list[float]: Lista de médias móveis com o mesmo comprimento
#                      da lista original. Retorna lista vazia se a
#                      entrada for vazia.
#
#     Raises:
#         ValueError: Se a janela for menor que 1.
#
#     Examples:
#         >>> calcular_media_movel([10, 20, 30, 40], janela=2)
#         [10.0, 15.0, 25.0, 35.0]
#     """

# def filtrar_transacoes_por_periodo(transacoes, data_inicio, data_fim,
#                                    formato_data="%Y-%m-%d"):
#     """
#     Filtra uma lista de transações por período de datas.
#
#     Retorna apenas as transações cuja data está dentro do intervalo
#     [data_inicio, data_fim] (inclusive em ambos os extremos).
#
#     Args:
#         transacoes (list[dict]): Lista de transações. Cada transação
#             deve ter uma chave 'data' no formato especificado.
#         data_inicio (str): Data inicial do filtro (ex: "2025-01-01").
#         data_fim (str): Data final do filtro (ex: "2025-01-31").
#         formato_data (str): Formato das datas. Padrão: "%Y-%m-%d".
#
#     Returns:
#         list[dict]: Lista de transações dentro do período.
#
#     Raises:
#         ValueError: Se data_inicio for posterior a data_fim.
#
#     Examples:
#         >>> transacoes = [{'data': '2025-01-05', 'valor': 100}]
#         >>> filtrar_transacoes_por_periodo(transacoes, '2025-01-01', '2025-01-31')
#         [{'data': '2025-01-05', 'valor': 100}]
#     """


# ═══════════════════════════════════════════════════════════════════════════
# 📄 TEMPLATE DE README.md — Peça ao Copilot para gerar!
#
#    Instrução para o Copilot:
#    "Gere um README.md profissional para este projeto de análise
#     bancária. Inclua: descrição, instalação, uso, estrutura de
#     pastas e exemplos."
#
#    Exemplo de como ficaria:
# ═══════════════════════════════════════════════════════════════════════════

# # 🏦 Sistema de Análise de Transações Bancárias
#
# ## Descrição
# Sistema de análise e relatórios de transações bancárias desenvolvido
# em Python com auxílio do GitHub Copilot. Processa dados mensais de
# transações, cruza com cadastros de clientes e gera relatórios
# executivos automatizados.
#
# ## Requisitos
# - Python 3.10+
# - Módulos padrão: csv, os, datetime, collections
#
# ## Instalação
# ```bash
# git clone <url-do-repositorio>
# cd aulaCopilot
# pip install -r requirements.txt
# ```
#
# ## Estrutura do Projeto
# ```
# aulaCopilot/
# ├── aula1/
# │   ├── dados/          # Dados de clientes
# │   ├── demos/          # Demos da Aula 1
# │   └── labs/           # Laboratórios da Aula 1
# ├── aula2/
# │   ├── dados/          # Transações mensais (CSV)
# │   ├── demos/          # Demos da Aula 2
# │   │   ├── demo01_refatoracao.py
# │   │   ├── demo02_debugging.py
# │   │   ├── demo03_pipeline.py
# │   │   └── demo04_documentacao.py
# │   └── labs/           # Laboratórios da Aula 2
# ├── recursos/           # Material de apoio
# └── requirements.txt
# ```
#
# ## Uso
# ```bash
# # Executar o pipeline completo
# python aula2/demos/demo03_pipeline.py
#
# # Demonstração de refatoração
# python aula2/demos/demo01_refatoracao.py
#
# # Demonstração de documentação
# python aula2/demos/demo04_documentacao.py
# ```
#
# ## Funcionalidades
# - 📊 Análise consolidada de transações (múltiplos meses)
# - 👤 Estatísticas por cliente
# - 📂 Classificação por categoria de gasto
# - 📈 Cálculo de média móvel
# - ✅ Validação de CPF
# - 💰 Formatação monetária brasileira
#
# ## Licença
# Projeto educacional — uso livre para fins de aprendizagem.
