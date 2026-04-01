# 🎓 Roteiro do Instrutor — Aula 2
## Desenvolvimento Rápido com Soluções de IA
### Produtividade e Projeto Final

**Duração total**: ~3 horas (19:00 – 22:00)  
**Pré-requisito**: Aula 1 — Fundamentos e Primeiros Passos  
**Materiais necessários**: slides.md, demo01–04, lab01–02, dados CSV

> ⚠️ Este documento é um guia minuto-a-minuto para o instrutor.
> Falas sugeridas estão em *itálico* entre aspas.
> Instruções de ação estão em **negrito**.

---

## ✅ Checklist de Preparação (fazer ANTES da aula)

### Ambiente
- [ ] VS Code aberto com a pasta `aulaCopilot` como workspace
- [ ] GitHub Copilot ativo e funcionando (testar com um prompt simples)
- [ ] Python 3.10+ instalado e funcionando no terminal integrado
- [ ] Terminal do VS Code visível e limpo
- [ ] Tema do VS Code com boa legibilidade para projeção (fundo escuro, fonte ≥16pt)
- [ ] Zoom do VS Code em ~150% para legibilidade na projeção

### Arquivos pré-abertos em abas
- [ ] `aula2/slides/slides.md` (para referência)
- [ ] `aula2/demos/demo01_refatoracao.py`
- [ ] `aula2/demos/demo02_debugging.py`
- [ ] `aula2/demos/demo03_pipeline.py`
- [ ] `aula2/demos/demo04_documentacao.py`

### Dados verificados
- [ ] Executar `python aula2/demos/demo01_refatoracao.py` → funciona sem erros
- [ ] Executar `python aula2/demos/demo03_pipeline.py` → gera relatório completo
- [ ] Executar `python aula2/demos/demo04_documentacao.py` → funciona sem erros
- [ ] Verificar que `aula2/dados/transacoes_janeiro.csv`, `transacoes_fevereiro.csv` e `transacoes_marco.csv` existem
- [ ] Verificar que `aula1/dados/clientes.csv` existe (usado pelo pipeline)

### Backup / Plano B
- [ ] Slides em PDF exportados (caso VS Code falhe)
- [ ] Screenshots dos outputs de cada demo salvos em pasta local
- [ ] Copilot Chat testado — se não responder, ter prompts prontos com respostas esperadas
- [ ] Hotspot do celular pronto (caso Wi-Fi falhe)
- [ ] Versão offline dos slides aberta no navegador

---

## 📋 Visão Geral dos Blocos

| # | Bloco | Horário | Duração |
|---|-------|---------|---------|
| 1 | Revisão e Aquecimento | 19:00 – 19:15 | 15 min |
| 2 | IA no Ciclo de Desenvolvimento | 19:15 – 19:40 | 25 min |
| 3 | Refatoração e Debugging | 19:40 – 20:10 | 30 min |
| 4 | ☕ Intervalo | 20:10 – 20:20 | 10 min |
| 5 | Automações Bancárias Realistas | 20:20 – 21:00 | 40 min |
| 6 | Documentação e Organização | 21:00 – 21:20 | 20 min |
| 7 | Mini Projeto Final | 21:20 – 22:00 | 40 min |

---

# BLOCO 1 — Revisão e Aquecimento
## 🕐 19:00 – 19:15 (15 min)

### 19:00 – 19:05 | Boas-vindas e recap (5 min)

**Ação**: Abrir os slides na seção "Recap — O que vimos na Aula 1".

*"Boa noite, pessoal! Bem-vindos à Aula 2. Antes de avançar, vamos relembrar rapidamente o que vimos na semana passada."*

**Percorrer os pontos do recap** — não se aprofundar, apenas validar:

*"Na Aula 1, nós entendemos o que é IA generativa e como LLMs funcionam — eles preveem o próximo token. Instalamos e configuramos o GitHub Copilot. Aprendemos que Tab aceita sugestões e Ctrl+I abre o chat inline. Trabalhamos com Python lendo CSVs e manipulando dados de clientes. E a grande lição: a IA é sua co-piloto, mas quem dirige é você."*

**Perguntar à turma:**

*"Alguém usou o Copilot durante a semana? Experimentou algo por conta? Teve alguma dificuldade?"*

> 💡 **Dica**: Se alguém relatar uma experiência, peça 30 segundos de relato. Isso engaja a turma e valida o aprendizado.

### 19:05 – 19:15 | Quick Challenge: Validação de CPF (10 min)

**Ação**: Abrir os slides na seção "Quick Challenge — Aquecimento".

*"Vamos começar com um desafio rápido para aquecer. Quero que vocês vejam na prática como o Copilot já conhece padrões do mundo real."*

**Ação**: Criar um arquivo novo no VS Code (`aquecimento_cpf.py`).

*"Vou abrir um arquivo vazio e pedir ao Copilot para criar uma função que valida CPF. Observem o prompt que vou usar."*

**Digitar no Copilot Chat (Ctrl+I)**:

```
Crie uma função Python chamada validar_cpf que recebe uma string
e retorna True se o CPF for válido (com verificação dos dígitos).
```

**Ação**: Esperar a sugestão do Copilot. Aceitar com Tab.

*"Vejam: o Copilot já conhece o algoritmo de validação de CPF da Receita Federal. Ele sabe que tem 11 dígitos, que sequências repetidas são inválidas e que precisa calcular os dois dígitos verificadores."*

**Testar ao vivo no terminal**:
```python
print(validar_cpf("529.982.247-25"))  # True
print(validar_cpf("111.111.111-11"))  # False
```

*"Funcionou! Isso é poderoso — em menos de 1 minuto temos uma função complexa que funciona. Mas lembrem-se: sempre testem. O Copilot pode gerar código que PARECE correto mas tem bugs sutis."*

> 🅱️ **Plano B**: Se o Copilot não responder ou gerar código incorreto, mostrar a versão pronta dos slides (bloco de código com `validar_cpf`). Dizer: *"Às vezes a IA erra ou demora — ter uma versão de referência é sempre bom."*

---

# BLOCO 2 — IA no Ciclo de Desenvolvimento
## 🕐 19:15 – 19:40 (25 min)

### 19:15 – 19:22 | O Ciclo Completo (7 min)

**Ação**: Abrir os slides na seção "O Ciclo Completo de Desenvolvimento".

*"Agora vamos entender onde a IA se encaixa no dia a dia de um desenvolvedor. Todo desenvolvimento segue um ciclo: Ideação, Prototipação, Validação e Iteração."*

**Mostrar o diagrama do ciclo** (Ideação → Prototipação → Validação → Iteração → volta).

*"A grande sacada é: com IA, cada fase fica mais rápida, mas nenhuma pode ser pulada. Vocês não podem pular direto para código sem entender o problema. A IA acelera, mas não substitui o pensamento."*

**Avançar para o slide "IA em Cada Fase do Ciclo".**

*"Olhem esta tabela. Na Ideação, a IA faz brainstorm. Na Prototipação, gera código rápido. Na Validação, gera testes. Na Iteração, refatora. A IA é útil em todas as fases, mas de formas diferentes."*

**Destacar os exemplos de prompt bom vs ruim:**

*"Observem a diferença: 'Faça um programa de banco' é vago demais. O Copilot não sabe o que fazer. Agora, 'Crie uma função que recebe uma lista de dicionários com campos valor e tipo, e retorna o saldo total' — isso é específico, claro, e gera um resultado muito melhor."*

### 19:22 – 19:28 | Estratégias para Copilot Free (6 min)

**Ação**: Avançar para o slide "Estratégias para Copilot Free".

*"Como a maioria de vocês está no plano Free, vamos falar de estratégias para usar as interações com sabedoria."*

**Percorrer as 3 estratégias**:

1. *"Primeira: prompts curtos e diretos. Não peça o mundo de uma vez. Peça uma função por vez."*

2. *"Segunda: arquivos pequenos e focados. O Copilot entende melhor arquivos com até ~100 linhas. Se seu arquivo tiver 500 linhas, ele se perde."*

3. *"Terceira: iterar por etapas. Passo 1: gere a função básica. Passo 2: peça validação. Passo 3: peça tratamento de erros. Passo 4: peça docstring. Cada passo é um prompt separado."*

*"Dividir para conquistar — vale para código E para prompts!"*

### 19:28 – 19:34 | Quando a IA Ajuda vs Quando Atrapalha (6 min)

**Ação**: Avançar para o slide "Quando a IA Ajuda vs Quando Atrapalha".

*"Isso aqui é muito importante. A IA NÃO é boa em tudo."*

**Ler a tabela destacando:**

*"A IA é ótima para gerar boilerplate, funções conhecidas, docstrings, refatorar código e escrever testes. Mas ela pode atrapalhar em decisões de arquitetura, lógica de negócio muito específica da sua empresa, e segurança crítica sem revisão."*

**Ler a regra de ouro em voz alta, enfatizando:**

*"Use a IA para acelerar o que você já sabe fazer. Use a IA para aprender o que você ainda não sabe. Nunca use a IA para pular o que você precisa entender. Imprimam isso na cabeça!"*

### 19:34 – 19:40 | Armadilhas Comuns (6 min)

**Ação**: Avançar para o slide "Armadilhas Comuns ao Usar IA".

*"Antes de irmos para as demos, vamos falar de 5 erros que todo mundo comete quando começa a usar IA para programar."*

**Percorrer cada armadilha rapidamente (1 min cada)**:

1. *"Copiar e colar mágico — aceitar código sem entender. Solução: sempre use /explain antes."*
2. *"Pedir o mundo de uma vez — prompts enormes geram código enorme e impossível de revisar."*
3. *"Loop infinito de correções — pedir para corrigir gera novo bug, e aí você pede de novo... Para, entenda o problema, reescreva o prompt do zero."*
4. *"Confiar demais — a IA pode gerar código que funciona com os seus dados mas falha com outros."*
5. *"Ignorar a estrutura — jogar tudo num arquivo só. Organize em módulos desde o início."*

*"A IA erra. Você revisa. Juntos, vocês produzem melhor do que cada um sozinho."*

> 💡 **Dica**: Esse bloco é teórico. Mantenha o ritmo para não perder a turma. Se o tempo estiver apertado, pule os detalhes das armadilhas e vá direto para as demos.

---

# BLOCO 3 — Refatoração e Debugging com Copilot
## 🕐 19:40 – 20:10 (30 min)

### 19:40 – 19:45 | Introdução à Refatoração (5 min)

**Ação**: Abrir os slides na seção "O que é Refatoração e Por Que Importa".

*"Refatoração é melhorar a estrutura do código SEM alterar o comportamento. O programa faz a mesma coisa, mas fica mais legível, mais fácil de manter e de estender."*

**Mostrar slide "Código Espaguete vs Código Modular"** — apontar as diferenças lado a lado.

*"Olhem o antes e o depois. Mesmo resultado, mas agora cada função pode ser testada, reutilizada e entendida separadamente. Isso é o poder da refatoração."*

### 19:45 – 19:58 | Demo 01 — Refatoração com Copilot (13 min)

**Ação**: Abrir `aula2/demos/demo01_refatoracao.py` no VS Code.

*"Vamos ver isso na prática. Abram comigo o arquivo demo01_refatoracao.py."*

#### Passo 1 — Mostrar o código "espaguete" (3 min)

**Ação**: Scrollar até o bloco comentado "VERSÃO ORIGINAL" (linhas 28-76).

*"Olhem este código. Variáveis chamadas x, y, d, t, k. Nenhuma função. Sem tratamento de erro. O open sem with. Tudo num bloco só. Quem consegue me dizer o que este código faz?"*

> 💡 Esperar uns 10 segundos. Alguém provavelmente dirá "lê transações" ou "calcula totais".

*"Exatamente — ele lê um CSV de transações, soma os débitos e agrupa por categoria. Mas levou um tempo para entender, né? Imagina manter isso numa equipe de 10 pessoas."*

#### Passo 2 — Pedir ao Copilot para refatorar (5 min)

**Ação**: Descomentar o bloco espaguete (linhas 36-65). Selecionar TODO o código descomentado.

**Ação**: Abrir o Copilot Chat com `Ctrl+I` e digitar:

```
Refatore este código seguindo boas práticas: crie funções separadas,
use nomes descritivos, adicione tratamento de erros e docstrings.
```

*"Vejam o que o Copilot sugere. Ele vai separar em funções, renomear variáveis, adicionar docstrings..."*

**Ação**: Mostrar a sugestão do Copilot na tela. **NÃO aceitar** — apenas exibir.

*"Legal, mas vamos comparar com a versão que já preparamos."*

#### Passo 3 — Comparar com a versão refatorada (3 min)

**Ação**: Scrollar até a "VERSÃO REFATORADA" (linha 80 em diante).

*"Olhem a versão refatorada. Temos 6 funções com responsabilidade única: carregar_transacoes, filtrar_por_tipo, calcular_total, calcular_media, agrupar_por_categoria e exibir_relatorio."*

**Mostrar a tabela de comparação** no final do arquivo (linhas 208-220):

*"Antes: variáveis x, y, d. Depois: total_debitos, media_debitos. Antes: sem funções. Depois: 6 funções. Antes: sem tratamento de erro. Depois: try/except com mensagens claras. Essa é a diferença entre código que funciona e código profissional."*

#### Passo 4 — Executar a versão refatorada (2 min)

**Ação**: Comentar novamente o bloco espaguete. Executar no terminal:

```bash
python aula2/demos/demo01_refatoracao.py
```

*"Funciona perfeitamente. Mesmo resultado, mas agora o código é sustentável."*

> 🅱️ **Plano B (Demo 01)**: Se o Copilot não gerar uma refatoração adequada, dizer: *"A IA nem sempre acerta de primeira. Por isso preparamos uma versão de referência. O importante é que vocês entendam o PROCESSO: mostrar o problema, pedir a melhoria, e sempre comparar."* Prosseguir mostrando a versão refatorada já pronta no arquivo.

### 19:58 – 20:10 | Demo 02 — Debugging com Copilot (12 min)

**Ação**: Abrir `aula2/demos/demo02_debugging.py` no VS Code.

*"Agora vamos para debugging. Debugging é parte do dia a dia — e o Copilot pode ajudar muito. Este arquivo tem 5 bugs INTENCIONAIS numerados de 1 a 5."*

**Ação**: Abrir os slides na seção "Debugging com Copilot" e mostrar a tabela de comandos (`/explain`, `/fix`, `/tests`, `@workspace`).

*"Antes de começar, guardem estes comandos: /explain explica o código, /fix sugere correção, /tests gera testes. Vamos usar os dois primeiros agora."*

#### Bug 4 — FileNotFoundError (3 min)

*"Vamos executar o código e ver o que acontece."*

**Ação**: Executar no terminal:
```bash
python aula2/demos/demo02_debugging.py
```

*"FileNotFoundError! Olhem a mensagem: ele está procurando em 'data/' mas a pasta se chama 'dados/'. Esse é o Bug 4."*

**Ação**: Selecionar a linha do `open()` (linha 44-47). Usar `/explain` no Copilot Chat.

*"Vejam, o Copilot explica: o caminho usa 'data' mas deveria ser 'dados'. Agora vamos pedir a correção."*

**Ação**: Usar `/fix` no Copilot Chat. Aceitar a correção (trocar `'data'` por `'dados'`).

*"Corrigido! Vamos executar de novo."*

#### Bug 3 — TypeError (3 min)

**Ação**: Executar novamente. Agora aparece TypeError.

*"TypeError: não dá para somar float com string. O valor lido do CSV vem como string, e o código tenta somar direto. Esse é o Bug 3."*

**Ação**: Selecionar a linha 76. Usar `/fix`.

*"A correção é simples: converter para float antes de usar. O Copilot sugere exatamente isso."*

**Ação**: Aplicar a correção (converter `valor` para `float(valor)`).

#### Bug 2 — KeyError (2 min)

**Ação**: Executar novamente. Agora aparece KeyError para 'investimentos'.

*"KeyError! O código tenta acessar a categoria 'investimentos' que não existe no dicionário. Solução: verificar antes de acessar."*

**Ação**: Aplicar a correção — usar `if nome_categoria in dados_categoria`.

#### Bug 5 — Lógica invertida (2 min)

*"Agora o código roda, mas olhem o resultado: 'Transações acima de R$ 200' mas está retornando muitas... Alguma coisa estranha."*

**Ação**: Selecionar a função `encontrar_transacoes_altas`. Usar `/explain`.

*"O Copilot detectou: o operador está invertido! Usa '<' quando deveria ser '>'. Esse é o bug mais perigoso: o código roda sem erro, mas o resultado está errado. Por isso SEMPRE testem os resultados, não apenas se roda."*

**Ação**: Corrigir `<` para `>`.

#### Bug 1 — ZeroDivisionError (2 min)

*"O Bug 1 é a divisão por zero. No nosso dataset, todas as categorias têm transações, então ele não aparece sozinho. Mas e se tivéssemos uma categoria vazia?"*

**Ação**: Adicionar manualmente antes de `calcular_media_por_categoria`:
```python
dados['teste'] = {'total': 0.0, 'transacoes': []}
```

*"Pronto — agora ele estoura. A correção: verificar se a lista está vazia antes de dividir."*

**Ação**: Remover a linha de teste. Mostrar a correção.

*"Cinco bugs, cinco correções. Percebam o fluxo: executar → ver o erro → selecionar → /explain → /fix → testar de novo. Esse é o ciclo de debugging assistido por IA."*

> 🅱️ **Plano B (Demo 02)**: Se o Copilot não funcionar para `/explain` ou `/fix`, mostrar as correções comentadas que já estão no próprio arquivo (cada bug tem a correção logo abaixo, precedida por `✅ CORREÇÃO`). Dizer: *"Mesmo sem a IA, as correções estão documentadas. O fluxo é o mesmo: entender o erro, encontrar a causa, aplicar a correção."*

---

# BLOCO 4 — Intervalo
## ☕ 20:10 – 20:20 (10 min)

*"Vamos fazer uma pausa de 10 minutos. Usem o banheiro, peguem um café. Quando voltarmos, vamos construir o pipeline principal da aula — a demo mais completa."*

> 💡 **Durante o intervalo**: Verificar que `demo03_pipeline.py` está pronto para executar. Abrir o arquivo e deixar na aba ativa. Verificar que os 3 CSVs de transações e o CSV de clientes estão acessíveis.

---

# BLOCO 5 — Automações Bancárias Realistas
## 🕐 20:20 – 21:00 (40 min)

### 20:20 – 20:28 | Contexto do Pipeline (8 min)

**Ação**: Abrir os slides na seção "O Desafio: Consolidar Dados de Múltiplos Meses".

*"Bem-vindos de volta! Agora vamos para a parte mais interessante da aula. Imaginem o cenário: vocês trabalham num banco. O sistema gera um CSV de transações por mês. O gerente pede um relatório consolidado do trimestre. Vocês têm 3 arquivos: janeiro, fevereiro e março."*

**Mostrar o diagrama do pipeline** nos slides (Ler → Consolidar → Classificar → Calcular → Reportar).

*"Esse padrão se chama pipeline — muito usado em engenharia de dados. Cada etapa é uma função que recebe dados e retorna dados transformados. A saída de uma é a entrada da próxima. Simples e poderoso."*

**Ação**: Mostrar os slides sobre validação de dados e tratamento de erros.

*"No mundo real, dados são sujos. Sempre validem! Vamos ver como o Copilot nos ajuda a construir cada etapa."*

### 20:28 – 20:55 | Demo 03 — Pipeline Completo (27 min)

**Ação**: Abrir `aula2/demos/demo03_pipeline.py` no VS Code.

*"Este é o demo principal da aula. Vamos percorrer o pipeline completo, etapa por etapa."*

> 💡 **Estratégia**: NÃO construir do zero ao vivo. O arquivo já está pronto. A abordagem é percorrer cada etapa, explicando como o Copilot ajudaria a criar cada função e como as peças se encaixam.

#### Etapa 1 — Carregamento de Dados (5 min)

**Ação**: Scrollar até a seção "ETAPA 1 — CARREGAMENTO DE DADOS" (linha 43).

*"Primeira etapa: carregar dados. Temos duas funções: carregar_transacoes e carregar_clientes. Ambas lêem CSV, mas com detalhes diferentes."*

**Destacar na função `carregar_transacoes`**:

*"Observem os detalhes: verificação se o arquivo existe ANTES de abrir, uso de with para gerenciar o arquivo, DictReader para ter nomes de colunas, e conversão de valor para float já na leitura. Cada detalhe foi pensado."*

*"Se vocês pedissem ao Copilot: 'Crie uma função que carrega transações de um CSV com tratamento de erros', ele geraria algo muito parecido."*

#### Etapa 2 — Consolidação (3 min)

**Ação**: Scrollar até "ETAPA 2 — CONSOLIDAÇÃO" (linha 100).

*"Segunda etapa: juntar os 3 meses. A função consolidar_transacoes recebe uma lista de listas e junta tudo em uma lista só. Simples, mas importante separar — e se amanhã tivermos 12 meses?"*

#### Etapa 3 — Classificação por Categoria (4 min)

**Ação**: Scrollar até "ETAPA 3 — CLASSIFICAÇÃO POR CATEGORIA" (linha 122).

*"Terceira etapa: agrupar por categoria. Usamos defaultdict — uma estrutura do Python que cria automaticamente uma lista vazia para chaves novas. O Copilot adora sugerir defaultdict quando vê agrupamentos."*

#### Etapa 4 — Estatísticas por Cliente (5 min)

**Ação**: Scrollar até "ETAPA 4 — ESTATÍSTICAS POR CLIENTE" (linha 143).

*"Aqui é onde fica interessante. Para cada cliente, calculamos total gasto, total recebido, número de transações e categorias usadas. Vejam como cruzamos com os dados de clientes para pegar o nome."*

**Destacar o defaultdict com lambda**:

*"Esse defaultdict com lambda é um padrão avançado — ele cria automaticamente a estrutura com valores zerados para cada novo cliente. Se o Copilot não sugerir isso, vocês podem pedir: 'Use defaultdict com lambda para inicializar'."*

#### Etapa 5 — Resumo Executivo (5 min)

**Ação**: Scrollar até "ETAPA 5 — RESUMO EXECUTIVO" (linha 194).

*"A última etapa de processamento: gerar o resumo em texto corrido. Vejam como a função recebe os dados já calculados e apenas monta o texto. Separação de responsabilidades!"*

**Destacar**: *"Essa função não faz cálculo nenhum — só formata texto. Isso é o princípio de responsabilidade única."*

#### Exibição e Execução (5 min)

**Ação**: Scrollar até `exibir_relatorio` e depois até `main()`.

*"A função main orquestra tudo: carrega, consolida, classifica, calcula, gera resumo e exibe. Cada passo é uma linha. Se algo falhar, o try/except captura."*

**Ação**: Executar no terminal:

```bash
python aula2/demos/demo03_pipeline.py
```

*"Olhem o resultado! Temos transações por mês, top 5 categorias de gasto com barras visuais, top 5 clientes por volume, média de gastos mensais e um resumo executivo em texto corrido. Tudo gerado automaticamente a partir de 3 CSVs."*

**Pausa dramática.**

*"Quanto tempo levaria para fazer isso manualmente no Excel? Horas. Com Python e Copilot? Construímos esse pipeline em minutos."*

> 🅱️ **Plano B (Demo 03)**: Se a execução falhar (ex: arquivo não encontrado), verificar os caminhos. O script usa caminhos relativos ao diretório do próprio arquivo. Se necessário, executar de dentro da pasta demos: `cd aula2/demos && python demo03_pipeline.py`. Se persistir, mostrar os screenshots do output salvos previamente.

### 20:55 – 21:00 | Reflexão e Conexão (5 min)

**Ação**: Mostrar os slides sobre organização em módulos e relatórios automatizados.

*"O que acabamos de ver é um padrão real usado em empresas. Dados entram, processamento acontece em etapas, e um relatório sai. Num ambiente profissional, cada etapa estaria em um arquivo separado: leitura.py, processamento.py, calculo.py, relatorio.py."*

*"E o Copilot ajudou em cada etapa: sugerir funções, adicionar type hints, gerar docstrings, tratar erros. Mas quem pensou na arquitetura do pipeline fomos nós."*

---

# BLOCO 6 — Documentação e Organização
## 🕐 21:00 – 21:20 (20 min)

### 21:00 – 21:05 | Por Que Documentar (5 min)

**Ação**: Abrir os slides na seção "Bloco 5 — Documentação e Organização".

*"Vamos falar de algo que todo mundo pula: documentação. Quem aqui já olhou código que escreveu há 3 meses e não entendeu nada?"*

> 💡 Esperar risos e mãos levantadas.

*"Documentação não é frescura — é investimento. Para o seu eu do futuro, para a equipe, para quem vai manter o código depois."*

**Mostrar rapidamente**: a tabela "O que documentar" e o formato Google Style de docstrings.

### 21:05 – 21:18 | Demo 04 — Documentação Automática (13 min)

**Ação**: Abrir `aula2/demos/demo04_documentacao.py` no VS Code.

*"Este arquivo tem 4 funções utilitárias bancárias SEM documentação. Vamos pedir ao Copilot para documentá-las."*

#### Passo 1 — Mostrar funções sem docstrings (3 min)

**Ação**: Scrollar pelas funções `validar_cpf`, `formatar_valor_monetario`, `calcular_media_movel`, `filtrar_transacoes_por_periodo` (linhas 36-112).

*"Olhem: 4 funções que funcionam perfeitamente, mas não têm nenhuma documentação. Se eu sou um desenvolvedor novo na equipe, como vou saber o que validar_cpf aceita como entrada? O que calcular_media_movel retorna? Quais exceções podem acontecer?"*

#### Passo 2 — Pedir ao Copilot para gerar docstrings (5 min)

**Ação**: Selecionar TODAS as funções (linhas 36-112). Abrir Copilot Chat com `Ctrl+I`.

```
Gere docstrings no formato Google Style para todas as funções 
selecionadas. Inclua Args, Returns, Raises e Examples.
```

*"Vejam o que o Copilot gera. Ele analisa o código, entende os parâmetros, identifica as exceções possíveis e até cria exemplos de uso."*

**Ação**: Mostrar a sugestão sem aceitar. Depois scrollar até o bloco "VERSÃO COM DOCSTRINGS" (linha 189 em diante).

*"Comparem com a versão de referência. Vejam como o Copilot identificou que validar_cpf aceita formato com ou sem pontuação, que formatar_valor_monetario pode lançar TypeError, e que calcular_media_movel pode lançar ValueError."*

#### Passo 3 — Mostrar template de README (3 min)

**Ação**: Scrollar até o bloco "TEMPLATE DE README.md" (linha 294 em diante).

*"Além de docstrings, o Copilot pode gerar o README do projeto inteiro. Olhem este template: tem descrição, requisitos, instalação, estrutura de pastas, uso e funcionalidades. Em 30 segundos, vocês têm um README profissional."*

#### Passo 4 — Executar as funções (2 min)

**Ação**: Executar no terminal:

```bash
python aula2/demos/demo04_documentacao.py
```

*"As funções funcionam perfeitamente — validação de CPF com dados reais dos clientes, formatação monetária, média móvel e filtro por período. Tudo testado com dados dos nossos CSVs."*

> 🅱️ **Plano B (Demo 04)**: Se o Copilot não gerar docstrings adequadas, mostrar diretamente o bloco comentado "VERSÃO COM DOCSTRINGS" que já está no arquivo. Dizer: *"Nem sempre o Copilot acerta os detalhes, mas ele dá uma base excelente que vocês ajustam em segundos."*

### 21:18 – 21:20 | Organização de Projeto (2 min)

**Ação**: Mostrar rapidamente os slides sobre organização de projeto Python e menção ao Git.

*"Duas coisas rápidas: organizem seus projetos com um módulo por responsabilidade, e usem Git para versionar. Não vamos aprofundar Git hoje, mas saibam que o Copilot também pode ajudar a gerar .gitignore e mensagens de commit."*

---

# BLOCO 7 — Mini Projeto Final
## 🕐 21:20 – 22:00 (40 min)

### 21:20 – 21:28 | Apresentação do Lab (8 min)

**Ação**: Abrir os slides na seção "Mini Projeto Final". Depois abrir `aula2/labs/lab02_instrucoes.md`.

*"Agora é a hora de vocês! Vamos ao mini projeto final. Vocês vão construir uma solução completa, do zero, com a ajuda do Copilot."*

**Mostrar a metodologia**:

*"Lembrem do ciclo: Pensar → Dividir → Pedir → Revisar → Testar. Usem isso em CADA etapa."*

**Apresentar as 3 opções** — ler o título e descrição de cada:

*"Opção A: Relatório Mensal de Gastos por Categoria. Vocês consolidam os 3 meses e geram um relatório de gastos agrupados por categoria. É a opção mais parecida com o pipeline que acabamos de ver."*

*"Opção B: Detector de Transações Suspeitas. Vocês criam regras de detecção: valor alto, múltiplas transações no mesmo dia, transações em final de semana. Ideal para quem gosta de lógica."*

*"Opção C: Resumo Executivo para Gerente de Agência. Vocês filtram por agência e geram um email executivo com indicadores. Ideal para quem gosta de relatórios e textos."*

*"Se estão em dúvida, recomendo a Opção A — é a mais direta e tem exemplos de prompts no arquivo de instruções."*

**Mostrar os dados disponíveis** (tabela no lab02):

*"Vocês têm 4 arquivos CSV: clientes na aula1/dados, e transações de janeiro, fevereiro e março na aula2/dados. As categorias são: alimentação, aluguel, educação, lazer, salário, saúde, transferência e transporte."*

**Mostrar o checklist de funcionalidades** de uma das opções.

*"Cada opção tem um checklist. Antes de me chamar dizendo que terminou, confiram o checklist."*

**Orientação final antes de começar**:

*"Criem o arquivo lab02_meu_projeto.py dentro de aula2/labs/. Comecem pela leitura de 1 CSV — faça funcionar com 1 antes de expandir para 3. Usem os prompts sugeridos no lab. E não aceitem código do Copilot sem ler — leiam tudo, entendam tudo."*

*"Vocês têm 30 minutos. Mãos à obra! Eu vou circular pela sala para ajudar."*

### 21:28 – 21:58 | Tempo de Desenvolvimento (30 min)

> 📋 **Guia para circular pela sala**:

#### Primeiros 5 min (21:28 – 21:33)
**Prioridade**: Garantir que todos começaram.
- Verificar se todos abriram o arquivo de instruções
- Verificar se todos criaram o arquivo `.py`
- Verificar se o Copilot está ativo
- **Problemas comuns**: aluno não sabe qual opção escolher (recomende A), Copilot não funciona (verificar extensão ativa), não encontra os CSVs (mostrar o caminho)

#### Minutos 5-15 (21:33 – 21:43)
**Prioridade**: Ajudar quem travou na leitura de CSV.
- Dica: *"Peça ao Copilot: 'Crie uma função que lê um CSV de transações com as colunas id_transacao, id_cliente, data, tipo, categoria, valor, descricao'"*
- Se alguém travou no caminho: mostrar `os.path.dirname(os.path.abspath(__file__))` e `os.path.join`
- Se alguém está muito rápido: desafiar — *"Adicione tratamento de erros e docstrings"*

#### Minutos 15-25 (21:43 – 21:53)
**Prioridade**: Ajudar com lógica de processamento.
- Problemas comuns: agrupamento por categoria (sugerir `defaultdict`), cálculo de percentual, formatação de saída
- Relembrar: *"Testem a cada nova função! Não esperem ter tudo pronto para testar."*
- **Aviso de tempo** aos 20 min: *"Pessoal, faltam 10 minutos. Se ainda não têm o relatório/output, foquem nisso agora."*

#### Minutos 25-30 (21:53 – 21:58)
**Prioridade**: Fechar o projeto.
- Ajudar quem está lutando com a saída formatada
- Para os mais avançados: *"Salve o relatório em um arquivo .txt usando with open()"*
- **Aviso final**: *"Pessoal, 2 minutos! Executem o código uma última vez para confirmar que funciona."*

> 💡 **Sinais de alerta**: Aluno parado olhando a tela sem digitar → abordar proativamente. Aluno com muitos erros em cascata → sugerir recomeçar do zero com prompts mais simples. Aluno que não está usando o Copilot → relembrar os atalhos.

### 21:58 – 22:00 | Apresentações e Encerramento (2 min)

*"Tempo! Quem conseguiu gerar o relatório? Levantem a mão!"*

> 💡 Comemorar independente do número. Qualquer avanço é válido.

**Se houver voluntários** (2-3 pessoas, 2 min cada):

*"Alguém quer mostrar o que construiu? Pode compartilhar a tela ou eu projeto do seu computador. Não precisa estar perfeito — o importante é o processo."*

**Para cada apresentação, comentar**:
- O que ficou bom (elogiar algo específico)
- Uma sugestão de melhoria (sempre construtiva)
- Destacar se usou alguma técnica da aula (docstrings, tratamento de erros, etc.)

**Se não houver voluntários**:

*"Tudo bem! Vou mostrar rapidamente a solução de referência."*

**Ação**: Executar `python aula2/labs/lab02_solucao.py` (se existir) ou mostrar o output esperado nos slides.

---

# ENCERRAMENTO
## 🕐 22:00 (últimos minutos)

### Recap do Curso Completo

**Ação**: Abrir os slides na seção "Recap Completo do Curso".

*"Vamos recapitular tudo o que vocês aprenderam nessas duas aulas."*

**Ler os tópicos rapidamente**:

*"Na Aula 1: entenderam IA generativa, instalaram o Copilot, aprenderam Python básico, leram CSVs. Na Aula 2: ciclo de desenvolvimento com IA, refatoração, debugging, pipeline de dados, documentação, e construíram um projeto completo."*

*"Vocês saíram de 'o que é IA?' para 'construí um pipeline de dados com IA'. Isso em duas noites. Imaginem o que conseguem fazer com mais tempo e prática."*

### Próximos Passos

**Ação**: Mostrar o slide "Próximos Passos".

*"Para continuar aprendendo: no curto prazo, refaçam os exercícios sem olhar o material. Criem um mini projeto pessoal — pode ser qualquer coisa: organizar suas finanças, analisar dados de um hobby, automatizar algo do trabalho."*

*"No médio prazo, aprendam Pandas para dados, Flask para web, Pytest para testes. E aprofundem em Git e GitHub."*

*"No longo prazo, participem de projetos open source e explorem áreas como APIs e ciência de dados."*

### Fala Motivacional de Encerramento

*"Quero encerrar com uma reflexão. A IA não veio para substituir programadores — ela veio para amplificar quem programa. O diferencial não é saber usar o Copilot. Todo mundo vai saber. O diferencial é saber PENSAR sobre o problema, saber DIVIDIR em partes, saber REVISAR o que a IA gera."*

*"Vocês agora têm uma ferramenta poderosa nas mãos. Usem ela para aprender mais rápido, para prototipar ideias, para resolver problemas reais. Não tenham medo de errar — o Copilot está ali para ajudar a corrigir."*

*"A melhor forma de aprender é construindo. Então construam. Todo dia, um pouquinho. E lembrem: quem dirige são vocês. A IA é só a co-piloto."*

*"Obrigado pela participação de vocês. Foi um prazer! Qualquer dúvida, podem me procurar. Boa noite!"*

### Recursos e Links

**Ação**: Mostrar o slide "Recursos e Links Úteis".

*"Deixo aqui os links para consulta. Tudo está no repositório também, na pasta recursos/links_uteis.md."*

---

## 📝 Notas Pós-Aula

### Itens para verificar após a aula:
- [ ] Salvar logs do chat para referência futura
- [ ] Anotar dúvidas que surgiram e não foram respondidas
- [ ] Anotar o que funcionou e o que não funcionou nas demos
- [ ] Verificar se os alunos que tiveram dificuldade precisam de material extra
- [ ] Coletar feedback (formulário rápido ou conversa informal)

### Ajustes comuns para próximas turmas:
- Se o Bloco 2 ficou longo demais → cortar armadilhas e focar em estratégias
- Se a Demo 03 levou muito tempo → pular a Etapa 2 (consolidação) e focar nas Etapas 4 e 5
- Se o Lab ficou curto → começar o Lab 5 minutos antes
- Se muitos alunos travaram no Lab → na próxima turma, fazer a Opção A juntos nos primeiros 10 min e depois soltar
