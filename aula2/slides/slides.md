# Desenvolvimento Rápido com Soluções de IA — Aula 2
## Produtividade e Projeto Final

**Curso**: Desenvolvimento Rápido com Soluções de IA
**Duração**: ~3 horas
**Pré-requisito**: Aula 1 — Fundamentos e Primeiros Passos

> Instrutor: use `---` como separador de slides ao apresentar.

---

# Agenda da Aula 2

| Bloco | Tema | Tempo |
|-------|------|-------|
| 1 | Revisão e Aquecimento | 15 min |
| 2 | IA no Ciclo de Desenvolvimento | 25 min |
| 3 | Refatoração e Debugging com Copilot | 30 min |
| 4 | Automações Bancárias Realistas | 40 min |
| 5 | Documentação e Organização | 20 min |
| 6 | Mini Projeto Final | 40 min |
| — | Encerramento | 10 min |

**Formato**: slides expositivos + demos ao vivo + lab prático
**Ferramentas**: VS Code + GitHub Copilot (Free) + Python 3.10+

---

# Recap — O que vimos na Aula 1

- **IA Generativa e LLMs**: modelos de linguagem preveem o próximo token; quanto melhor o contexto, melhor a resposta
- **Ferramentas**: GitHub Copilot, ChatGPT, Cursor, Bolt.new — cada uma com seu ponto forte
- **GitHub Copilot na prática**:
  - Completar código com `Tab`
  - Copilot Chat (`Ctrl+I`) para pedir ajuda inline
  - Prompts claros = respostas melhores
- **Python + Copilot**: lemos CSVs, manipulamos dados, criamos funções simples
- **Metodologia**: dividir o problema → pedir por partes → revisar → iterar

> A IA é uma **co-piloto** — quem dirige é você!

---

# Quick Challenge — Aquecimento

## [DEMO RÁPIDA] Validação de CPF com Copilot

**Desafio**: Peça ao Copilot para criar uma função que valida CPF.

Prompt sugerido no Copilot Chat:

```
Crie uma função Python chamada validar_cpf que recebe uma string
e retorna True se o CPF for válido (com verificação dos dígitos).
```

Resultado esperado:

```python
def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(c for c in cpf if c.isdigit())
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = (soma * 10 % 11) % 10
        if int(cpf[i]) != digito:
            return False
    return True

# Teste rápido
print(validar_cpf("529.982.247-25")) # True
print(validar_cpf("111.111.111-11")) # False
```

> Observe: o Copilot já conhece a regra de validação de CPF!

---

# Bloco 2 — IA no Ciclo de Desenvolvimento

## O Ciclo Completo de Desenvolvimento

```
  ┌──────────┐ ┌──────────────┐ ┌───────────┐ ┌───────────┐
  │ IDEAÇÃO │ ──▶ │ PROTOTIPAÇÃO │ ──▶ │ VALIDAÇÃO │ ──▶ │ ITERAÇÃO │
  └──────────┘ └──────────────┘ └───────────┘ └───────────┘
       ▲ │
       └────────────────────────────────────────────────────────┘
```

| Fase | O que acontece |
|------|---------------|
| **Ideação** | Definir o problema, pensar em soluções |
| **Prototipação** | Escrever a primeira versão funcional |
| **Validação** | Testar, verificar, garantir que funciona |
| **Iteração** | Melhorar, refatorar, adicionar funcionalidades |

> Com IA, cada fase fica **mais rápida** — mas nenhuma pode ser pulada!

---

# IA em Cada Fase do Ciclo

| Fase | Como a IA ajuda | Exemplo de prompt |
|------|----------------|-------------------|
| **Ideação** | Brainstorm de abordagens, sugerir estruturas de dados | *"Quais estruturas posso usar para organizar transações bancárias?"* |
| **Prototipação** | Gerar código funcional rapidamente, criar esqueletos | *"Crie uma função que lê um CSV e retorna um dicionário agrupado por cliente"* |
| **Validação** | Gerar testes, identificar edge cases, revisar lógica | *"Gere testes para essa função cobrindo entradas vazias e valores negativos"* |
| **Iteração** | Refatorar, otimizar, adicionar tratamento de erros | *"Refatore para usar list comprehension e adicione tratamento de exceções"* |

**Dica de ouro**: quanto mais específico o prompt, melhor o resultado.

```
 "Faça um programa de banco"
 "Crie uma função que recebe uma lista de dicionários com campos
   'valor' e 'tipo', e retorna o saldo total (créditos - débitos)"
```

---

# Estratégias para Copilot Free

O plano Free tem **limite de interações por mês**. Use com sabedoria!

### 1. Prompts curtos e diretos
```
 "Quero que você crie um sistema completo de gestão bancária com
   login, cadastro, extrato, transferência e relatórios"

 "Crie uma função calcular_saldo(transacoes) que recebe uma lista
   de dicts com 'valor' e 'tipo' e retorna o saldo"
```

### 2. Arquivos pequenos e focados
- Um arquivo por responsabilidade (ex: `leitura.py`, `calculo.py`, `relatorio.py`)
- O Copilot entende melhor arquivos com até ~100 linhas

### 3. Iterar por etapas
- Passo 1: Gere a função básica
- Passo 2: Peça para adicionar validação
- Passo 3: Peça para adicionar tratamento de erros
- Passo 4: Peça para adicionar docstring

> Dividir para conquistar — vale para código **e** para prompts!

---

# Quando a IA Ajuda vs Quando Atrapalha

| IA ajuda muito | IA pode atrapalhar |
|-------------------|----------------------|
| Gerar boilerplate e código repetitivo | Decisões de arquitetura complexas |
| Criar funções com lógica conhecida (ordenação, filtros) | Lógica de negócio muito específica da empresa |
| Gerar docstrings e comentários | Código que envolve segurança crítica (sem revisão) |
| Refatorar código existente | Otimização de performance sem contexto |
| Escrever testes unitários | Depurar problemas de infraestrutura |
| Converter entre formatos (JSON ↔ CSV ↔ dict) | Entender requisitos vagos ou ambíguos |
| Explicar código legado | Substituir o entendimento do desenvolvedor |

### Regra de ouro:

> **Use a IA para acelerar o que você já sabe fazer.**
> **Use a IA para aprender o que você ainda não sabe.**
> **Nunca use a IA para pular o que você precisa entender.**

---

# Desenvolvimento Iterativo — Passo a Passo

**Cenário**: criar uma função que classifica transações bancárias.

**Etapa 1** — Peça a versão básica:
```python
def classificar_transacao(descricao):
    categorias = {
        "supermercado": "Alimentação",
        "restaurante": "Alimentação",
        "farmácia": "Saúde",
        "combustível": "Transporte",
        "posto": "Transporte",
    }
    for palavra, categoria in categorias.items():
        if palavra in descricao.lower():
            return categoria
    return "Outros"
```

**Etapa 2** — Peça para tratar edge cases:
```python
def classificar_transacao(descricao):
    if not descricao or not isinstance(descricao, str):
        return "Não classificado"
    # ... resto da lógica
```

**Etapa 3** — Peça para tornar configurável:
```python
def classificar_transacao(descricao, mapa_categorias=None):
    if mapa_categorias is None:
        mapa_categorias = CATEGORIAS_PADRAO
    # ... lógica usando o mapa recebido
```

> Cada etapa é um prompt separado. Revise antes de seguir!

---

# Armadilhas Comuns ao Usar IA

### 1. "Copiar e colar mágico"
- Aceitar o código sem entender o que ele faz
- **Solução**: use `/explain` antes de aceitar

### 2. "Pedir o mundo de uma vez"
- Prompts enormes geram código enorme e difícil de revisar
- **Solução**: divida em funções pequenas

### 3. "Loop infinito de correções"
- Pedir para corrigir → gera novo bug → pedir para corrigir → ...
- **Solução**: pare, entenda o problema, reescreva o prompt

### 4. "Confiar demais no código gerado"
- A IA pode gerar código que funciona mas não é correto
- **Solução**: teste com dados reais e edge cases

### 5. "Ignorar a estrutura"
- Colocar tudo em um arquivo só porque a IA gerou assim
- **Solução**: organize em módulos desde o início

> A IA erra. Você revisa. Juntos, vocês produzem melhor.

---

# Bloco 3 — Refatoração e Debugging

## O que é Refatoração e Por Que Importa

**Refatoração** = melhorar a estrutura do código **sem alterar** o comportamento.

### Por que refatorar?
- **Legibilidade**: código claro é mais fácil de manter
- **Menos bugs**: código organizado = menos esconderijos para bugs
- **Reuso**: funções bem definidas podem ser usadas em outros projetos
- **Colaboração**: outras pessoas (e seu "eu do futuro") vão entender
- **Evolução**: código limpo é mais fácil de estender

### Sinais de que o código precisa de refatoração:
- Funções com mais de 20-30 linhas
- Nomes de variáveis como `x`, `temp`, `dados2`
- Código duplicado (copy-paste)
- Muitos `if/else` aninhados
- Comentários explicando o que o código faz (em vez de o código se explicar)

---

# Código Espaguete vs Código Modular

### Antes — Código Espaguete

```python
import csv

arquivo = open("transacoes.csv", "r")
leitor = csv.reader(arquivo)
next(leitor)
total_c = 0
total_d = 0
for linha in leitor:
    if linha[3] == "credito":
        total_c = total_c + float(linha[2])
    else:
        total_d = total_d + float(linha[2])
arquivo.close()
print(f"Créditos: {total_c}")
print(f"Débitos: {total_d}")
print(f"Saldo: {total_c - total_d}")
```

### Depois — Código Modular

```python
import csv

def ler_transacoes(caminho: str) -> list[dict]:
    with open(caminho, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def calcular_totais(transacoes: list[dict]) -> dict:
    creditos = sum(float(t["valor"]) for t in transacoes if t["tipo"] == "credito")
    debitos = sum(float(t["valor"]) for t in transacoes if t["tipo"] == "debito")
    return {"creditos": creditos, "debitos": debitos, "saldo": creditos - debitos}

def exibir_resumo(totais: dict) -> None:
    for chave, valor in totais.items():
        print(f"{chave.capitalize()}: R$ {valor:,.2f}")

# --- Execução ---
transacoes = ler_transacoes("transacoes.csv")
totais = calcular_totais(transacoes)
exibir_resumo(totais)
```

> Mesmo resultado, mas agora cada função pode ser testada, reutilizada e entendida separadamente.

---

# [DEMO] Refatoração com Copilot

## Arquivo: `demo01_refatoracao.py`

**O que vamos fazer:**
1. Partir de um código "espaguete" que processa transações
2. Pedir ao Copilot para refatorar passo a passo

**Prompts para a demo:**

```
Prompt 1: "Refatore este código para usar funções separadas
           para leitura, processamento e exibição"

Prompt 2: "Adicione type hints em todas as funções"

Prompt 3: "Substitua o open/close por context manager (with)"

Prompt 4: "Use csv.DictReader em vez de csv.reader"
```

**Dicas para a plateia:**
- Observe como o Copilot entende o contexto do arquivo aberto
- Cada refatoração mantém o comportamento original
- Teste após cada mudança!

```python
# Atalho útil no VS Code:
# Selecione o código → Ctrl+I → digite o prompt de refatoração
```

> Abra `aula2/demos/demo01_refatoracao.py` no VS Code

---

# Geração de Funções e Modularização

O Copilot é excelente para **extrair funções** de blocos de código.

### Prompt de extração:

```
Extraia a lógica de filtragem em uma função separada chamada
filtrar_por_tipo que recebe a lista de transações e o tipo desejado.
```

### Resultado:

```python
def filtrar_por_tipo(transacoes: list[dict], tipo: str) -> list[dict]:
    """Filtra transações pelo tipo (credito/debito)."""
    return [t for t in transacoes if t["tipo"] == tipo]

def calcular_total(transacoes: list[dict]) -> float:
    """Calcula a soma dos valores de uma lista de transações."""
    return sum(float(t["valor"]) for t in transacoes)

# Uso modular
creditos = filtrar_por_tipo(transacoes, "credito")
debitos = filtrar_por_tipo(transacoes, "debito")
saldo = calcular_total(creditos) - calcular_total(debitos)
```

### Vantagens da modularização:
- Funções pequenas e reutilizáveis
- Fácil de testar individualmente
- Nomes descritivos = documentação natural
- Composição flexível de operações

---

# Tratamento de Exceções com IA

A IA pode sugerir **tratamento de erros** para cenários comuns.

### Prompt:
```
Adicione tratamento de exceções para: arquivo não encontrado,
arquivo vazio, e valores não numéricos na coluna 'valor'.
```

### Resultado:

```python
def ler_transacoes_seguro(caminho: str) -> list[dict]:
    """Lê transações de um CSV com tratamento de erros."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            transacoes = list(csv.DictReader(f))

        if not transacoes:
            print(f" Arquivo '{caminho}' está vazio.")
            return []

        # Validar valores numéricos
        for t in transacoes:
            try:
                float(t["valor"])
            except (ValueError, KeyError):
                print(f" Transação inválida ignorada: {t}")
                transacoes.remove(t)

        return transacoes

    except FileNotFoundError:
        print(f" Arquivo '{caminho}' não encontrado.")
        return []
    except Exception as e:
        print(f" Erro inesperado: {e}")
        return []
```

> A IA sugere, mas **você decide** quais erros são relevantes para o seu caso.

---

# Debugging com Copilot

## Comandos úteis do Copilot Chat:

| Comando | O que faz | Quando usar |
|---------|-----------|-------------|
| `/explain` | Explica o código selecionado linha a linha | Quando não entende o que o código faz |
| `/fix` | Sugere correção para erros | Quando tem um bug identificado |
| `/tests` | Gera testes para o código | Para validar o comportamento |
| `@workspace` | Considera o contexto do projeto inteiro | Quando o bug envolve múltiplos arquivos |

### Fluxo de debugging com IA:

```
1. Identifique o sintoma (erro, resultado errado)
         ↓
2. Selecione o trecho suspeito
         ↓
3. Use /explain para entender a lógica
         ↓
4. Use /fix para sugerir correção
         ↓
5. Revise a sugestão criticamente
         ↓
6. Teste a correção com dados reais
```

> O Copilot sugere correções, mas nem sempre a primeira sugestão é a melhor. Leia com atenção!

---

# [DEMO] Encontrando e Corrigindo Bugs

## Arquivo: `demo02_debugging.py`

**Código com bugs propositais:**

```python
def calcular_media_transacoes(transacoes):
    total = 0
    for t in transacoes:
        total += t["valor"] # Bug 1: valor é string, não float
    media = total / len(transacoes) # Bug 2: divisão por zero se lista vazia
    return round(media) # Bug 3: round sem casas decimais

dados = [
    {"cliente": "Ana", "valor": "150.50", "tipo": "credito"},
    {"cliente": "Ana", "valor": "89.90", "tipo": "debito"},
    {"cliente": "Ana", "valor": "200.00", "tipo": "credito"},
]

print(f"Média: R$ {calcular_media_transacoes(dados)}")
print(f"Média vazia: R$ {calcular_media_transacoes([])}")
```

**Roteiro da demo:**
1. Executar o código e ver o erro
2. Selecionar a função → `/explain`
3. Pedir ao Copilot → `/fix`
4. Revisar a correção sugerida
5. Testar com dados reais e lista vazia

> Abra `aula2/demos/demo02_debugging.py` no VS Code

---

# Bloco 4 — Automações Bancárias Realistas

## O Desafio: Consolidar Dados de Múltiplos Meses

**Cenário do mundo real:**
- O banco gera um CSV de transações **por mês**
- Precisamos consolidar Jan + Fev + Mar em um relatório único
- Cada CSV tem as mesmas colunas:

```
id,data,cliente_id,cliente_nome,tipo,valor,descricao
1,2024-01-05,C001,Ana Silva,debito,150.00,Supermercado Extra
2,2024-01-07,C001,Ana Silva,credito,3500.00,Salário
```

**Arquivos disponíveis:**
- `aula2/dados/transacoes_janeiro.csv`
- `aula2/dados/transacoes_fevereiro.csv`
- `aula2/dados/transacoes_marco.csv`

**Resultado esperado:**
- Total de transações consolidadas
- Classificação por categoria
- Estatísticas por cliente
- Resumo executivo em texto

---

# Pipeline de Dados

## Ler → Consolidar → Classificar → Calcular → Reportar

```
 ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
 │ Janeiro.csv │ │ Fevereiro.csv│ │ Março.csv │
 └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
        │ │ │
        └───────────┬───────┘───────────────────┘
                    ▼
          ┌─────────────────┐
          │ CONSOLIDAR │ Juntar todos os registros
          └────────┬────────┘
                   ▼
          ┌─────────────────┐
          │ CLASSIFICAR │ Atribuir categorias
          └────────┬────────┘
                   ▼
          ┌─────────────────┐
          │ CALCULAR │ Estatísticas por cliente
          └────────┬────────┘
                   ▼
          ┌─────────────────┐
          │ REPORTAR │ Gerar resumo executivo
          └─────────────────┘
```

Cada etapa é uma **função independente** que recebe dados e retorna dados transformados.

> Esse padrão se chama **pipeline** — muito usado em engenharia de dados!

---

# [DEMO] Pipeline Completo

## Arquivo: `demo03_pipeline.py`

### Etapa 1 — Ler e Consolidar CSVs

```python
import csv
import os

def ler_csv(caminho: str) -> list[dict]:
    """Lê um arquivo CSV e retorna lista de dicionários."""
    with open(caminho, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def consolidar_csvs(diretorio: str, arquivos: list[str]) -> list[dict]:
    """Consolida múltiplos CSVs em uma única lista."""
    todas = []
    for arquivo in arquivos:
        caminho = os.path.join(diretorio, arquivo)
        transacoes = ler_csv(caminho)
        print(f" {arquivo}: {len(transacoes)} transações")
        todas.extend(transacoes)
    print(f" Total consolidado: {len(todas)} transações")
    return todas
```

> Prompt usado: *"Crie uma função que lê múltiplos CSVs de um diretório e consolida em uma única lista de dicionários"*

---

# [DEMO] Pipeline — Classificar e Calcular

### Etapa 2 — Classificar Transações

```python
CATEGORIAS = {
    "supermercado": "Alimentação", "restaurante": "Alimentação",
    "farmácia": "Saúde", "hospital": "Saúde",
    "combustível": "Transporte", "uber": "Transporte",
    "aluguel": "Moradia", "condomínio": "Moradia",
    "salário": "Receita", "freelance": "Receita",
}

def classificar(transacoes: list[dict]) -> list[dict]:
    """Adiciona campo 'categoria' a cada transação."""
    for t in transacoes:
        desc = t.get("descricao", "").lower()
        t["categoria"] = "Outros"
        for palavra, cat in CATEGORIAS.items():
            if palavra in desc:
                t["categoria"] = cat
                break
    return transacoes
```

### Etapa 3 — Estatísticas por Cliente

```python
def stats_por_cliente(transacoes: list[dict]) -> dict:
    """Calcula estatísticas agrupadas por cliente."""
    clientes = {}
    for t in transacoes:
        nome = t["cliente_nome"]
        valor = float(t["valor"])
        if nome not in clientes:
            clientes[nome] = {"creditos": 0, "debitos": 0, "qtd": 0}
        clientes[nome]["qtd"] += 1
        if t["tipo"] == "credito":
            clientes[nome]["creditos"] += valor
        else:
            clientes[nome]["debitos"] += valor
    for c in clientes.values():
        c["saldo"] = c["creditos"] - c["debitos"]
    return clientes
```

---

# [DEMO] Pipeline — Resumo Executivo

### Etapa 4 — Gerar Relatório

```python
def gerar_resumo(clientes: dict, transacoes: list[dict]) -> str:
    """Gera um resumo executivo em texto."""
    linhas = []
    linhas.append("=" * 50)
    linhas.append(" RESUMO EXECUTIVO — TRIMESTRE")
    linhas.append("=" * 50)
    linhas.append(f"\nTotal de transações: {len(transacoes)}")
    linhas.append(f"Clientes ativos: {len(clientes)}")

    linhas.append("\n--- Por Cliente ---")
    for nome, dados in sorted(clientes.items()):
        linhas.append(f"\n {nome}:")
        linhas.append(f" Transações: {dados['qtd']}")
        linhas.append(f" Créditos: R$ {dados['creditos']:>10,.2f}")
        linhas.append(f" Débitos: R$ {dados['debitos']:>10,.2f}")
        linhas.append(f" Saldo: R$ {dados['saldo']:>10,.2f}")

    linhas.append("\n" + "=" * 50)
    return "\n".join(linhas)

# --- Pipeline completo ---
arquivos = ["transacoes_janeiro.csv", "transacoes_fevereiro.csv",
            "transacoes_marco.csv"]
dados = consolidar_csvs("aula2/dados", arquivos)
dados = classificar(dados)
clientes = stats_por_cliente(dados)
print(gerar_resumo(clientes, dados))
```

> Abra `aula2/demos/demo03_pipeline.py` no VS Code

---

# Validação de Dados e Tratamento de Erros

Dados do mundo real são **sujos**. Sempre valide!

```python
def validar_transacao(t: dict) -> tuple[bool, str]:
    """Valida uma transação e retorna (válida, motivo)."""
    campos_obrigatorios = ["data", "cliente_nome", "tipo", "valor"]
    for campo in campos_obrigatorios:
        if campo not in t or not t[campo]:
            return False, f"Campo '{campo}' ausente ou vazio"

    try:
        valor = float(t["valor"])
        if valor < 0:
            return False, "Valor negativo"
    except ValueError:
        return False, f"Valor não numérico: {t['valor']}"

    if t["tipo"] not in ("credito", "debito"):
        return False, f"Tipo inválido: {t['tipo']}"

    return True, "OK"

def filtrar_validas(transacoes: list[dict]) -> list[dict]:
    """Retorna apenas transações válidas, logando as inválidas."""
    validas = []
    for t in transacoes:
        ok, motivo = validar_transacao(t)
        if ok:
            validas.append(t)
        else:
            print(f" Transação ignorada (linha {t.get('id', '?')}): {motivo}")
    return validas
```

> Prompt: *"Crie validação para cada campo da transação, retornando motivo do erro"*

---

# Relatórios Automatizados

Gere relatórios em diferentes formatos com IA:

### Prompt:
```
Crie uma função que gera um relatório em formato texto/CSV
com totais por categoria e por mês.
```

```python
def relatorio_por_categoria(transacoes: list[dict]) -> str:
    """Gera relatório agrupado por categoria."""
    categorias = {}
    for t in transacoes:
        cat = t.get("categoria", "Outros")
        if cat not in categorias:
            categorias[cat] = {"total": 0.0, "qtd": 0}
        categorias[cat]["total"] += float(t["valor"])
        categorias[cat]["qtd"] += 1

    linhas = ["Categoria,Quantidade,Total (R$)"]
    for cat, dados in sorted(categorias.items()):
        linhas.append(f"{cat},{dados['qtd']},{dados['total']:.2f}")
    return "\n".join(linhas)

def salvar_relatorio(conteudo: str, caminho: str) -> None:
    """Salva o relatório em um arquivo."""
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f" Relatório salvo em: {caminho}")
```

> Relatórios em CSV podem ser abertos no Excel — ótimo para compartilhar com gestores!

---

# Organização em Funções Reutilizáveis

### O pipeline completo, organizado:

```python
# main.py — orquestração do pipeline

from leitura import ler_csv, consolidar_csvs
from processamento import classificar, validar_transacoes
from calculo import stats_por_cliente, stats_por_categoria
from relatorio import gerar_resumo, salvar_relatorio

def main():
    # 1. Leitura
    arquivos = ["transacoes_janeiro.csv", "transacoes_fevereiro.csv",
                "transacoes_marco.csv"]
    dados = consolidar_csvs("dados", arquivos)

    # 2. Validação e classificação
    dados = validar_transacoes(dados)
    dados = classificar(dados)

    # 3. Cálculos
    por_cliente = stats_por_cliente(dados)
    por_categoria = stats_por_categoria(dados)

    # 4. Relatório
    resumo = gerar_resumo(por_cliente, por_categoria, dados)
    print(resumo)
    salvar_relatorio(resumo, "relatorio_trimestral.txt")

if __name__ == "__main__":
    main()
```

> Cada módulo (`leitura.py`, `processamento.py`, etc.) tem uma responsabilidade clara.

---

# Bloco 5 — Documentação e Organização

## Por Que Documentar?

### Para o "eu do futuro"
```python
# Você daqui a 3 meses olhando seu próprio código:
# "O que eu estava pensando quando escrevi isso?!"
```

### Para a equipe
- Novos membros entendem o projeto mais rápido
- Menos perguntas = mais produtividade
- Menos dependência de uma única pessoa

### O que documentar:
| O quê | Como | Onde |
|-------|------|------|
| O que a função faz | Docstring | Dentro da função |
| Como usar o projeto | README.md | Raiz do projeto |
| Decisões técnicas | Comentários | No código |
| Como instalar e rodar | README.md | Raiz do projeto |

> Código bom se auto-documenta. Documentação explica o **porquê**, não o **como**.

---

# Docstrings em Python

### Formato recomendado (Google Style):

```python
def calcular_saldo(transacoes: list[dict], tipo: str = None) -> float:
    """Calcula o saldo total das transações.

    Soma os valores de crédito e subtrai os de débito.
    Opcionalmente filtra por tipo antes de calcular.

    Args:
        transacoes: Lista de dicts com chaves 'valor' e 'tipo'.
        tipo: Se informado, filtra apenas transações desse tipo.

    Returns:
        Saldo total como float.

    Raises:
        ValueError: Se alguma transação tiver valor não numérico.

    Example:
        >>> dados = [{"valor": "100", "tipo": "credito"}]
        >>> calcular_saldo(dados)
        100.0
    """
    if tipo:
        transacoes = [t for t in transacoes if t["tipo"] == tipo]
    return sum(float(t["valor"]) for t in transacoes)
```

### Seções da docstring:
- **Resumo**: primeira linha, breve
- **Descrição**: detalhes adicionais
- **Args**: parâmetros e seus tipos
- **Returns**: o que retorna
- **Raises**: exceções possíveis
- **Example**: exemplo de uso

---

# [DEMO] Gerar Docstrings e README com Copilot

## Arquivo: `demo04_documentacao.py`

### Gerando docstrings automaticamente:

**Prompt no Copilot Chat:**
```
Gere docstrings no formato Google Style para todas as funções
deste arquivo. Inclua Args, Returns e Example.
```

### Gerando README.md do projeto:

**Prompt:**
```
Gere um README.md para este projeto Python que:
- Explica o que o projeto faz
- Lista os pré-requisitos
- Mostra como instalar e rodar
- Descreve a estrutura de pastas
- Inclui exemplos de uso
```

### Dicas:
- Selecione a função → `Ctrl+I` → *"Adicione docstring"*
- O Copilot entende o contexto e gera documentação relevante
- Sempre revise: a IA pode inventar detalhes incorretos

> Abra `aula2/demos/demo04_documentacao.py` no VS Code

---

# Organização de Projeto Python

### Estrutura recomendada para projetos simples:

```
meu_projeto/
├── README.md # Documentação principal
├── requirements.txt # Dependências (pip freeze)
├── main.py # Ponto de entrada
├── dados/ # Arquivos de dados (CSV, JSON)
│ ├── transacoes_jan.csv
│ ├── transacoes_fev.csv
│ └── transacoes_mar.csv
├── src/ # Código-fonte organizado
│ ├── leitura.py # Funções de leitura de dados
│ ├── processamento.py # Lógica de negócio
│ ├── calculo.py # Funções de cálculo
│ └── relatorio.py # Geração de relatórios
├── testes/ # Testes (quando houver)
│ └── test_calculo.py
└── saida/ # Relatórios gerados
    └── relatorio.txt
```

### Boas práticas:
- Um módulo por responsabilidade
- Separar dados de código
- README na raiz sempre
- Não versionar dados sensíveis (use `.gitignore`)
- Listar dependências no `requirements.txt`

---

# Versionamento com Git — Menção Rápida

### Por que usar Git?
- **Histórico**: volte a qualquer versão anterior
- **Colaboração**: trabalhe em equipe sem conflitos
- **Segurança**: backup do código na nuvem (GitHub)

### Comandos essenciais:

```bash
# Iniciar um repositório
git init

# Ver o que mudou
git status

# Adicionar arquivos para commit
git add .

# Salvar uma versão
git commit -m "Adiciona pipeline de consolidação de transações"

# Enviar para o GitHub
git push origin main
```

### O que colocar no `.gitignore`:
```
# Arquivos que NÃO devem ir para o repositório
__pycache__/
*.pyc
.env
dados/sensivel/
saida/
```

> O Copilot pode ajudar a gerar `.gitignore` e mensagens de commit!

---

# Bloco 6 — Mini Projeto Final

## Escolha Seu Cenário!

### Opção A — Relatório Mensal de Gastos por Categoria
- Ler os 3 CSVs de transações
- Classificar cada transação por categoria
- Gerar relatório com total gasto por categoria
- Identificar a categoria com maior gasto

### Opção B — Detector de Transações Suspeitas
- Ler os 3 CSVs de transações
- Definir um threshold (ex: R$ 5.000)
- Listar transações acima do threshold
- Gerar alerta com detalhes da transação suspeita

### Opção C — Resumo Executivo para Gerente
- Consolidar os 3 CSVs
- Calcular: total de créditos, débitos e saldo por cliente
- Identificar o cliente mais ativo e o de maior saldo
- Gerar um relatório formatado em texto

> Todos os cenários usam os mesmos CSVs de `aula2/dados/`

---

# Metodologia: Pensar → Dividir → Pedir → Revisar → Testar

```
 ┌──────────┐
 │ PENSAR │ Entenda o problema antes de escrever código
 └────┬─────┘
      ▼
 ┌──────────┐
 │ DIVIDIR │ Quebre em funções pequenas (3-5 funções)
 └────┬─────┘
      ▼
 ┌──────────┐
 │ PEDIR │ Use o Copilot para cada função separadamente
 └────┬─────┘
      ▼
 ┌──────────┐
 │ REVISAR │ Leia o código gerado, entenda, ajuste
 └────┬─────┘
      ▼
 ┌──────────┐
 │ TESTAR │ Execute com dados reais, teste edge cases
 └──────────┘
```

### Exemplo de divisão (Opção A):
1. `ler_e_consolidar(arquivos)` → retorna lista de transações
2. `classificar_transacoes(transacoes)` → adiciona categorias
3. `calcular_por_categoria(transacoes)` → retorna totais por categoria
4. `encontrar_maior_gasto(totais)` → retorna a categoria top
5. `gerar_relatorio(totais, maior)` → imprime relatório formatado

---

# Dicas para o Projeto

### Comece simples e evolua:
1. **Primeiro**: faça funcionar com 1 CSV
2. **Depois**: expanda para os 3 CSVs
3. **Então**: adicione classificação/cálculos
4. **Por fim**: gere o relatório

### Prompts úteis:
```
"Crie uma função que lê um CSV e retorna lista de dicionários"

"Crie uma função que classifica uma transação por categoria
 baseado na descrição"

"Crie uma função que calcula o total por categoria a partir
 de uma lista de transações classificadas"

"Gere um relatório formatado mostrando gastos por categoria
 ordenados do maior para o menor"
```

### Se travar:
- Releia o erro com calma
- Use `/explain` no código que não entendeu
- Use `/fix` se tiver um bug
- Peça ajuda ao instrutor

---

# Checklist de Entrega

Antes de considerar seu projeto pronto, verifique:

### Funcionalidade
- [ ] Lê os 3 arquivos CSV corretamente
- [ ] Processa os dados sem erros
- [ ] Gera o resultado esperado (relatório/alerta/resumo)
- [ ] Funciona mesmo com dados inesperados (tratamento de erros)

### Qualidade do Código
- [ ] Código organizado em funções (mínimo 3 funções)
- [ ] Nomes de variáveis e funções descritivos
- [ ] Pelo menos uma docstring no código
- [ ] Sem código comentado/morto

### Boas Práticas
- [ ] Usa `with` para abrir arquivos
- [ ] Usa `csv.DictReader` para ler CSVs
- [ ] Trata pelo menos um tipo de exceção
- [ ] Código roda sem modificações (caminho dos arquivos correto)

> Bônus: salvar o relatório em arquivo `.txt` ou `.csv`

---

# [LAB] Mãos à Obra!

## Tempo: 40 minutos

### Instruções:
1. Escolha um cenário (A, B ou C)
2. Crie um novo arquivo em `aula2/labs/` (ex: `projeto_opcaoA.py`)
3. Use a metodologia: Pensar → Dividir → Pedir → Revisar → Testar
4. Use os CSVs de `aula2/dados/`
5. Confira o checklist antes de finalizar

### Estrutura sugerida do arquivo:

```python
"""
Mini Projeto Final — Opção [A/B/C]
Curso: Desenvolvimento Rápido com Soluções de IA
"""
import csv
import os

# --- Funções de Leitura ---
# ... suas funções aqui ...

# --- Funções de Processamento ---
# ... suas funções aqui ...

# --- Funções de Relatório ---
# ... suas funções aqui ...

# --- Execução Principal ---
if __name__ == "__main__":
    # Orquestrar o pipeline
    pass
```

> O instrutor estará disponível para ajudar!

---

# Recap Completo do Curso

## Aula 1 — Fundamentos e Primeiros Passos

- O que é IA generativa e como funcionam LLMs
- Panorama de ferramentas (Copilot, ChatGPT, Cursor...)
- GitHub Copilot: instalação, configuração, primeiros prompts
- Python básico: variáveis, funções, listas, dicionários
- Leitura de CSVs e manipulação de dados bancários

## Aula 2 — Produtividade e Projeto Final

- Ciclo de desenvolvimento com IA (Ideação → Iteração)
- Estratégias para usar Copilot Free de forma eficiente
- Refatoração: código espaguete → código modular
- Debugging assistido: `/explain`, `/fix`, `/tests`
- Pipeline de dados: ler → consolidar → classificar → calcular → reportar
- Documentação: docstrings, README, organização de projeto
- Mini projeto: aplicação prática de tudo que aprendemos

> Vocês saíram de "o que é IA?" para "construí um pipeline de dados com IA"!

---

# Próximos Passos — Como Continuar Aprendendo

### Curto prazo (próximas semanas):
- Refaça os exercícios sem olhar o material
- Crie um mini projeto pessoal usando Copilot
- Explore a documentação oficial do Python

### Médio prazo (próximos meses):
- Aprenda bibliotecas: **Pandas** (dados), **Flask** (web), **Pytest** (testes)
- Explore outras IAs: ChatGPT para planejamento, Cursor para projetos maiores
- Aprofunde em **Git e GitHub** — essencial para qualquer desenvolvedor

### Longo prazo (próximo ano):
- Participe de projetos open source
- Explore áreas: automação, APIs, ciência de dados
- Faça cursos complementares (FreeCodeCamp, roadmap.sh)

> A melhor forma de aprender é **construindo projetos reais**.

---

# Recursos e Links Úteis

### GitHub Copilot
- [Documentação Oficial](https://docs.github.com/pt/copilot) — Guia completo em PT-BR
- [Plano Free](https://docs.github.com/pt/copilot/about-github-copilot/subscription-plans-for-github-copilot) — O que está incluso
- [Dicas de Uso](https://docs.github.com/pt/copilot/getting-started) — Boas práticas

### Python
- [Tutorial Oficial (PT-BR)](https://docs.python.org/pt-br/3/tutorial/index.html)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/) — Referência rápida
- [Documentação do módulo csv](https://docs.python.org/pt-br/3/library/csv.html)

### Aprendizado Contínuo
- [GitHub Skills](https://skills.github.com/) — Cursos interativos gratuitos
- [FreeCodeCamp](https://www.freecodecamp.org/) — Trilhas completas
- [Roadmap.sh — Python](https://roadmap.sh/python) — Caminho de aprendizado
- [Prompt Engineering Guide](https://www.promptingguide.ai/pt) — Em português

### Referência Completa
- Consulte `recursos/links_uteis.md` neste repositório

> Obrigado por participar! Bom aprendizado!
