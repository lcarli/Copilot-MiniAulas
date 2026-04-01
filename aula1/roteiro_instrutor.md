# 🎬 Roteiro do Instrutor — Aula 1

## Desenvolvimento Rápido com Soluções de IA

**Duração total**: 3 horas (19:00 – 22:00)
**Público**: Iniciantes com base em lógica de programação e banco de dados
**Formato**: Presencial / Online síncrono

> Este roteiro é um guia minuto-a-minuto. Use como teleprompter — adapte o tom à sua personalidade, mas siga a estrutura e os tempos.

---

## ✅ Checklist de Preparação (fazer ANTES da aula)

### Ambiente do instrutor
- [ ] VS Code aberto e atualizado
- [ ] Extensão **GitHub Copilot** instalada e logada (ícone visível na barra de status)
- [ ] Extensão **GitHub Copilot Chat** instalada
- [ ] Python 3.10+ instalado e funcionando no terminal integrado (`python --version`)
- [ ] Pasta do projeto `aulaCopilot` aberta no VS Code
- [ ] Terminal integrado do VS Code aberto e testado
- [ ] Tema do VS Code com **bom contraste** (recomendado: Dark+ ou tema com fundo escuro)
- [ ] **Tamanho de fonte ≥ 18px** no editor (Ctrl + = para aumentar)
- [ ] **Tamanho de fonte ≥ 16px** no terminal integrado

### Arquivos prontos
- [ ] `aula1/demos/demo01_hello_copilot.py` — testado e funcionando
- [ ] `aula1/demos/demo02_ler_csv.py` — testado e funcionando
- [ ] `aula1/demos/demo03_relatorio.py` — testado e funcionando
- [ ] `aula1/dados/clientes.csv` — presente e com dados válidos
- [ ] `aula1/dados/transacoes.csv` — presente e com dados válidos
- [ ] `aula1/labs/lab01_instrucoes.md` — revisado

### Backups (Plano B)
- [ ] Cópias dos scripts de demo completos em pasta separada (caso o Copilot não sugira ao vivo)
- [ ] Slides exportados em PDF (caso a internet caia)
- [ ] Capturas de tela das demos executadas (para mostrar resultado esperado)

### Logística
- [ ] Projetor/tela compartilhada testada
- [ ] Link da aula enviado aos alunos (se online)
- [ ] Slides abertos em aba separada do navegador
- [ ] Água e café ☕

---

## Bloco 1 — Abertura e Contexto (19:00 – 19:25) ⏱️ 25 min

### Preparação
- Slide de boas-vindas visível na tela
- VS Code fechado (abrir só quando chegar na demo)
- Estar de pé / câmera ligada, tom animado

### Condução

#### 19:00 – 19:05 | Boas-vindas e apresentação (5 min)

**Fala de abertura (memorizar o tom, não o texto exato):**

> "Boa noite, pessoal! Sejam muito bem-vindos à primeira aula do curso Desenvolvimento Rápido com Soluções de IA. Hoje vocês vão aprender algo que vai mudar completamente a forma como vocês escrevem código. Não é exagero — ao final desta aula, vocês vão sair daqui produzindo código Python real com a ajuda de inteligência artificial. E a melhor parte: é mais fácil do que vocês imaginam."

- Apresente-se brevemente (nome, experiência, algo pessoal para gerar conexão)
- Mostre o slide de agenda e percorra os blocos rapidamente

> "Vamos cobrir bastante coisa hoje, mas tudo de forma prática. Teoria tem, mas demos e mão na massa são o foco."

#### 19:05 – 19:10 | O que é Desenvolvimento Assistido por IA (5 min)

**Avance para o slide "O que é Desenvolvimento Assistido por IA?"**

> "Desenvolvimento assistido por IA é usar ferramentas inteligentes como parceiras no seu trabalho. A IA sugere código, explica trechos, gera testes, encontra bugs. Mas — e isso é fundamental — ela não substitui vocês."

**Use a analogia do slide:**

> "Pensem num co-piloto de avião. Ele monitora instrumentos, sugere rotas, faz cálculos. Mas quem decide e controla o avião é o piloto — que são vocês. A IA é uma ferramenta poderosa, mas não infalível. Vocês continuam sendo os responsáveis pelo código."

🎯 **Ponto de atenção**: Alunos iniciantes podem ter medo de que IA vai "roubar seus empregos". Desmistifique isso logo.

#### 19:10 – 19:18 | Impacto no Mercado de Trabalho (8 min)

**Avance para o slide "Impacto da IA no Mercado de Trabalho"**

> "Vou mostrar alguns dados reais pra vocês. Em 2023, o GitHub publicou uma pesquisa mostrando que desenvolvedores completam tarefas 55% mais rápido usando o Copilot. Cinquenta e cinco por cento! Pensem o que isso significa: o que você faz em 8 horas, poderia fazer em menos de 4."

Percorra os outros dados do slide: Stack Overflow (76%), McKinsey (30%), GitHub (74% menos frustração).

> "Mas o ponto mais importante está aqui embaixo: não é sobre perder empregos. É sobre mudar a forma de trabalhar. Quem souber usar IA vai ter uma vantagem competitiva enorme. E habilidades como pensamento crítico e revisão de código ficam ainda mais importantes — não menos."

**Pergunta de engajamento:**

> 🎤 "Levanta a mão quem aqui já ouviu falar que IA vai substituir programadores. *(pausa)* Pois é, é uma preocupação comum. Mas o que a gente vê na prática é que ela substitui tarefas repetitivas — não pessoas que pensam."

#### 19:18 – 19:23 | O que a IA já faz hoje (5 min)

**Avance para o slide "O que a IA já faz hoje no desenvolvimento"**

Percorra a lista rapidamente, dando um exemplo concreto para cada:

- **Gerar código**: "Você escreve em português o que quer e a IA gera Python, Java, SQL..."
- **Documentar**: "Selecionou uma função e pediu /doc — pronto, docstring gerada."
- **Debugar**: "Colou o erro no chat e em 10 segundos já tem a causa provável."
- **Criar testes**: "Pediu /tests e ela gera os testes unitários."
- **Refatorar**: "Seu código funciona, mas está feio — a IA sugere uma versão mais limpa."
- **Explicar código legado**: "Código antigo que ninguém entende? A IA traduz."

> "Tudo isso já funciona hoje. Não é futuro — é presente."

#### 19:23 – 19:25 | Pergunta de engajamento + transição (2 min)

**Avance para o slide "Pergunta para Engajamento"**

> 🎤 "Agora eu quero saber de vocês: quem já usou alguma IA para qualquer tarefa? Pode ser ChatGPT pra resumir texto, Gemini pra tirar dúvida, qualquer coisa. Levanta a mão! *(ou escreva no chat se for online)*"

*(Espere respostas, comente 2-3, mostre interesse genuíno)*

> "Ótimo! Vocês já estão no caminho. Agora vamos entender como essas ferramentas funcionam por dentro."

**Frase de transição:**

> "Pra usar bem uma ferramenta, ajuda muito entender como ela funciona. Então vamos mergulhar nos fundamentos dos LLMs — os modelos de linguagem que fazem tudo isso acontecer."

### Dicas do Instrutor
- **Tom**: Empolgado, mas acessível. Evite jargões técnicos demais neste bloco.
- **Erro comum**: Gastar tempo demais aqui. Este bloco é motivacional — não aprofunde.
- **Se alguém perguntar sobre uma ferramenta específica**: "Ótima pergunta! Vamos cobrir isso daqui a pouco no bloco de ferramentas."
- **Alunos tímidos**: Se ninguém levantar a mão, dê exemplos do cotidiano — "quem já pediu pro ChatGPT corrigir um e-mail?"

---

## Bloco 2 — Fundamentos de LLMs (19:25 – 19:55) ⏱️ 30 min

### Preparação
- Slides de LLMs prontos
- Ter na cabeça a analogia do "autocomplete turbinado"

### Condução

#### 19:25 – 19:32 | O que é um LLM (7 min)

**Avance para o slide "O que é um LLM"**

> "LLM significa Large Language Model — Modelo de Linguagem de Grande Escala. É um programa de computador treinado com bilhões de textos — livros, sites, repositórios de código, documentação — para entender e gerar linguagem."

**Use a analogia do autocomplete:**

> "Vocês conhecem o autocomplete do celular, né? Você digita 'bom' e ele sugere 'dia'. O LLM é como um autocomplete turbinado: em vez de prever a próxima palavra, ele prevê parágrafos inteiros, com lógica e coerência."

> "Mas atenção: ele não 'entende' como um humano. Ele calcula probabilidades do que vem a seguir. É estatística muito sofisticada."

Mostre a tabela de modelos (GPT-4o, Claude, Gemini, Llama) rapidamente.

**Pergunta de engajamento:**

> 🎤 "Alguém aqui já ouviu falar da diferença entre GPT e ChatGPT? *(pausa)* GPT é o modelo — o cérebro. ChatGPT é a interface — o rosto. É como dizer que o motor é o GPT, e o carro é o ChatGPT."

#### 19:32 – 19:38 | Previsão do Próximo Token (6 min)

**Avance para o slide "Como funciona: Previsão do Próximo Token"**

> "Vamos ver na prática. Quando vocês escrevem `def calcular_total(valores):`, o que o LLM faz?"

Aponte para o diagrama do slide:

> "Ele olha esse texto, analisa os padrões que aprendeu no treinamento, e calcula: 'o que é mais provável de vir depois?' E a resposta mais provável é `return sum(valores)`. Por quê? Porque ele viu milhares de funções parecidas durante o treinamento."

Percorra os 5 passos do processo simplificado.

> "Um detalhe importante: ele NÃO consulta uma base de dados. Não é uma busca no Google. São padrões estatísticos aprendidos. Isso explica por que às vezes ele erra — mais sobre isso daqui a pouco."

#### 19:38 – 19:43 | Conceito de Token (5 min)

**Avance para o slide "Conceito de Token"**

> "Antes de ir adiante: o que é um token? Token é a menor unidade que o LLM processa. Não é exatamente uma palavra."

Mostre a tabela de exemplos:

> "'Olá' é 1 token. 'Olá, mundo!' é 4 tokens. A palavra 'Desenvolvimento' pode ser 2 ou 3 tokens. Uma linha de código Python gasta entre 5 e 15 tokens."

> "Por que isso importa? Porque LLMs têm um limite. O GPT-4o processa até 128 mil tokens — cerca de 300 páginas. Parece muito, mas se você joga um projeto inteiro, pode estourar."

**Analogia útil:**

> "Pensem assim: o LLM tem uma mesa de trabalho. Quanto mais papéis você coloca na mesa, mais difícil fica pra ele achar o que precisa. Se a mesa enche, os papéis mais antigos caem no chão — ele esquece."

#### 19:43 – 19:48 | Contexto e Arquitetura de Interação (5 min)

**Avance para os slides "Arquitetura de Interação" e "O que é Contexto"**

> "Toda conversa com um LLM tem três camadas: o System Prompt — instruções invisíveis que definem o comportamento; o User Prompt — o que vocês escrevem; e a Resposta — o que a IA gera."

> "No Copilot, o System Prompt já vem configurado. Ele sabe que está num editor de código, sabe qual linguagem vocês estão usando. Vocês só precisam se preocupar com o User Prompt — os comentários e o código que vocês escrevem."

**Slide "O que é Contexto"**:

> "Contexto é tudo que a IA enxerga pra gerar a resposta. No Copilot, isso inclui o arquivo que vocês estão editando, os arquivos abertos em outras abas, os comentários, e até o nome do arquivo. Se seu arquivo se chama `calcular_juros.py`, o Copilot já sabe que provavelmente você quer funções financeiras!"

**Dica prática (enfatize):**

> "Três dicas de ouro: mantenham conversas curtas e focadas. Se mudou de assunto, comece um novo chat. E deem nomes descritivos aos arquivos e variáveis — isso melhora muito as sugestões."

#### 19:48 – 19:53 | Limitações e Alucinação (5 min)

**Avance para o slide "Limitações dos LLMs"**

> "Agora a parte que todo mundo precisa saber: onde a IA falha."

**Alucinação (ênfase!):**

> "Alucinação é quando a IA inventa coisas que parecem reais mas são falsas. Ela pode citar uma biblioteca Python que não existe. Pode gerar uma função com parâmetros inventados. E o pior: faz isso com total confiança. Não pisca, não hesita."

**Contexto limitado:**

> "Já falamos sobre a mesa de trabalho: conversa longa, o início se perde."

**Dependência de clareza:**

> "Prompt vago gera resposta vaga. Prompt ambíguo gera resposta imprevisível. A IA não lê sua mente — ela lê seu texto."

> "Então a regra de ouro é: **nunca confie cegamente na IA. Sempre revise, teste e valide.**"

#### 19:53 – 19:55 | Exemplo prático de prompt + transição (2 min)

**Avance para o slide "Mesmo Pedido, Prompts Diferentes"**

> "Olha a diferença: 'faz uma função de banco' versus 'crie uma função Python que recebe uma lista de dicionários com campos cliente e saldo, e retorna apenas os clientes com saldo negativo, ordenados do mais negativo para o menos negativo.' O resultado é completamente diferente!"

Mostre o código do slide rapidamente.

**Frase de transição:**

> "Agora que vocês entendem como os LLMs funcionam por dentro, vamos ver quais ferramentas existem pra aproveitar isso no dia a dia."

### Dicas do Instrutor
- **Ritmo**: Este bloco é conceitual. Não corra, mas também não se perca em detalhes técnicos como attention heads ou transformers.
- **Pergunta frequente**: "Mas o LLM consulta a internet?" → Não. Ele usa padrões do treinamento. Alguns (como o Bing Chat) têm busca integrada, mas o modelo em si não.
- **Pergunta frequente**: "O Copilot vê meu código inteiro?" → Ele vê o arquivo atual e as abas abertas, não o projeto inteiro. Mais sobre isso no bloco do Copilot.
- **Se alguém quiser mais detalhes técnicos**: "Excelente curiosidade! Isso entraria em arquitetura de transformers, que é um curso inteiro. Pra hoje, o modelo mental de 'autocomplete turbinado' é o suficiente."

---

## Bloco 3 — Panorama de Ferramentas (19:55 – 20:15) ⏱️ 20 min

### Preparação
- Slides de ferramentas prontos
- Se possível, ter ChatGPT aberto em outra aba para uma comparação rápida

### Condução

#### 19:55 – 20:00 | Mapa de Ferramentas (5 min)

**Avance para o slide "Mapa de Ferramentas de IA para Desenvolvimento"**

> "Vamos dar um zoom out e ver o cenário completo. Temos ferramentas de IA para devs em várias categorias."

Percorra o mapa:

- **Fora da IDE**: "ChatGPT, Claude, Gemini, Perplexity — vocês abrem no navegador, colam código, conversam."
- **Dentro da IDE**: "Copilot, Cursor, Cody, CodeWhisperer — integradas ao editor, sugerem enquanto vocês digitam."
- **Prototipação**: "Spark, Lovable, Bolt.new, V0 — você descreve o que quer e elas geram apps inteiros."
- **Especialistas**: "Agent Mode do Copilot, Devin — agentes que fazem tarefas de múltiplos passos sozinhos."

> "Muita opção, né? Calma. Hoje vamos focar no GitHub Copilot, que é a ferramenta mais prática pra quem escreve código no dia a dia."

#### 20:00 – 20:05 | ChatGPT e uso conversacional (5 min)

**Avance para o slide "ChatGPT — Uso Conversacional"**

> "O ChatGPT todo mundo já conhece. Pra desenvolvimento, ele é ótimo pra tirar dúvidas conceituais, planejar arquitetura, debugar erros. Você cola o erro, ele explica e sugere correção."

> "Mas o ponto fraco é: ele não tem acesso ao seu código automaticamente. Você precisa copiar e colar. E isso quebra o fluxo de trabalho."

#### 20:05 – 20:12 | Dentro vs Fora da IDE (7 min)

**Avance para o slide "Dentro vs Fora da IDE"**

> "Aqui tá a grande diferença. Olhem esta tabela:"

Percorra os critérios: contexto, velocidade, fluxo, tarefas complexas.

> "Minha recomendação: use as duas abordagens de forma complementar. Planejou a solução? ChatGPT ou Claude. Vai codar? Copilot no VS Code. Dúvida rápida no meio do código? Copilot Chat sem sair do editor."

**Slides rápidos sobre Cursor, Spark, Lovable** (2-3 min):

> "Rapidamente: Cursor é uma IDE inteira com IA nativa — interessante pra quem quer ir além. GitHub Spark cria micro-apps a partir de descrições em linguagem natural. Lovable, Bolt e V0 geram interfaces visuais. Todas são ferramentas válidas, mas para este curso vamos focar no Copilot por ser a mais versátil e acessível."

#### 20:12 – 20:15 | Transição para o intervalo (3 min)

**Pergunta de engajamento:**

> 🎤 "Antes do intervalo — alguém aqui já usou alguma dessas ferramentas? Cursor? Lovable? Pode ser a versão gratuita. *(espere respostas)*"

**Frase de transição:**

> "Perfeito. Vamos fazer uma pausa de 10 minutos. Quando voltarmos, vamos abrir o VS Code e botar a mão na massa com o Copilot. Se alguém ainda não instalou a extensão, aproveita o intervalo pra instalar. *(mostre o slide de instalação rapidamente)*"

### Dicas do Instrutor
- **Tom**: Informativo, mas sem vender nenhuma ferramenta. Seja neutro.
- **Pergunta frequente**: "Qual é a melhor?" → "Depende do uso. Pro dia a dia de codificação, o Copilot integrado ao VS Code é difícil de bater."
- **Não gaste tempo demais**: Este bloco é panorâmico. O foco da aula é o Copilot.

---

## Bloco 4 — Intervalo (20:15 – 20:25) ⏱️ 10 min

### Condução

> "Pessoal, 10 minutos de intervalo. Peguem água, café, alonguem. E se alguém precisa de ajuda pra instalar o Copilot, eu fico aqui nos primeiros 5 minutos."

### O que fazer durante o intervalo
- Ajudar alunos com instalação do Copilot
- Verificar se os arquivos de demo estão prontos
- Abrir o VS Code com a pasta `aulaCopilot` e o terminal integrado
- Criar um arquivo Python em branco para a demo 01 (ou ter um vazio pronto)
- Testar que `python --version` funciona no terminal
- Fechar abas desnecessárias para tela limpa

### Ao retornar

> "Pessoal, vamos voltar! Agora é a parte que eu mais gosto: vamos abrir o VS Code e ver a mágica acontecer ao vivo."

---

## Bloco 5 — GitHub Copilot na Prática (20:25 – 20:55) ⏱️ 30 min

### Preparação
- VS Code aberto na pasta `aulaCopilot`
- Terminal integrado visível
- Extensão do Copilot ativada (ícone na barra de status)
- Nenhum arquivo aberto (tela limpa)

### Condução

#### 20:25 – 20:30 | O que é o Copilot + como instalar (5 min)

**Avance para o slide "O que é o GitHub Copilot"**

> "GitHub Copilot é uma extensão do VS Code que usa IA pra sugerir código em tempo real, direto no editor. O diferencial: funciona enquanto vocês digitam, sem trocar de janela, e entende o contexto do projeto."

**Slide "Plano Free":**

> "E a boa notícia: tem plano gratuito! 2.000 completions e 50 mensagens de chat por mês. Pra aprender e praticar, é mais que suficiente. Estudantes ainda ganham o plano Pro de graça pelo GitHub Student Developer Pack."

**Slide "Como Instalar":**

Percorra os passos rapidamente. Se estiver online:

> "Quem ainda não instalou: abre o VS Code, Ctrl+Shift+X, pesquisa 'GitHub Copilot', instala, faz login com a conta do GitHub. Se o ícone aparecer na barra de status embaixo, funcionou."

#### 20:30 – 20:35 | Features principais (5 min)

**Avance para o slide "Features Principais"**

Demonstre cada feature APONTANDO para o VS Code (sem codar ainda):

> "Primeiro: o **Autocomplete**. Sugestões aparecem em texto cinza enquanto vocês digitam. Tab pra aceitar, Esc pra rejeitar. Alt+] e Alt+[ pra ver outras sugestões."

> "Segundo: o **Copilot Chat** — Ctrl+Shift+I. Um chat integrado no VS Code onde vocês perguntam em português. 'Como faço pra ler um CSV?' e ele responde com código contextualizado."

> "Terceiro: **Comandos rápidos** — /explain, /fix, /tests, /doc. Seleciona um trecho, digita o comando, e pronto."

> "E quarto: o **Agent Mode** — a cereja do bolo. O Copilot planeja e executa tarefas de múltiplos passos. Mas isso é assunto pra aulas futuras."

#### 20:35 – 20:40 | Boas Práticas de Prompting (5 min)

**Avance para o slide "Boas Práticas de Prompting para Copilot"**

> "Antes de codar, regras de ouro para extrair o melhor do Copilot:"

Percorra as 4 práticas do slide com ênfase:

> "**Um**: pedidos pequenos e específicos. Não peça 'faz o sistema bancário'. Peça 'função que calcula juros compostos dado capital, taxa e período'."

> "**Dois**: instruções claras. Não 'processa os dados'. Sim: 'leia o arquivo CSV, filtre linhas onde saldo é menor que zero, ordene por nome'."

> "**Três**: especifique o formato de saída. 'Retorne um dicionário com as chaves total, media, maior, menor.'"

> "**Quatro**: dê contexto com comentários. Comentários são instruções pro Copilot. Comente bem!"

#### 20:40 – 20:43 | Metodologia: Pensar → Dividir → Pedir → Revisar → Testar (3 min)

**Avance para o slide "Metodologia: Copilot Assisted Development"**

> "Essa é a metodologia que vocês vão usar em todo o curso:"

Desenhe no ar (ou aponte pro diagrama):

> "**Pensar**: entenda o problema antes de pedir ajuda. **Dividir**: quebre em tarefas menores — uma função por vez. **Pedir**: escreva prompts claros. **Revisar**: leia o código gerado — ele faz o que vocês esperavam? **Testar**: execute, teste com dados reais e de borda."

> "Gravem isso: **Pensar, Dividir, Pedir, Revisar, Testar**. É seu mantra."

#### 20:43 – 20:55 | DEMO 01 — Hello Copilot 🎯 (12 min)

**Avance para o slide "[DEMO] Hora da Demo!"**

> "Agora chega de teoria. Vamos ver isso funcionando. Acompanhem minha tela!"

### Demo 01: `demo01_hello_copilot.py`

**Passo a passo EXATO:**

1. **No VS Code**, clique em `File > New File`, salve como `demo01_teste.py` dentro de `aula1/demos/`

   > "Reparem que o nome do arquivo já dá contexto pro Copilot."

2. **Digite o comentário** (letra por letra, devagar):
   ```python
   # Peça ao Copilot: "crie uma função que recebe um nome e retorna uma saudação personalizada"
   ```

3. **Pressione Enter** e espere 2-3 segundos. O Copilot deve sugerir algo como:
   ```python
   def saudacao(nome: str) -> str:
       """Retorna uma saudação personalizada com o nome informado."""
       return f"Olá, {nome}! Seja bem-vindo(a) ao curso de desenvolvimento com IA! 🚀"
   ```

   > "Vejam: eu não digitei NADA de código. Escrevi um comentário em português e o Copilot sugeriu a função inteira. Com type hints, docstring e até emoji! *(pausa para efeito)*"

   > "Agora pressiono Tab pra aceitar."

4. **Pressione Tab** para aceitar.

5. **Deixe duas linhas em branco e digite o próximo comentário:**
   ```python
   # Peça ao Copilot: "crie uma função que verifica se um número é par ou ímpar"
   ```

6. **Pressione Enter** e espere a sugestão.

   > "De novo: comentário em português → função completa. Vejam que ele já sabia o padrão: type hints, docstring, if/else."

7. **Aceite com Tab.** Repita para o terceiro comentário:
   ```python
   # Peça ao Copilot: "crie uma função que recebe uma lista de números e retorna estatísticas"
   ```

   > "Essa é mais complexa — uma função que retorna dicionário com média, máximo e mínimo. Vejam como ele trata a lista vazia. Bom código defensivo!"

8. **Adicione o bloco principal.** Digite:
   ```python
   if __name__ == "__main__":
   ```
   E deixe o Copilot sugerir o código de teste.

   > "Até o bloco de testes ele sugere! Ele entendeu que queremos testar as três funções."

9. **Execute no terminal:**
   ```
   python aula1/demos/demo01_teste.py
   ```

   > "E tá funcionando! Código gerado por IA, revisado por humano, testado e aprovado."

**O que destacar:**
- O Copilot leu o comentário em **português** e gerou código correto
- Ele adicionou **type hints** e **docstrings** automaticamente
- O código trata **edge cases** (lista vazia)
- O nome do arquivo e os comentários influenciam as sugestões

**🔧 Plano B — Se o Copilot não sugerir:**
- Verifique se o ícone está ativo na barra de status (sem ❌)
- Tente pressionar `Alt+\` para forçar uma sugestão
- Se persistir, abra o arquivo de backup `demo01_hello_copilot.py`, copie a função e cole, dizendo: "Às vezes o Copilot demora um pouco. Na prática, funciona na grande maioria das vezes. Vou usar o backup pra não perdermos tempo."
- Mostre o código do backup e comente como se tivesse sido gerado ao vivo

**Frase de transição:**

> "Viram como é simples? Comentário em português, Tab e pronto. Agora vamos subir de nível: vamos trabalhar com dados reais — arquivos CSV, como os que vocês vão encontrar no dia a dia."

### Dicas do Instrutor
- **Demo é o momento mais importante da aula.** Não apresse. Deixe o "uau" acontecer.
- **Pause depois que o Copilot sugerir** — deixe os alunos absorverem.
- **Se o Copilot sugerir algo diferente do esperado**: comente! "Olha, ele sugeriu diferente do que eu tinha em mente. Vamos ver se funciona... *(analise ao vivo)*. Funciona! É por isso que a etapa de Revisar é essencial."
- **Velocidade**: Digite devagar. Os alunos estão acompanhando.

---

## Bloco 6 — Python + Copilot: Automação (20:55 – 21:30) ⏱️ 35 min

### Preparação
- VS Code aberto na pasta `aulaCopilot`
- Arquivo `aula1/dados/clientes.csv` presente
- Arquivo `aula1/dados/transacoes.csv` presente
- Terminal integrado visível

### Condução

#### 20:55 – 21:00 | Por que Python para Automação (5 min)

**Avance para o slide "Por que Python para Automação?"**

> "Por que Python? Quatro motivos: sintaxe simples — parece pseudocódigo. Bibliotecas poderosas — csv, pandas, os. Produtividade — menos código pra fazer mais. E a IA adora Python — é a linguagem com mais exemplos de treinamento."

Mostre a tabela de tarefas manuais vs automação:

> "Pensem no dia a dia: abrir planilha e filtrar dados manualmente? Script Python faz em segundos. Conferir saldos um por um? Loop faz em milissegundos. Gerar relatório mensal? Automatizado."

Mostre o exemplo de 5 linhas que processa um CSV:

> "Cinco linhas de Python processam o que levaria horas manualmente. E com o Copilot, vocês nem precisam lembrar a sintaxe."

#### 21:00 – 21:05 | Leitura de CSV e Manipulação de Dados (5 min)

**Avance para os slides "Leitura de Arquivos CSV" e "Manipulação de Listas e Dicionários"**

> "CSV — Comma-Separated Values. Arquivo de texto simples onde cada linha é um registro. É o formato universal para troca de dados."

Mostre o exemplo do slide:

> "Cada linha vira um dicionário Python: `{'nome': 'Ana Silva', 'conta': '1001', 'saldo': 15000.50}`. Pra acessar o nome: `cliente['nome']`. Simples assim."

> "E pra filtrar, somar, ordenar — tudo com list comprehension e funções built-in do Python. Vocês vão ver na prática agora."

#### 21:05 – 21:18 | DEMO 02 — Ler CSV e Filtrar Dados 🎯 (13 min)

**Avance para o slide "[DEMO] Ler clientes.csv e filtrar dados"**

> "Segunda demo! Agora vamos trabalhar com dados reais."

### Demo 02: `demo02_ler_csv.py`

**Passo a passo EXATO:**

1. **Abra o arquivo `aula1/dados/clientes.csv`** primeiro no VS Code.

   > "Primeiro, vamos ver os dados com os quais vamos trabalhar. Olhem: id_cliente, nome, tipo_conta, saldo_atual. Dados bancários fictícios."

2. **Crie um novo arquivo** `demo02_teste.py` em `aula1/demos/`.

3. **Digite o cabeçalho:**
   ```python
   # Leitura de dados bancários a partir de CSV
   # Vamos ler o arquivo clientes.csv usando o módulo csv do Python
   ```

4. **Digite:**
   ```python
   import csv
   import os
   ```

5. **Digite o comentário e espere a sugestão:**
   ```python
   # Função que lê o CSV de clientes e retorna uma lista de dicionários
   ```

   > "Vejam: o Copilot sabe que estamos trabalhando com CSV bancário — o contexto do comentário e o arquivo aberto ajudam."

   O Copilot deve sugerir a função `carregar_clientes`. Aceite com Tab.

   > "Reparem que ele converteu o saldo para float automaticamente. Ele sabe que pra fazer cálculos, precisa ser número."

6. **Continue com os próximos comentários, um por vez:**
   ```python
   # Função que retorna a lista de nomes de todos os clientes
   ```
   *(Aceite a sugestão)*

   ```python
   # Função que filtra clientes pelo tipo de conta
   ```
   *(Aceite a sugestão)*

   ```python
   # Função que retorna o cliente com o maior saldo
   ```
   *(Aceite a sugestão)*

   > "Quatro funções, quatro comentários. Zero digitação de lógica."

7. **Adicione o bloco principal.** O Copilot deve sugerir os testes. Se não sugerir completo, use o arquivo de backup como referência.

8. **Execute:**
   ```
   python aula1/demos/demo02_teste.py
   ```

   > "Total de clientes, lista de nomes, filtro por tipo de conta, e o cliente com maior saldo. Tudo funcionando."

**O que destacar:**
- O módulo `csv.DictReader` transforma linhas em dicionários
- A conversão de `str` para `float` é necessária e o Copilot faz automaticamente
- O caminho relativo com `os.path.join` e `os.path.dirname(__file__)` é uma boa prática
- As funções são pequenas e focadas — seguindo a metodologia Dividir

**🔧 Plano B:**
- Se o CSV não for encontrado: verifique o caminho. Use `os.path.join(os.path.dirname(__file__), '..', 'dados', 'clientes.csv')`
- Se o Copilot travar: abra `demo02_ler_csv.py` como backup e percorra o código explicando
- Diga: "O resultado é idêntico ao que o Copilot geraria. Vou mostrar a lógica passo a passo."

**Pergunta de engajamento:**

> 🎤 "Quem aqui já trabalhou com arquivos CSV no dia a dia? Planilhas exportadas, relatórios, dados de sistema? *(espere respostas)* Pois é — Python + Copilot automatiza tudo isso."

#### 21:18 – 21:28 | DEMO 03 — Relatório de Transações 🎯 (10 min)

**Avance para o slide "[DEMO] Gerar relatório de transações"**

> "Agora vamos escalar. Vamos cruzar dois arquivos CSV e gerar um relatório profissional."

### Demo 03: `demo03_relatorio.py`

**Passo a passo EXATO:**

1. **Abra `aula1/dados/transacoes.csv`** rapidamente para mostrar a estrutura.

   > "Temos transações com id, id_cliente, data, tipo (débito/crédito), categoria, valor e descrição. Vamos cruzar isso com os clientes."

2. **Abra o arquivo `demo03_relatorio.py`** diretamente (este é mais complexo — melhor usar o arquivo pronto e percorrer o código).

   > "Essa demo é um pouco mais complexa, então vou abrir o script pronto e percorrer com vocês, mostrando como cada parte foi construída com o Copilot."

3. **Percorra as funções**, explicando cada uma:

   - `carregar_csv`: "Função genérica que lê qualquer CSV. O Copilot generalizou o que fizemos na demo anterior."
   - `calcular_totais`: "Soma débitos e créditos separadamente usando list comprehension com filtro."
   - `agrupar_por_categoria`: "Usa `defaultdict` — uma estrutura que cria chaves automaticamente. Muito útil pra agrupamentos."
   - `encontrar_maior_transacao`: "Usa `max` com `key` — o mesmo padrão da demo anterior."
   - `buscar_nome_cliente`: "Busca simples por ID. Em banco de dados seria um JOIN — aqui fazemos manual."

4. **Execute:**
   ```
   python aula1/demos/demo03_relatorio.py
   ```

   > "Olhem esse relatório: resumo geral com total de transações, débitos, créditos e saldo. Top 5 categorias. Maior transação com detalhes. Tudo formatado profissionalmente."

   > "Imaginem quanto tempo levaria pra fazer isso manualmente numa planilha. Com Python e Copilot: minutos."

**O que destacar:**
- Cruzamento de dados entre dois CSVs (similar a JOIN em SQL)
- Uso de `defaultdict` para agrupamento
- Formatação profissional com alinhamento e emojis
- O padrão `if __name__ == "__main__"` para scripts executáveis

**🔧 Plano B:**
- Se der erro de arquivo não encontrado: ajuste o caminho no terminal
- Se der erro de encoding: adicione `encoding='utf-8'` na abertura do arquivo
- Se não tiver tempo para executar: mostre o print de uma execução anterior (captura de tela)

#### 21:28 – 21:30 | Transição para o Lab (2 min)

> "Viram as três demos? Começamos com funções simples, passamos por leitura de CSV, e chegamos num relatório completo. Agora é a vez de vocês!"

**Frase de transição:**

> "Nos próximos 30 minutos, vocês vão fazer um exercício prático. Vão usar tudo o que vimos — comentários como prompts, Copilot pra gerar código, e a metodologia Pensar-Dividir-Pedir-Revisar-Testar. Eu vou circular pra ajudar."

### Dicas do Instrutor
- **Nas demos, sempre execute o código.** Alunos precisam ver o resultado no terminal.
- **Se o resultado for diferente do esperado**: não entre em pânico. Analise ao vivo e mostre como debugar — isso é mais valioso que uma demo perfeita.
- **Velocidade das demos**: Demo 02 pode ser mais rápida se o tempo estiver apertado. Demo 03 pode ser walkthrough (mostrar código pronto) em vez de live coding.
- **Pergunta frequente**: "Precisa de pandas?" → "Não! Pra este nível, o módulo `csv` da biblioteca padrão é suficiente. Pandas é poderoso mas adiciona complexidade."

---

## Bloco 7 — Lab Prático (21:30 – 22:00) ⏱️ 30 min

### Preparação
- Arquivo `aula1/labs/lab01_instrucoes.md` aberto ou projetado
- Alunos com VS Code aberto e Copilot ativo
- Arquivo `aula1/dados/transacoes.csv` disponível

### Condução

#### 21:30 – 21:35 | Apresentação do exercício (5 min)

**Projete ou compartilhe o arquivo `lab01_instrucoes.md`**

> "O exercício é o seguinte: vocês vão criar um script Python que analisa as transações bancárias do arquivo CSV e gera um resumo no terminal."

Percorra os requisitos:

> "O que vocês precisam fazer:"
> 1. "Criar um arquivo novo: `lab01_minha_solucao.py` na pasta `labs/`"
> 2. "Ler o arquivo `transacoes.csv`"
> 3. "Calcular total de débitos e créditos"
> 4. "Identificar a categoria com maior gasto"
> 5. "Encontrar o cliente com mais transações"
> 6. "Imprimir um resumo formatado"

**Mostre a saída esperada** do slide:

> "O resultado deve ficar mais ou menos assim: totais de débito e crédito, gastos por categoria, categoria com maior gasto, e cliente com mais transações."

**Dica de como começar:**

> "Lembrem da metodologia: primeiro **pensem** no problema. Depois **dividam** em funções — uma pra ler o CSV, uma pra calcular totais, uma pra agrupar, uma pra imprimir. Depois **peçam** pro Copilot, uma função por vez. **Revisem** o código. E **testem**."

> "E lembrem: escrevam comentários em português descrevendo o que querem. O Copilot vai fazer o resto."

**Mostrar os exemplos de prompts:**

> "Esses comentários são um bom ponto de partida:"
> - `# Ler arquivo CSV de transações bancárias`
> - `# Calcular total de débitos e créditos`
> - `# Agrupar transações por categoria e somar valores`

#### 21:35 – 21:55 | Tempo de trabalho (20 min)

> "Pessoal, mãos à obra! Vocês têm 20 minutos. Eu vou circular pra tirar dúvidas. Se estiver online, me chamem pelo chat."

**O que fazer durante o lab:**

1. **Circule pela sala** (ou monitore o chat) ativamente
2. **Não dê a resposta** — direcione com perguntas:
   - "O que esse erro tá dizendo?" (em vez de corrigir direto)
   - "Tenta escrever um comentário descrevendo o que você quer que essa parte faça"
   - "Lembra da função que vimos na demo? Tenta pedir algo parecido pro Copilot"
3. **Erros comuns** a observar:
   - Esquecer de converter `valor` de string para float → "Olha o tipo do dado que veio do CSV"
   - Caminho do CSV errado → "Use `../dados/transacoes.csv` a partir da pasta labs"
   - Divisão por zero → "E se não tiver nenhuma transação de crédito?"
   - Encoding UTF-8 → "Adiciona `encoding='utf-8'` no `open()`"
4. **Aos 10 minutos**, faça um checkpoint:
   > "Pessoal, metade do tempo! Quem já conseguiu ler o CSV levanta a mão. *(avalie o progresso)*"
   > Se poucos progrediram: "Vou mostrar como começar — abram um arquivo novo e escrevam este comentário..."

5. **Aos 15 minutos**, se alguém travou:
   > "Quem tá travado: abre o Copilot Chat (Ctrl+Shift+I) e pergunta: 'como leio um arquivo CSV em Python e calculo a soma por categoria?'"

#### 21:55 – 22:00 | Encerramento e Recap (5 min)

**Peça para 1-2 alunos mostrarem suas soluções** (se presencial):

> "Alguém quer compartilhar a tela e mostrar o que fez? Não precisa estar perfeito!"

*(Se ninguém se voluntariar, mostre você mesmo uma solução usando o código da demo 03 como referência)*

**Recap rápido — avance para o slide "Recap":**

> "Vamos relembrar o que vimos hoje:"

> "**Conceitos**: o que é desenvolvimento assistido por IA, como funcionam os LLMs — tokens, contexto, previsão — e as limitações da IA, especialmente a alucinação."

> "**Ferramentas**: ChatGPT pra conversa, Copilot pra código, e o panorama de tudo que existe."

> "**Prática**: instalamos o Copilot, criamos funções do zero com comentários, lemos CSV, geramos relatórios. Tudo com Python e IA."

> "E a mensagem mais importante do dia: **A IA é tão boa quanto o prompt que você dá e a revisão que você faz.**"

**Preview da próxima aula:**

> "Na aula 2, vamos subir mais um nível: SQL com Copilot. Criação de tabelas, consultas, joins — tudo assistido por IA. E vamos trabalhar com banco de dados SQLite direto no Python. Tragam as mesmas ferramentas instaladas."

**Encerramento:**

> "Referências e links úteis estão nos slides. Pratiquem com o Copilot Free até a próxima aula — quanto mais usarem, melhor ficam."

> "A frase do dia: *'O melhor momento para começar a usar IA no desenvolvimento foi ontem. O segundo melhor momento é agora.'*"

> "Obrigado, pessoal! Até a próxima aula! 🚀"

### Dicas do Instrutor
- **Se o tempo estiver apertado**: reduza o lab para 20 min e faça o recap em 3 min.
- **Se os alunos estiverem avançados**: incentive os desafios extras (média por categoria, transação de maior valor).
- **Se os alunos estiverem travados**: faça live coding da solução nos últimos 5 minutos, pedindo que acompanhem.
- **Alunos que terminaram cedo**: peça que ajudem colegas ou tentem os desafios extras.
- **NÃO pule o recap** — ele ancora o aprendizado.

---

## 📋 Resumo de Tempos

| Horário | Bloco | Duração |
|---------|-------|---------|
| 19:00 – 19:25 | Abertura e Contexto | 25 min |
| 19:25 – 19:55 | Fundamentos de LLMs | 30 min |
| 19:55 – 20:15 | Panorama de Ferramentas | 20 min |
| 20:15 – 20:25 | ☕ Intervalo | 10 min |
| 20:25 – 20:55 | GitHub Copilot na Prática + Demo 01 | 30 min |
| 20:55 – 21:30 | Python + Copilot: Automação + Demos 02/03 | 35 min |
| 21:30 – 22:00 | Lab Prático + Encerramento | 30 min |

---

## 🚨 Planos de Contingência

### Se a internet cair:
- Use slides em PDF (preparados previamente)
- Demos: abra os arquivos de backup e percorra o código como walkthrough
- Lab: peça para os alunos escreverem a solução sem o Copilot e depois testem quando a internet voltar

### Se o Copilot não funcionar para algum aluno:
- Verifique login no GitHub e se o plano Free está ativo
- Verifique se a extensão está instalada e atualizada
- Reinicie o VS Code
- Último recurso: o aluno pode usar o ChatGPT no navegador para gerar o código e colar no VS Code

### Se o tempo estiver apertado:
- Bloco 3 (Ferramentas): reduza para 10 min — pule Cursor/Lovable e foque no "Dentro vs Fora da IDE"
- Demo 03: faça walkthrough em vez de live coding
- Lab: reduza para 20 min

### Se os alunos estiverem mais avançados que o esperado:
- Aprofunde nas demos (peça que eles sugiram variações)
- No lab, incentive os desafios extras
- Introduza conceitos do Agent Mode do Copilot (preview da aula 2+)

### Se os alunos estiverem mais iniciantes que o esperado:
- Desacelere as demos — explique cada linha de Python
- No lab, faça live coding guiado (todos fazem junto com você)
- Foque nos conceitos básicos de Python (listas, dicionários, for, if) antes de avançar

---

> **Lembrete final**: O roteiro é um guia, não uma prisão. Adapte ao ritmo da turma, responda dúvidas com calma e lembre-se: se os alunos saírem da aula usando o Copilot com confiança, a aula foi um sucesso. 🎯
