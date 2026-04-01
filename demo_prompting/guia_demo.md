# Demo: Evolucao de Prompt Engineering com Copilot

## Objetivo

Mostrar ao vivo como a qualidade da interacao com a IA muda drasticamente dependendo de:
1. **Como voce pede** (prompt vago vs. prompt detalhado)
2. **Que instrucoes voce da** (sem instructions vs. com instructions)

**Duracao**: ~25 minutos
**Ferramenta**: GitHub Copilot Chat no VS Code (plano Free)
**Arquivo de dados**: `dados/extrato_conta.csv` (extrato bancario pessoal ficticio - marco/2025)

---

## Preparacao

Antes de comecar a demo:

1. Abra o VS Code na pasta `demo_prompting/`
2. Verifique que o Copilot esta ativo (icone no canto inferior)
3. **Desative temporariamente** o arquivo `.github/copilot-instructions.md`:
   - Renomeie para `copilot-instructions.md.bak` (vamos reativar na Etapa 3)
4. Abra o arquivo `dados/extrato_conta.csv` no editor para que o Copilot tenha contexto
5. Tenha os scripts de `resultados_esperados/` prontos como backup

---

## Etapa 1 — O Prompt Vago (5 min)

### Contexto para a turma

> "Vamos comecar pedindo algo para o Copilot da forma como a maioria das pessoas faz no dia a dia — de forma vaga e imprecisa."

### Acao

1. Abra o Copilot Chat (Ctrl+Shift+I ou clique no icone do chat)
2. Tenha o arquivo `extrato_conta.csv` aberto no editor
3. Digite o seguinte prompt:

```
analisa esse CSV pra mim
```

4. Aguarde a resposta do Copilot

### O que provavelmente vai acontecer

O Copilot vai gerar algo como:
- Codigo generico que apenas le e imprime os dados
- Sem formatacao de valores monetarios
- Sem agrupamento por categoria
- Talvez nem use o contexto do arquivo aberto
- Pode sugerir pandas sem necessidade
- Sem tratamento de erros

**Backup**: Se o resultado for muito diferente, mostre o arquivo `resultados_esperados/etapa1_resultado.py`

### Ponto pedagogico

> "Vejam: o Copilot fez algo, mas nao e muito util. Ele nao sabe o que queremos porque NOS nao dissemos o que queremos. E como pedir para um estagiario 'faz ai uma analise' sem explicar de que, para quem, em que formato."
>
> **Regra de ouro: A qualidade do output da IA e diretamente proporcional a qualidade do input.**

---

## Etapa 2 — O Prompt Bem Feito (7 min)

### Contexto para a turma

> "Agora vamos fazer EXATAMENTE a mesma coisa, mas com um prompt que deixa claro o que queremos. Notem a diferenca."

### Acao

1. No Copilot Chat, inicie uma nova conversa (clique em +)
2. Certifique-se que o arquivo `extrato_conta.csv` esta aberto
3. Digite o seguinte prompt:

```
Crie um script Python que leia o arquivo dados/extrato_conta.csv.
Este arquivo contem um extrato bancario pessoal com as colunas: data, descricao, categoria, tipo (debito/credito) e valor.

O script deve:
1. Calcular o total de gastos (debitos) e receitas (creditos) do mes
2. Agrupar os gastos por categoria e mostrar o total e o percentual de cada uma
3. Identificar a categoria com maior gasto
4. Gerar um relatorio formatado no terminal com separadores visuais

Use Python puro com o modulo csv (nao use pandas).
```

4. Aguarde a resposta

### O que provavelmente vai acontecer

O Copilot vai gerar um codigo MUITO melhor:
- Calcula debitos e creditos separadamente
- Agrupa por categoria
- Mostra percentuais
- Relatorio formatado
- Mas provavelmente: sem funcoes, sem docstrings, sem tratamento de erro, valores no formato americano

**Backup**: `resultados_esperados/etapa2_resultado.py`

### Compare ao vivo

> "Vamos rodar os dois. Vejam a diferenca."

Execute ambos os scripts e compare a saida.

### Ponto pedagogico

> "Mesmo pedido — 'analisa o CSV' — mas agora com CONTEXTO e ESPECIFICIDADE. Olhem o que mudou no prompt:"
>
> 1. **Disse o que e o arquivo** (extrato bancario pessoal, com as colunas X, Y, Z)
> 2. **Listou o que quero** (calcular totais, agrupar, identificar maior)
> 3. **Especificou o formato de saida** (relatorio formatado no terminal)
> 4. **Restringiu a tecnologia** (Python puro, modulo csv)
>
> "Quatro coisas simples que transformaram o resultado."

---

## Etapa 3 — Com Instructions (5 min)

### Contexto para a turma

> "O resultado ficou bom, mas e se eu quisesse que TODO codigo gerado pelo Copilot seguisse certas regras automaticamente? Sem eu precisar repetir no prompt toda vez? Para isso existem as INSTRUCTIONS."

### Acao

1. **Reative o arquivo de instructions**:
   - Renomeie `copilot-instructions.md.bak` de volta para `copilot-instructions.md` na pasta `.github/`
   - (Mostre o conteudo do arquivo para a turma antes de reativar)

2. Mostre o conteudo do arquivo para a turma:

```
Abram o arquivo .github/copilot-instructions.md comigo.
Vejam que definimos:
- Escopo: apenas analise de dados bancarios
- Encoding UTF-8 obrigatorio
- Caminhos relativos
- Codigo modularizado em funcoes
- Docstrings obrigatorias
- Tratamento de erros
- Formato monetario brasileiro (R$ 1.234,56)
- E mais...
```

3. No Copilot Chat, inicie uma nova conversa
4. Use o MESMO prompt da Etapa 2 (copie e cole)
5. Aguarde a resposta

### O que provavelmente vai acontecer

O Copilot vai gerar codigo que segue as instructions:
- Funcoes separadas com docstrings
- `encoding='utf-8'` em todos os `open()`
- Caminhos relativos com `__file__`
- Tratamento de erros com `try/except`
- Valores em formato brasileiro (R$ 1.234,56)
- `if __name__ == "__main__":`
- Variaveis com nomes descritivos em portugues

**Backup**: `resultados_esperados/etapa3_resultado.py`

### Compare ao vivo

Execute os 3 scripts lado a lado (ou em sequencia) e mostre a evolucao:

```bash
python resultados_esperados/etapa1_resultado.py
python resultados_esperados/etapa2_resultado.py
python resultados_esperados/etapa3_resultado.py
```

### Ponto pedagogico

> "Mesmo prompt da Etapa 2, mas agora o Copilot seguiu regras que definimos UMA VEZ. Nao precisei pedir 'use docstrings', 'use encoding utf-8', 'formate como R$'. As instructions fazem isso automaticamente."
>
> "Em um time de desenvolvimento, instructions garantem que TODOS os desenvolvedores recebem sugestoes consistentes do Copilot."

---

## Etapa 3.5 — Agente Custom: Levando ao Proximo Nivel (3 min)

### Contexto para a turma

> "Alem das instructions, podemos criar um AGENTE CUSTOM — um assistente com nome, descricao e regras proprias que aparece como opcao no Copilot Chat. E como criar um 'especialista' dentro do seu projeto."

### Acao

1. Mostre o arquivo `.github/agents/analista-bancario.agent.md`
2. Destaque a estrutura:

```
O arquivo tem duas partes:
1. FRONTMATTER (entre ---): nome, descricao, ferramentas permitidas
2. CORPO: as mesmas instrucoes que tinhamos, mas agora vinculadas a um agente
```

3. No Copilot Chat, clique no seletor de agentes (dropdown no topo do chat)
4. O agente **"Analista Bancario"** deve aparecer na lista
5. Selecione-o e faca o mesmo pedido:

```
analisa o extrato do CSV
```

### Ponto pedagogico

> "A diferenca entre instructions e um agente custom:
> - **Instructions** se aplicam a TODAS as conversas do Copilot neste projeto
> - **Agente custom** e uma PERSONA que voce seleciona quando quer — pode ter varios agentes diferentes para diferentes tarefas
>
> Pensem em agentes como 'especialistas' do seu time: um para dados, outro para testes, outro para documentacao."

### Estrutura do arquivo agent.md

```markdown
---
name: Analista Bancario           # Nome que aparece no dropdown
description: Especialista em...   # Descricao curta
tools: [edit, search, runCommands] # Ferramentas que o agente pode usar
---

(Instrucoes do agente aqui - mesmo formato das instructions)
```

> "Para criar um agente, basta colocar um arquivo `.agent.md` na pasta `.github/agents/`. O VS Code detecta automaticamente."

---

## Etapa 4 — Guardrails: Fora do Escopo (3 min)

### Contexto para a turma

> "Uma coisa muito poderosa das instructions e que podemos LIMITAR o que o assistente faz. Olhem o que acontece quando pedimos algo fora do escopo."

### Acao

1. Com as instructions ainda ativas, no Copilot Chat digite:

```
crie um jogo da velha em Python
```

2. Aguarde a resposta

### O que provavelmente vai acontecer

O Copilot deve responder algo como:
> "Desculpe, estou configurado para ajudar apenas com analise de dados bancarios."

Ou pode gerar o codigo mesmo assim (as instructions sao "sugestoes", nao bloqueios absolutos). Se gerar:

> "Notem que mesmo assim, o Copilot tentou seguir as instructions mas nao recusou completamente. Instructions sao orientacoes, nao firewalls. Para bloqueio real, precisariamos de outra camada de seguranca."

3. Tente outro pedido fora do escopo:

```
escreva um email de ferias para meu chefe
```

### Ponto pedagogico

> "As instructions funcionam como GUARDRAILS — elas orientam o assistente a ficar no caminho certo. Nao sao 100% infalíveis, mas fazem uma diferenca enorme na pratica."
>
> "Pensem nisso para seus projetos: se voce tem um assistente de IA em producao, instructions ajudam a manter o foco e evitar respostas fora de contexto."

---

## Resumo Final (1 min)

Mostre este resumo para fechar:

| Etapa | Prompt | Resultado |
|-------|--------|-----------|
| 1 | Vago: "analisa esse CSV" | Codigo generico e inutil |
| 2 | Detalhado: contexto + requisitos + formato | Codigo funcional e util |
| 3 | Detalhado + Instructions | Codigo profissional e consistente |
| 3.5 | Agente custom "Analista Bancario" | Especialista selecionavel no dropdown |
| 4 | Fora do escopo + Instructions | Assistente recusa educadamente |

> **Mensagem final**: "A IA e tao boa quanto o contexto que voce da. Investir 2 minutos num prompt bom economiza 20 minutos de retrabalho. E instructions dao consistencia para o time inteiro."

---

## Troubleshooting

### O Copilot nao usa as instructions
- Verifique que o arquivo esta em `.github/copilot-instructions.md` (exatamente esse caminho)
- Reinicie o VS Code apos criar/renomear o arquivo
- As instructions funcionam melhor no Copilot Chat do que no autocompletar

### O Copilot gera resultado muito diferente do esperado
- Use os scripts em `resultados_esperados/` como backup
- Lembre a turma: "A IA nao e deterministica — cada execucao pode gerar algo ligeiramente diferente"

### O Copilot ignora o escopo das instructions
- Normal — instructions sao orientacoes, nao bloqueios absolutos
- Use isso como ponto pedagogico: "Por isso revisao humana ainda e essencial"

### O plano Free atingiu o limite de mensagens
- Limite do Free: 50 mensagens/mes no Copilot Chat
- Se atingir, use os scripts de backup e explique o conceito
