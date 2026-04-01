# Desenvolvimento Rápido com Soluções de IA — Aula 1

### Bem-vindos ao curso!

**Instrutor**: [Nome do Instrutor]
**Duração**: ~3 horas (com intervalos)
**Público**: Iniciantes com base em lógica de programação e banco de dados

> _"A IA não substitui o desenvolvedor — ela amplifica o que ele já sabe fazer."_

---

# Agenda da Aula 1

| Bloco | Tema | Tempo |
|-------|------|-------|
| 1 | Abertura e Contexto | 25 min |
| 2 | Fundamentos de LLMs | 30 min |
| 3 | Panorama de Ferramentas | 20 min |
| 4 | GitHub Copilot na Prática | 30 min |
| 5 | Python + Copilot: Automação Bancária | 35 min |
| 6 | Lab Prático | 30 min |

**Objetivo**: Sair desta aula usando IA para escrever código Python real, com confiança e senso crítico.

---

# O que é Desenvolvimento Assistido por IA?

É o uso de ferramentas de inteligência artificial como **parceiras** no processo de desenvolvimento de software.

- A IA **sugere** código enquanto você digita
- A IA **explica** trechos de código que você não entende
- A IA **gera** testes, documentação e até consultas SQL
- A IA **encontra** bugs e sugere correções

### Analogia simples

> Pense em um **co-piloto** num avião: ele ajuda, sugere rotas e monitora instrumentos — mas o **piloto** (você) toma as decisões e mantém o controle.

**Você continua sendo o responsável pelo código.** A IA é uma ferramenta poderosa, mas não infalível.

---

# Impacto da IA no Mercado de Trabalho

### Dados reais que importam:

- **GitHub Survey 2023**: desenvolvedores completam tarefas **55% mais rápido** com Copilot
- **Stack Overflow Developer Survey 2024**: **76% dos desenvolvedores** já usam ou planejam usar ferramentas de IA
- **McKinsey 2024**: IA generativa pode automatizar até **30% das horas de trabalho** em engenharia de software
- **GitHub**: desenvolvedores relatam **74% menos frustração** em tarefas repetitivas

### O que isso significa para você?

- Não é sobre **perder empregos** — é sobre **mudar a forma de trabalhar**
- Quem souber usar IA bem terá **vantagem competitiva**
- Habilidades como **pensamento crítico** e **revisão de código** ficam ainda mais importantes

---

# O que a IA já faz hoje no desenvolvimento

### Gerar código
> Você descreve o que quer em português, a IA escreve o código

### Documentar
> A IA lê seu código e gera docstrings, READMEs e comentários explicativos

### Debugar
> Cole um erro e pergunte: "o que está errado?" — a IA analisa e sugere correção

### Criar testes
> A IA gera testes unitários automaticamente a partir do seu código

### Refatorar
> A IA sugere versões mais limpas e eficientes do seu código

### Explicar código legado
> Código antigo que ninguém entende? A IA traduz para linguagem humana

---

# Pergunta para Engajamento

## Quem já usou IA para alguma tarefa?

- Pode ser **ChatGPT**, **Copilot**, **Gemini**, **Claude** ou qualquer outra
- Não precisa ser para programação!

### Exemplos comuns:
- Pedir para resumir um texto
- Gerar um e-mail profissional
- Tirar dúvidas de programação
- Pedir ajuda com Excel ou SQL

> _Levante a mão ou escreva no chat!_

---

# O que é um LLM — Large Language Model

### Modelo de Linguagem de Grande Escala

Um LLM é um programa de computador treinado com **bilhões de textos** (livros, sites, código, documentação) para entender e gerar linguagem.

### Analogia: autocomplete turbinado

- O **autocomplete do celular** prevê a próxima **palavra**
- Um **LLM** prevê os próximos **parágrafos inteiros**, com lógica e coerência
- Ele não "entende" como um humano — ele calcula **probabilidades** do que vem a seguir

### Exemplos de LLMs:

| Modelo | Empresa | Uso comum |
|--------|---------|-----------|
| GPT-4o | OpenAI | ChatGPT, Copilot |
| Claude | Anthropic | Análise de texto, código |
| Gemini | Google | Buscas, assistente |
| Llama | Meta | Código aberto |

---

# Como funciona: Previsão do Próximo Token

O LLM funciona como uma máquina de **prever a próxima peça** do texto:

```
Entrada: "def calcular_total(valores):"
                    ↓
LLM analisa o contexto e os padrões que aprendeu
                    ↓
Previsão: " return sum(valores)"
```

### Passo a passo simplificado:

1. Você escreve algo (um **prompt**)
2. O modelo **analisa** todas as palavras/tokens do prompt
3. Ele calcula: _"qual é a próxima palavra mais provável?"_
4. Gera um token, adiciona ao contexto, e repete
5. O processo continua até completar a resposta

> Ele **não consulta** uma base de dados — ele usa **padrões estatísticos** aprendidos no treinamento.

---

# Conceito de Token

### O que é um Token?

Token é a **menor unidade de texto** que o LLM processa. Não é exatamente uma palavra — pode ser um pedaço de palavra, um símbolo ou um espaço.

### Exemplos práticos:

| Texto | Tokens aproximados |
|-------|-------------------|
| `"Olá"` | 1 token |
| `"Olá, mundo!"` | 4 tokens |
| `"Desenvolvimento"` | 2-3 tokens |
| Uma linha de Python | 5-15 tokens |
| Um arquivo de 100 linhas | ~500-1000 tokens |

### Por que isso importa?

- LLMs têm **limite de tokens** que conseguem processar (janela de contexto)
- GPT-4o: ~128.000 tokens (~300 páginas de texto)
- **Quanto mais contexto você dá**, mais tokens gasta
- Código muito longo pode **estourar o limite** e a IA "esquece" o início

---

# Arquitetura de Interação com LLMs

Toda conversa com um LLM segue esta estrutura:

```
┌─────────────────────────────────────────┐
│ SYSTEM PROMPT │
│ (Define o comportamento da IA) │
│ Ex: "Você é um assistente de Python" │
├─────────────────────────────────────────┤
│ USER PROMPT │
│ (Seu pedido / pergunta) │
│ Ex: "Crie uma função que soma lista" │
├─────────────────────────────────────────┤
│ RESPOSTA DA IA │
│ (O que o modelo gera) │
│ Ex: "def somar(lista): return sum..." │
└─────────────────────────────────────────┘
```

- **System Prompt**: instruções "invisíveis" que definem como a IA se comporta
- **User Prompt**: o que **você** escreve — sua pergunta ou comando
- **Resposta**: o que a IA gera com base nos dois anteriores

> No GitHub Copilot, o **System Prompt** já vem configurado para ajudar com código!

---

# O que é Contexto e por que importa

### Contexto = tudo que a IA "enxerga" para gerar sua resposta

No GitHub Copilot, o contexto inclui:
- O **arquivo** que você está editando
- **Arquivos abertos** em outras abas
- **Comentários** no código
- O **nome do arquivo** (ex: `calcular_juros.py` dá dica do que você quer)

### Janela de contexto

```
┌────────────────────────────────────────────┐
│ IA lembra ←──── JANELA DE CONTEXTO ────→ │
│ [início da conversa ... mensagens ... fim] │
│ │
│ Se a conversa for muito longa, │
│ o INÍCIO é "esquecido" pela IA │
└────────────────────────────────────────────┘
```

### Dica prática:
- Mantenha conversas **curtas e focadas**
- Se mudar de assunto, comece um **novo chat**
- Dê **nomes descritivos** aos seus arquivos e variáveis

---

# Como a IA gera código

### Passo a passo simplificado:

1. **Você escreve um comentário ou prompt**
   ```python
   # Função que calcula o saldo médio de uma lista de contas
   ```

2. **A IA analisa o contexto**
   - Linguagem: Python
   - Objetivo: calcular saldo médio
   - Estrutura esperada: função com parâmetro lista

3. **A IA gera o código token por token**
   ```python
   def calcular_saldo_medio(contas):
       if not contas:
           return 0
       total = sum(conta['saldo'] for conta in contas)
       return total / len(contas)
   ```

4. **Você revisa e aceita (ou ajusta)**

> A IA gera código **estatisticamente provável**, não **logicamente garantido**. Sempre revise!

---

# Limitações dos LLMs

### Alucinação
A IA **inventa** informações que parecem reais mas são falsas.
- Pode citar bibliotecas que **não existem**
- Pode gerar funções com **parâmetros inventados**
- Pode afirmar coisas com **total confiança** mesmo estando errada

### Contexto limitado
- Se a conversa é longa, a IA **esquece o início**
- Arquivos muito grandes podem **não caber** na janela de contexto

### Dependência de clareza no prompt
- Prompt vago = resposta vaga
- Prompt ambíguo = resposta imprevisível
- A IA não lê sua mente — ela lê seu **texto**

### Dados de treinamento
- O modelo tem uma **data de corte** — não sabe de novidades recentes
- Pode sugerir código com **práticas desatualizadas**

> **Regra de ouro**: nunca confie cegamente na IA. Sempre revise, teste e valide.

---

# Exemplo: Mesmo Pedido, Prompts Diferentes

### Prompt vago:
> "Faz uma função de banco"

Resultado provável: código genérico, incompleto, sem clareza do que fazer.

### Prompt específico:
> "Crie uma função Python que recebe uma lista de dicionários com campos 'cliente' e 'saldo', e retorna apenas os clientes com saldo negativo, ordenados do mais negativo para o menos negativo."

```python
def clientes_saldo_negativo(contas):
    negativos = [c for c in contas if c['saldo'] < 0]
    return sorted(negativos, key=lambda c: c['saldo'])

# Exemplo de uso
contas = [
    {'cliente': 'Ana', 'saldo': -500},
    {'cliente': 'João', 'saldo': 1200},
    {'cliente': 'Maria', 'saldo': -150},
]

print(clientes_saldo_negativo(contas))
# [{'cliente': 'Ana', 'saldo': -500}, {'cliente': 'Maria', 'saldo': -150}]
```

> **A qualidade da resposta depende diretamente da qualidade do seu prompt.**

---

# Mapa de Ferramentas de IA para Desenvolvimento

```
┌─────────────────────────────────────────────────────────────┐
│ FERRAMENTAS DE IA PARA DEVs │
├──────────────────────┬──────────────────────────────────────┤
│ FORA DA IDE │ DENTRO DA IDE │
│ │ │
│ • ChatGPT │ • GitHub Copilot (VS Code) │
│ • Claude │ • Cursor (IDE completa com IA) │
│ • Gemini │ • Cody (Sourcegraph) │
│ • Perplexity │ • Amazon CodeWhisperer │
├──────────────────────┼──────────────────────────────────────┤
│ PROTOTIPAÇÃO │ ESPECIALISTAS │
│ │ │
│ • GitHub Spark │ • GitHub Copilot Agent Mode │
│ • Lovable │ • Copilot Workspace │
│ • Bolt.new │ • Devin (agente autônomo) │
│ • V0 (Vercel) │ │
└──────────────────────┴──────────────────────────────────────┘
```

---

# ChatGPT — Uso Conversacional

### O que é?
Interface de chat da OpenAI para conversar com os modelos GPT.

### Quando usar para desenvolvimento:
- **Tirar dúvidas conceituais**: "O que é uma API REST?"
- **Planejar arquitetura**: "Como estruturo um sistema de pagamentos?"
- **Debugar erros**: cole o erro e peça explicação
- **Gerar documentação**: "Documente esta função"
- **Aprender conceitos novos**: "Explique decorators em Python"

### Exemplo prático:
> **Você**: "Explique o que faz este código SQL e sugira melhorias"
>
> **ChatGPT**: analisa, explica linha a linha e sugere índices, joins otimizados etc.

### Limitações:
- Não tem acesso ao seu código automaticamente (precisa colar)
- Não executa código (a menos que use o Code Interpreter)
- Respostas podem ficar desatualizadas

---

# GitHub Copilot — Assistente dentro do Editor

### O que é?
Uma extensão do **VS Code** (e outros editores) que usa IA para sugerir código **em tempo real**, direto no editor.

### Diferencial:
- Funciona **enquanto você digita** — sem trocar de janela
- Entende o **contexto do seu projeto** (arquivos abertos, linguagem, padrões)
- Integração nativa com o **fluxo de trabalho** do desenvolvedor

### O que ele faz:
- **Autocomplete inteligente**: completa linhas e funções inteiras
- **Chat inline**: pergunte no editor e receba respostas
- **Comandos rápidos**: `/explain`, `/fix`, `/tests`, `/doc`
- **Agent Mode**: executa tarefas complexas de múltiplos passos

> **Foco desta aula**: vamos aprender a usar o Copilot na prática!

---

# Outras Ferramentas de IA

### Cursor
- IDE completa baseada no VS Code, com IA integrada nativamente
- Chat, autocomplete e edição multi-arquivo com IA
- Ideal para quem quer IA como parte central do fluxo

### GitHub Spark
- Ferramenta para criar micro-aplicações rapidamente
- Descreva o que quer em linguagem natural
- Gera apps funcionais sem escrever código

### Lovable / Bolt.new / V0
- Ferramentas para gerar **interfaces visuais** com IA
- Descreva a tela e a IA cria o frontend
- Ideal para **prototipação rápida**
- V0 (Vercel): gera componentes React/Next.js

> Cada ferramenta tem seu ponto forte. O segredo é saber **quando usar cada uma**.

---

# Dentro vs Fora da IDE — Quando usar cada abordagem

| Critério | Fora da IDE (ChatGPT, Claude) | Dentro da IDE (Copilot) |
|----------|-------------------------------|------------------------|
| **Melhor para** | Dúvidas conceituais, planejamento | Escrever código, refatorar |
| **Contexto** | Você precisa colar o código | Acessa seus arquivos automaticamente |
| **Velocidade** | Troca de janela, copia e cola | Sugestões em tempo real |
| **Fluxo** | Interrompe o fluxo de trabalho | Integrado ao fluxo |
| **Tarefas complexas** | Explicações longas, arquitetura | Implementação, testes, debug |
| **Aprendizado** | Ótimo para entender conceitos | Ótimo para praticar |

### Recomendação:

- **Planejou?** → Use ChatGPT/Claude para pensar e estruturar
- **Codou?** → Use Copilot para implementar e testar
- **Dúvida rápida?** → Copilot Chat no VS Code mesmo

> Use **as duas abordagens** de forma complementar!

---

# O que é o GitHub Copilot

### Seu assistente de programação com IA

GitHub Copilot é uma ferramenta criada pelo **GitHub** (Microsoft) que usa modelos de IA para ajudar desenvolvedores a escrever código mais rápido e com mais qualidade.

### Como funciona:
1. Você escreve código ou comentários no VS Code
2. O Copilot **analisa o contexto** (arquivo atual, abas abertas, linguagem)
3. Ele **sugere** código em texto cinza (ghost text)
4. Você pressiona `Tab` para aceitar ou continua digitando para ignorar

### Não é magia — é estatística!
- Treinado com código open-source do GitHub
- Usa modelos da OpenAI (GPT-4o, Claude e outros)
- Quanto melhor o contexto que você dá, melhor a sugestão

> Pense no Copilot como um **programador júnior muito rápido**: produz bastante, mas você precisa **revisar tudo**.

---

# Plano Free: O que está incluso

### GitHub Copilot Free — Disponível para todos!

| Recurso | Limite mensal |
|---------|---------------|
| Completions (autocomplete) | 2.000 por mês |
| Mensagens no Copilot Chat | 50 por mês |
| Modelos disponíveis | GPT-4o, Claude 3.5 Sonnet |
| Acesso ao Agent Mode | Limitado |

### Como ativar:
1. Tenha uma **conta no GitHub** (gratuita)
2. Acesse [github.com/settings/copilot](https://github.com/settings/copilot)
3. Ative o plano **Free**
4. Instale a extensão no VS Code

### Para estudantes:
- **GitHub Student Developer Pack**: Copilot **Pro gratuito**!
- Basta comprovar vínculo com instituição de ensino

> 2.000 completions é suficiente para aprender e praticar bastante!

---

# Como Instalar: Passo a Passo com VS Code

### Pré-requisitos:
- VS Code instalado
- Conta no GitHub criada
- Plano Copilot ativado (Free ou Pro)

### Instalação:

1. Abra o **VS Code**
2. Vá em **Extensions** (Ctrl+Shift+X)
3. Pesquise **"GitHub Copilot"**
4. Clique em **Install** na extensão oficial (ícone do Copilot)
5. Faça **login** com sua conta do GitHub quando solicitado
6. Confirme as permissões

### Verificando se funcionou:
- Ícone do Copilot aparece na **barra de status** (canto inferior)
- Abra um arquivo `.py` e comece a digitar — sugestões devem aparecer em cinza

> _[O instrutor mostrará cada passo ao vivo na tela]_

---

# Features Principais do GitHub Copilot

### Autocomplete (Ghost Text)
- Sugestões aparecem em **texto cinza** enquanto você digita
- `Tab` para aceitar | `Esc` para rejeitar
- `Alt+]` e `Alt+[` para navegar entre sugestões alternativas

### Copilot Chat (Ctrl+Shift+I)
- Chat integrado no VS Code
- Pergunte em **português** sobre código, erros, conceitos

### Comandos rápidos no Chat:
| Comando | O que faz |
|---------|-----------|
| `/explain` | Explica o código selecionado |
| `/fix` | Sugere correção para erros |
| `/tests` | Gera testes para o código |
| `/doc` | Gera documentação |

### Agent Mode
- O Copilot executa tarefas de múltiplos passos
- Pode criar arquivos, executar comandos, corrigir erros em loop

---

# Boas Práticas de Prompting para Copilot

### 1. Pedidos pequenos e específicos
```python
# Ruim: "Faz o sistema bancário"
# Bom: "Função que calcula juros compostos dado capital, taxa e período"
```

### 2. Instruções claras
```python
# Ruim: "Processa os dados"
# Bom: "Leia o arquivo CSV, filtre linhas onde saldo < 0, ordene por nome"
```

### 3. Especifique o formato de saída
```python
# Retorne um dicionário com as chaves: 'total', 'media', 'maior', 'menor'
```

### 4. Dê contexto com comentários
```python
# Este módulo trata de operações bancárias para contas correntes
# Todos os valores monetários são em BRL (reais)
# Taxas devem ser expressas em porcentagem (ex: 2.5 = 2.5%)
```

> **Lembre-se**: o Copilot lê seus comentários como instruções. Comente bem!

---

# Metodologia: Copilot Assisted Development

### 5 passos para usar IA de forma eficiente:

```
  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
  │ PENSAR │ → │ DIVIDIR │ → │ PEDIR │ → │ REVISAR │ → │ TESTAR │
  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘
```

1. ** Pensar**: Entenda o problema antes de pedir ajuda à IA
2. ** Dividir**: Quebre em tarefas menores (funções, módulos, etapas)
3. ** Pedir**: Escreva prompts claros e específicos para cada parte
4. ** Revisar**: Leia o código gerado — ele faz o que você esperava?
5. ** Testar**: Execute, teste com dados reais e de borda

### Por que funciona:
- Evita o erro de pedir "tudo de uma vez"
- Cada pedaço é mais fácil de revisar
- Bugs ficam isolados e mais fáceis de encontrar

> _"Não peça um sistema. Peça uma função por vez."_

---

# [DEMO] Hora da Demo!

## `demo01_hello_copilot.py`

### O que vamos fazer:
1. Criar um arquivo Python do zero
2. Escrever um comentário descrevendo o que queremos
3. Ver o Copilot sugerir o código automaticamente
4. Aceitar, ajustar e executar

### O que observar:
- Como as sugestões aparecem em **texto cinza**
- Como o **nome do arquivo** influencia as sugestões
- Como **comentários** guiam a IA
- Como aceitar (`Tab`) e rejeitar (`Esc`) sugestões

### Exemplo que será demonstrado:

```python
# Programa que pede o nome do usuário e exibe uma
# saudação personalizada com a data e hora atual
```

> _Acompanhe a tela do instrutor!_

---

# Por que Python para Automação?

### Python é a linguagem ideal para automação porque:

- **Sintaxe simples**: parece pseudocódigo, fácil de ler e escrever
- **Bibliotecas poderosas**: `csv`, `pandas`, `openpyxl`, `os`, `json`
- **Produtividade**: menos código para fazer mais
- **IA adora Python**: é a linguagem com mais exemplos de treinamento

### Exemplos de automação no dia a dia bancário:

| Tarefa manual | Automação com Python |
|---------------|---------------------|
| Abrir planilha, filtrar dados | Script lê CSV e filtra automaticamente |
| Conferir saldos um por um | Loop valida todos em segundos |
| Gerar relatório mensal | Script gera relatório formatado |
| Enviar e-mails de cobrança | Automação envia para todos os inadimplentes |

```python
# Com 5 linhas de Python você processa o que levaria horas manualmente
import csv

with open('clientes.csv') as f:
    for cliente in csv.DictReader(f):
        if float(cliente['saldo']) < 0:
            print(f"Alerta: {cliente['nome']} - Saldo: {cliente['saldo']}")
```

---

# Leitura de Arquivos CSV com Python

### O que é CSV?
**Comma-Separated Values** — arquivo de texto simples onde cada linha é um registro e as colunas são separadas por vírgula (ou ponto e vírgula).

### Exemplo de arquivo `clientes.csv`:
```
nome,conta,saldo,tipo
Ana Silva,1001,15000.50,corrente
João Santos,1002,-500.00,corrente
Maria Oliveira,1003,8200.00,poupanca
Carlos Lima,1004,-1200.75,corrente
```

### Lendo com Python:
```python
import csv

def ler_clientes(caminho_arquivo):
    """Lê um arquivo CSV e retorna uma lista de dicionários."""
    clientes = []
    with open(caminho_arquivo, encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            linha['saldo'] = float(linha['saldo'])
            clientes.append(linha)
    return clientes

clientes = ler_clientes('clientes.csv')
print(f"Total de clientes: {len(clientes)}")
```

> `csv.DictReader` transforma cada linha em um **dicionário** — muito prático!

---

# Manipulação de Listas e Dicionários

### Cada cliente é um dicionário:
```python
cliente = {
    'nome': 'Ana Silva',
    'conta': '1001',
    'saldo': 15000.50,
    'tipo': 'corrente'
}

# Acessando valores
print(cliente['nome']) # Ana Silva
print(cliente['saldo']) # 15000.50
```

### Operações comuns com listas de clientes:
```python
# Filtrar clientes com saldo negativo
inadimplentes = [c for c in clientes if c['saldo'] < 0]

# Calcular saldo total
saldo_total = sum(c['saldo'] for c in clientes)

# Encontrar maior saldo
maior_saldo = max(clientes, key=lambda c: c['saldo'])

# Agrupar por tipo de conta
from collections import defaultdict
por_tipo = defaultdict(list)
for c in clientes:
    por_tipo[c['tipo']].append(c)

# Ordenar por nome
ordenados = sorted(clientes, key=lambda c: c['nome'])
```

> Esses padrões aparecem **constantemente** em automação bancária!

---

# [DEMO] Ler clientes.csv e filtrar dados

## `demo02_ler_csv.py`

### O que vamos fazer:
1. Usar o Copilot para escrever um script que lê `clientes.csv`
2. Filtrar clientes com saldo negativo
3. Exibir um resumo formatado no terminal

### Prompts que usaremos no Copilot:
```python
# Leia o arquivo clientes.csv da pasta dados
# Filtre os clientes com saldo negativo
# Exiba: nome, conta e saldo de cada inadimplente
# No final, mostre o total de inadimplentes e a soma dos saldos negativos
```

### Resultado esperado:
```
=== RELATÓRIO DE INADIMPLENTES ===
Nome: João Santos | Conta: 1002 | Saldo: R$ -500.00
Nome: Carlos Lima | Conta: 1004 | Saldo: R$ -1.200,75

Total de inadimplentes: 2
Soma dos saldos negativos: R$ -1.700,75
```

> _Acompanhe: vamos escrever prompts e ver o Copilot gerar o código!_

---

# [DEMO] Gerar relatório de transações

## `demo03_relatorio.py`

### O que vamos fazer:
1. Ler dados de clientes e transações
2. Cruzar informações entre arquivos CSV
3. Gerar um relatório completo no terminal

### Conceitos aplicados:
- Leitura de múltiplos CSVs
- Junção de dados (similar a JOIN em SQL)
- Formatação de valores monetários
- Cálculos agregados (soma, média, contagem)

### Exemplo de saída esperada:
```
╔══════════════════════════════════════════╗
║ RELATÓRIO DE TRANSAÇÕES - 2024 ║
╠══════════════════════════════════════════╣
║ Total de transações: 150 ║
║ Volume total: R$ 245.890,00 ║
║ Ticket médio: R$ 1.639,27 ║
║ Transação mais alta: R$ 15.000,00 ║
╚══════════════════════════════════════════╝
```

> _Vamos construir isso passo a passo com o Copilot!_

---

# Lab Prático — Instruções

## Exercício: Análise de Contas Bancárias

### Objetivo:
Usando Python e o GitHub Copilot, crie um script que:

1. **Leia** o arquivo `dados/clientes.csv`
2. **Calcule** as seguintes métricas:
   - Saldo total de todos os clientes
   - Saldo médio por tipo de conta (corrente vs poupança)
   - Quantidade de clientes com saldo acima de R$ 10.000
3. **Filtre** e exiba os clientes com saldo negativo
4. **Gere** um resumo formatado no terminal

### Regras:
- Use o Copilot Chat e autocomplete para ajudar
- Escreva **comentários primeiro**, depois deixe o Copilot completar
- Revise o código gerado antes de executar
- Não copie código pronto — use a IA como assistente

### Tempo: 25 minutos

---

# Lab Prático — Dicas

### Como usar o Copilot para resolver:

**Passo 1**: Comece com um comentário de alto nível
```python
# Script de análise de contas bancárias
# Lê clientes.csv e gera relatório com métricas
```

**Passo 2**: Peça uma função por vez
```python
# Função que lê o CSV e retorna lista de dicionários
```

**Passo 3**: Use o Copilot Chat para dúvidas
> "Como calculo a média de saldos agrupado por tipo de conta?"

**Passo 4**: Se travar, use `/explain` no código existente

**Passo 5**: Teste com os dados fornecidos

### Erros comuns:
- Esquecer de converter saldo de `string` para `float`
- Caminho do arquivo errado (use `dados/clientes.csv`)
- Divisão por zero se não houver clientes de um tipo

---

# Lab Prático — Checklist de Entrega

### Verifique se seu script:

- [ ] Lê o arquivo `clientes.csv` sem erro
- [ ] Converte os saldos para número (`float`)
- [ ] Calcula o saldo total de todos os clientes
- [ ] Calcula o saldo médio por tipo de conta
- [ ] Conta quantos clientes têm saldo acima de R$ 10.000
- [ ] Lista os inadimplentes (saldo negativo)
- [ ] Exibe os resultados formatados no terminal
- [ ] O código está legível e com comentários

### Bônus (se sobrar tempo):
- [ ] Ordenar inadimplentes do mais negativo para o menos negativo
- [ ] Salvar o relatório em um arquivo `.txt`
- [ ] Adicionar tratamento de erro (`try/except`) para arquivo não encontrado

### Salve seu arquivo como: `labs/lab01_analise_contas.py`

---

# Recap — O que aprendemos hoje

### Conceitos:
- O que é **desenvolvimento assistido por IA**
- Como funcionam os **LLMs** (tokens, contexto, previsão)
- **Limitações** da IA (alucinação, contexto limitado)
- Importância de **bons prompts**

### Ferramentas:
- **ChatGPT** para conversa e planejamento
- **GitHub Copilot** para código dentro do VS Code
- Panorama de outras ferramentas (Cursor, Spark, Lovable)

### Prática:
- Instalação e configuração do **Copilot**
- Leitura de **CSV com Python**
- Metodologia: **Pensar → Dividir → Pedir → Revisar → Testar**

> _"A IA é tão boa quanto o prompt que você dá e a revisão que você faz."_

---

# Preview da Aula 2 + Referências

### Na próxima aula:
- **SQL com Copilot**: criação de tabelas, consultas, joins
- **Banco de dados SQLite** com Python
- **Padrões de prompt** avançados para SQL
- **Lab**: Sistema de cadastro com banco de dados

### Referências e links úteis:
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [GitHub Copilot Free](https://github.com/features/copilot)

### Leitura recomendada:
- "GitHub Copilot: O Guia do Desenvolvedor" — GitHub Blog
- "Prompt Engineering for Developers" — DeepLearning.AI

> _Pratiquem com o Copilot Free até a próxima aula! Quanto mais usarem, melhor ficam._

---

# Obrigado!

### Dúvidas?

**Contato**: [e-mail/canal do instrutor]

> _"O melhor momento para começar a usar IA no desenvolvimento foi ontem. O segundo melhor momento é agora."_
