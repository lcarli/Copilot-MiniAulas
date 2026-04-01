# ============================================================
# Demo 01 - Primeiro contato com Python + GitHub Copilot
# ============================================================
# Este é o primeiro script da Aula 1.
# O objetivo é mostrar como o Copilot pode gerar funções
# simples a partir de comentários em linguagem natural.
#
# Instrutor: digite os comentários "Peça ao Copilot" e
# deixe o Copilot sugerir o código automaticamente!
# ============================================================


# Peça ao Copilot: "crie uma função que recebe um nome e retorna uma saudação personalizada"
def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada com o nome informado."""
    return f"Olá, {nome}! Seja bem-vindo(a) ao curso de desenvolvimento com IA! 🚀"


# Peça ao Copilot: "crie uma função que verifica se um número é par ou ímpar"
def par_ou_impar(numero: int) -> str:
    """Verifica se um número é par ou ímpar e retorna uma string descritiva."""
    if numero % 2 == 0:
        return f"O número {numero} é PAR"
    else:
        return f"O número {numero} é ÍMPAR"


# Peça ao Copilot: "crie uma função que recebe uma lista de números e retorna estatísticas"
def estatisticas(numeros: list) -> dict:
    """
    Recebe uma lista de números e retorna um dicionário com:
    - média
    - valor máximo
    - valor mínimo
    """
    if not numeros:
        return {"media": 0, "maximo": 0, "minimo": 0}

    media = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    return {
        "media": round(media, 2),
        "maximo": maximo,
        "minimo": minimo,
    }


# ============================================================
# Bloco principal — executa as demonstrações
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  DEMO 01 — Primeiro contato com o Copilot")
    print("=" * 50)

    # --- Teste da função de saudação ---
    print("\n📌 Função de saudação:")
    nomes = ["Ana", "Carlos", "Maria"]
    for nome in nomes:
        print(f"  {saudacao(nome)}")

    # --- Teste da função par ou ímpar ---
    print("\n📌 Função par ou ímpar:")
    numeros_teste = [7, 42, 13, 100, 0]
    for n in numeros_teste:
        print(f"  {par_ou_impar(n)}")

    # --- Teste da função de estatísticas ---
    print("\n📌 Função de estatísticas:")
    valores = [10, 25, 3, 47, 88, 12, 36]
    resultado = estatisticas(valores)
    print(f"  Lista: {valores}")
    print(f"  Média:  {resultado['media']}")
    print(f"  Máximo: {resultado['maximo']}")
    print(f"  Mínimo: {resultado['minimo']}")

    print("\n" + "=" * 50)
    print("  ✅ Demo 01 concluída com sucesso!")
    print("=" * 50)
