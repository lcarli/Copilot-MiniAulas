"""
=============================================================================
  DEMO 02 — Debugging com GitHub Copilot
  Aula 2: Desenvolvimento Assistido por IA
=============================================================================

  OBJETIVO:
    Código com 5 bugs INTENCIONAIS para o instrutor demonstrar ao vivo
    como o Copilot identifica, explica e corrige cada erro.

  COMO USAR NA AULA:
    1. Execute o script → ele vai falhar
    2. Selecione o erro no terminal e pergunte ao Copilot: "O que causou este erro?"
    3. Peça: "Corrija este bug"
    4. Vá corrigindo bug a bug com a turma

  DICA: Os bugs estão numerados (🐛 BUG 1 a 5).
        As correções estão logo abaixo, comentadas (✅ CORREÇÃO).
=============================================================================
"""

import csv
import os
import sys

# Garante saída UTF-8 no terminal Windows
sys.stdout.reconfigure(encoding='utf-8')

# Diretório base do script
DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))


def analisar_transacoes_por_categoria(caminho_csv: str) -> dict:
    """
    Analisa transações agrupadas por categoria.
    Retorna um dicionário com total e média por categoria.
    """

    # ──────────────────────────────────────────────────────────────
    # 🐛 BUG 4: FileNotFoundError — caminho incorreto sem tratamento
    #   O arquivo está em "dados/", mas o caminho abaixo usa "data/"
    #   Além disso, não há try/except para tratar o erro
    # ──────────────────────────────────────────────────────────────
    arquivo = open(
        os.path.join(DIRETORIO_BASE, '..', 'data', 'transacoes_janeiro.csv'),
        encoding='utf-8'
    )
    # ✅ CORREÇÃO: usar o caminho correto e tratar o erro
    # try:
    #     arquivo = open(
    #         os.path.join(DIRETORIO_BASE, '..', 'dados', 'transacoes_janeiro.csv'),
    #         encoding='utf-8'
    #     )
    # except FileNotFoundError:
    #     print(f"❌ Arquivo não encontrado! Verifique o caminho.")
    #     return {}

    leitor = csv.DictReader(arquivo)
    transacoes_por_categoria = {}

    for linha in leitor:
        categoria = linha['categoria']
        valor = linha['valor']

        # ──────────────────────────────────────────────────────────
        # 🐛 BUG 3: TypeError — valor lido do CSV é string, não número
        #   A linha abaixo tenta somar string com float, causando:
        #   TypeError: unsupported operand type(s) for +=: 'float' and 'str'
        # ──────────────────────────────────────────────────────────
        if categoria not in transacoes_por_categoria:
            transacoes_por_categoria[categoria] = {
                'total': 0.0,
                'transacoes': []
            }

        transacoes_por_categoria[categoria]['total'] += valor  # 💥 valor é string!
        transacoes_por_categoria[categoria]['transacoes'].append(valor)
        # ✅ CORREÇÃO: converter valor para float antes de usar
        # valor_numerico = float(valor)
        # transacoes_por_categoria[categoria]['total'] += valor_numerico
        # transacoes_por_categoria[categoria]['transacoes'].append(valor_numerico)

    arquivo.close()
    return transacoes_por_categoria


def calcular_media_por_categoria(dados_categoria: dict) -> dict:
    """
    Calcula a média de gastos por categoria.
    """
    medias = {}

    for categoria, info in dados_categoria.items():
        total = info['total']
        transacoes = info['transacoes']

        # ──────────────────────────────────────────────────────────
        # 🐛 BUG 1: ZeroDivisionError — divisão por zero
        #   Se uma categoria não tiver transações (lista vazia),
        #   len(transacoes) será 0 e a divisão falhará.
        #   (Esse cenário pode ocorrer se filtramos transações antes)
        # ──────────────────────────────────────────────────────────
        media = total / len(transacoes)  # 💥 E se len(transacoes) == 0?
        # ✅ CORREÇÃO: verificar se a lista não está vazia antes de dividir
        # media = total / len(transacoes) if len(transacoes) > 0 else 0.0

        medias[categoria] = media

    return medias


def buscar_categoria_especifica(dados_categoria: dict, nome_categoria: str) -> float:
    """
    Busca o total de uma categoria específica no dicionário.
    """

    # ──────────────────────────────────────────────────────────────
    # 🐛 BUG 2: KeyError — acessa chave sem verificar se existe
    #   Se nome_categoria não existir no dicionário, dá KeyError.
    #   Ex: buscar "investimentos" quando só existem "alimentacao", etc.
    # ──────────────────────────────────────────────────────────────
    total = dados_categoria[nome_categoria]['total']  # 💥 KeyError!
    # ✅ CORREÇÃO: verificar se a chave existe antes de acessar
    # if nome_categoria in dados_categoria:
    #     total = dados_categoria[nome_categoria]['total']
    # else:
    #     print(f"⚠️  Categoria '{nome_categoria}' não encontrada.")
    #     total = 0.0

    return total


def encontrar_transacoes_altas(dados_categoria: dict, limite: float = 200.0) -> list:
    """
    Encontra transações com valor acima do limite especificado.
    """
    transacoes_altas = []

    for categoria, info in dados_categoria.items():
        for valor in info['transacoes']:
            # ──────────────────────────────────────────────────────
            # 🐛 BUG 5: Lógica invertida — usa > quando deveria usar <
            #   O objetivo é encontrar transações ACIMA do limite,
            #   mas o operador está invertido, retornando as ABAIXO.
            # ──────────────────────────────────────────────────────
            if valor < limite:  # 💥 Invertido! Deveria ser >
                transacoes_altas.append({
                    'categoria': categoria,
                    'valor': valor
                })
    # ✅ CORREÇÃO: usar o operador correto
    #         if valor > limite:
    #             transacoes_altas.append({
    #                 'categoria': categoria,
    #                 'valor': valor
    #             })

    return transacoes_altas


def main():
    """Função principal — executa a análise com os bugs."""
    print("\n" + "=" * 60)
    print("  🐛 DEMO DE DEBUGGING — Encontre os 5 Bugs!")
    print("=" * 60)

    # Etapa 1: Carregar e analisar (dispara BUG 4 → FileNotFoundError)
    print("\n  📂 Carregando transações...")
    dados = analisar_transacoes_por_categoria(
        os.path.join(DIRETORIO_BASE, '..', 'dados', 'transacoes_janeiro.csv')
    )

    # Etapa 2: Calcular médias (dispara BUG 1 → ZeroDivisionError)
    print("  📊 Calculando médias por categoria...")
    medias = calcular_media_por_categoria(dados)
    for cat, media in medias.items():
        print(f"    {cat}: R$ {media:,.2f}")

    # Etapa 3: Buscar categoria inexistente (dispara BUG 2 → KeyError)
    print("\n  🔍 Buscando total de 'investimentos'...")
    total_invest = buscar_categoria_especifica(dados, 'investimentos')
    print(f"    Total investimentos: R$ {total_invest:,.2f}")

    # Etapa 4: Filtrar transações altas (BUG 5 → lógica invertida)
    print("\n  📈 Transações acima de R$ 200,00:")
    altas = encontrar_transacoes_altas(dados, limite=200.0)
    print(f"    Encontradas: {len(altas)} transações")
    for t in altas[:5]:
        print(f"    - {t['categoria']}: R$ {t['valor']:,.2f}")

    print("\n" + "=" * 60)
    print("  ✅ Análise concluída (se você chegou aqui, corrigiu tudo!)")
    print("=" * 60)


# ═══════════════════════════════════════════════════════════════════════════
# GUIA PARA O INSTRUTOR:
#
#   Ordem dos bugs ao executar:
#   1. BUG 4 → FileNotFoundError (caminho 'data/' vs 'dados/')
#   2. BUG 3 → TypeError (valor string + float)
#   3. BUG 1 → ZeroDivisionError (divisão por lista vazia) *
#   4. BUG 2 → KeyError ('investimentos' não existe)
#   5. BUG 5 → Lógica invertida (resultado errado, sem exceção)
#
#   * O BUG 1 pode não disparar com os dados reais (todas as categorias
#     têm transações). Para demonstrá-lo, adicione manualmente:
#     dados['teste'] = {'total': 0.0, 'transacoes': []}
#
#   DICA: Após corrigir cada bug, execute novamente para ver o próximo!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    main()
