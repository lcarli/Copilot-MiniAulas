# 🚀 Lab 2 — Mini Projeto Final

**Tempo estimado:** ~40 minutos

## Objetivo

Aplicar tudo o que você aprendeu sobre desenvolvimento com IA para construir uma solução completa, **do zero**, com a ajuda do GitHub Copilot.

---

## Metodologia

Siga o ciclo em todas as etapas:

```
🧠 Pensar → ✂️ Dividir → 💬 Pedir → 🔍 Revisar → ✅ Testar
```

1. **Pensar** — Entenda o problema antes de escrever código
2. **Dividir** — Quebre em partes menores e independentes
3. **Pedir** — Faça prompts claros e específicos ao Copilot
4. **Revisar** — Leia e entenda o código gerado antes de aceitar
5. **Testar** — Execute e valide com os dados reais

---

## Dados Disponíveis

| Arquivo | Colunas |
|---------|---------|
| `aula1/dados/clientes.csv` | id_cliente, nome, cpf, agencia, tipo_conta, data_abertura, saldo_atual |
| `aula2/dados/transacoes_janeiro.csv` | id_transacao, id_cliente, data, tipo, categoria, valor, descricao |
| `aula2/dados/transacoes_fevereiro.csv` | (mesmo formato) |
| `aula2/dados/transacoes_marco.csv` | (mesmo formato) |

**Categorias existentes:** alimentacao, aluguel, educacao, lazer, salario, saude, transferencia, transporte

**Tipos de transação:** credito (entrada), debito (saída)

---

## Escolha UMA das opções abaixo:

---

## Opção A — 📊 Relatório Mensal de Gastos por Categoria

### Descrição

Crie um programa que consolide as transações dos 3 meses e gere um relatório de gastos (débitos) agrupados por categoria.

### Passo a Passo Sugerido

1. Crie uma função para ler um arquivo CSV de transações
2. Crie uma função para consolidar os 3 arquivos em uma lista única
3. Filtre apenas as transações de débito (gastos)
4. Agrupe os gastos por categoria
5. Calcule: total por categoria, média por categoria, percentual do total
6. Gere o relatório formatado no terminal

### Exemplos de Prompts para o Copilot

> "Crie uma função em Python que leia um CSV de transações bancárias com as colunas id_transacao, id_cliente, data, tipo, categoria, valor, descricao e retorne uma lista de dicionários."

> "Crie uma função que receba uma lista de transações e retorne apenas as de tipo 'debito'."

> "Crie uma função que agrupe transações por categoria e calcule o total, a média e o percentual de cada categoria em relação ao total geral."

> "Gere um relatório formatado no terminal com os gastos por categoria, mostrando total, média e percentual, ordenado do maior para o menor gasto."

### Checklist de Funcionalidades

- [ ] Lê os 3 CSVs de transações
- [ ] Filtra apenas débitos
- [ ] Agrupa por categoria
- [ ] Calcula total, média e percentual por categoria
- [ ] Exibe relatório formatado no terminal
- [ ] Usa `with` para abrir arquivos
- [ ] Trata `FileNotFoundError`
- [ ] Funções com docstrings

### Exemplo de Saída Esperada

```
══════════════════════════════════════════════════════════
   RELATÓRIO DE GASTOS POR CATEGORIA — JAN a MAR/2025
══════════════════════════════════════════════════════════

 Categoria        Total (R$)    Média (R$)     %
 ─────────────────────────────────────────────────
 aluguel           12.500,00     1.562,50    25,3%
 alimentacao        8.200,00       410,00    16,6%
 transporte         5.100,00       340,00    10,3%
 ...

 TOTAL GERAL: R$ 49.350,00
══════════════════════════════════════════════════════════
```

---

## Opção B — 🔍 Detector de Transações Suspeitas

### Descrição

Crie um programa que analise as transações dos 3 meses e identifique transações suspeitas com base em regras predefinidas.

### Regras de Suspeita

1. **Valor alto**: transação com valor superior a R$ 5.000,00
2. **Múltiplas transações no mesmo dia**: cliente com 3 ou mais transações na mesma data
3. **Transações em finais de semana**: transações realizadas em sábados ou domingos (use a data como proxy)

### Passo a Passo Sugerido

1. Crie funções para ler os CSVs de transações e de clientes
2. Consolide todas as transações em uma lista
3. Implemente cada regra de detecção em uma função separada
4. Para cada transação suspeita, registre o motivo
5. Cruze com os dados de clientes para enriquecer o alerta (nome, agência)
6. Gere um relatório de alertas formatado

### Exemplos de Prompts para o Copilot

> "Crie uma função que receba uma lista de transações e retorne as que têm valor acima de 5000."

> "Crie uma função que identifique clientes com 3 ou mais transações no mesmo dia."

> "Crie uma função que identifique transações realizadas em sábados ou domingos usando datetime."

> "Gere um relatório de alertas de transações suspeitas, agrupado por tipo de suspeita, incluindo o nome do cliente e o motivo."

### Checklist de Funcionalidades

- [ ] Lê os 3 CSVs de transações + clientes.csv
- [ ] Detecta transações com valor > R$ 5.000
- [ ] Detecta múltiplas transações no mesmo dia para o mesmo cliente
- [ ] Detecta transações em finais de semana
- [ ] Inclui nome do cliente nos alertas
- [ ] Exibe relatório de alertas formatado
- [ ] Funções com docstrings e tratamento de erros

### Exemplo de Saída Esperada

```
══════════════════════════════════════════════════════════
   🚨 RELATÓRIO DE TRANSAÇÕES SUSPEITAS
══════════════════════════════════════════════════════════

 🔴 VALOR ALTO (> R$ 5.000,00): 6 transações
 ───────────────────────────────────────────────
   #39 | 2025-01-25 | João Silva      | R$ 5.576,76 | Salário ref. mês anterior
   ...

 🟡 MÚLTIPLAS NO MESMO DIA: 4 ocorrências
 ───────────────────────────────────────────────
   Ana Souza | 2025-02-15 | 3 transações no dia
   ...

 🟠 FINAL DE SEMANA: 12 transações
 ───────────────────────────────────────────────
   #102 | 2025-01-11 (Sáb) | Maria Oliveira | R$ 230,00
   ...
══════════════════════════════════════════════════════════
```

---

## Opção C — 📋 Resumo Executivo para Gerente de Agência

### Descrição

Crie um programa que gere um resumo executivo em texto corrido (como um email) para o gerente de uma agência específica, com os principais indicadores do trimestre.

### Passo a Passo Sugerido

1. Crie funções para ler os CSVs de transações e de clientes
2. Filtre os clientes pela agência desejada (ex: `0001`)
3. Filtre as transações desses clientes
4. Calcule indicadores por mês: total movimentado, número de transações
5. Calcule o crescimento mês a mês (em %)
6. Identifique os clientes mais ativos
7. Gere um texto corrido formatado como email executivo

### Exemplos de Prompts para o Copilot

> "Crie uma função que filtre clientes por agência e retorne seus IDs."

> "Crie uma função que filtre transações por uma lista de IDs de clientes."

> "Crie uma função que calcule o total movimentado por mês a partir de uma lista de transações."

> "Calcule o crescimento percentual entre meses consecutivos."

> "Gere um texto em formato de email executivo com os indicadores da agência, incluindo total movimentado por mês, número de clientes ativos e crescimento."

### Checklist de Funcionalidades

- [ ] Lê os 3 CSVs de transações + clientes.csv
- [ ] Filtra por agência específica
- [ ] Calcula total movimentado por mês
- [ ] Calcula número de clientes ativos por mês
- [ ] Calcula crescimento mês a mês (%)
- [ ] Gera resumo executivo em texto corrido
- [ ] Funções com docstrings e tratamento de erros

### Exemplo de Saída Esperada

```
══════════════════════════════════════════════════════════
De: Sistema de Análise Bancária
Para: Gerente da Agência 0001
Assunto: Resumo Executivo — 1º Trimestre 2025
══════════════════════════════════════════════════════════

Prezado(a) Gerente,

Segue o resumo de desempenho da Agência 0001 referente ao
período de Janeiro a Março de 2025.

A agência possui 5 clientes cadastrados. No trimestre,
foram registradas 42 transações totalizando R$ 38.500,00
em movimentações.

MOVIMENTAÇÃO MENSAL:
  • Janeiro/2025:  R$ 12.300,00 (14 transações)
  • Fevereiro/2025: R$ 13.800,00 (15 transações) — ↑ 12,2%
  • Março/2025:     R$ 12.400,00 (13 transações) — ↓ 10,1%

Os clientes mais ativos no período foram Carlos Eduardo
Souza (12 transações) e Maria Fernanda Oliveira (9
transações).

Atenciosamente,
Sistema de Análise Bancária
══════════════════════════════════════════════════════════
```

---

## Dicas Gerais

1. **Comece simples** — faça funcionar primeiro, depois melhore
2. **Teste cedo** — rode o código a cada nova função
3. **Use os dados reais** — os CSVs estão na pasta `dados/`
4. **Não aceite tudo cegamente** — revise o que o Copilot gerar
5. **Documente** — docstrings e nomes claros facilitam sua vida

---

## Entrega

Salve seu código em `aula2/labs/lab02_meu_projeto.py` e execute para verificar que funciona com os dados reais.

Ao final, compare com a solução de referência em `lab02_solucao.py` (implementa a Opção A).
