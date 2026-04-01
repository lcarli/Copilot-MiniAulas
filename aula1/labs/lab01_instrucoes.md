# Lab 1 — Análise de Transações Bancárias com Copilot

## 🎯 Objetivo

Usando o **GitHub Copilot** como assistente, criar um script Python que analise as transações bancárias do arquivo CSV e gere um resumo no terminal.

## ⏱️ Tempo estimado

~30 minutos

---

## 📋 O que você vai fazer

1. **Criar um novo arquivo** `lab01_minha_solucao.py` dentro da pasta `aula1/labs/`
2. **Ler o arquivo** `transacoes.csv` (dica: use o módulo `csv` do Python)
3. **Calcular o total** de transações de **débito** e **crédito** separadamente
4. **Identificar qual categoria** teve o maior gasto total
5. **Encontrar o cliente** (`id_cliente`) com o maior volume de transações
6. **Imprimir um resumo formatado** no terminal

---

## 🤖 Como usar o Copilot

- **Escreva comentários** descrevendo o que você quer fazer — o Copilot vai sugerir o código
- **Exemplos de prompts** que podem ajudar:
  - `# Ler arquivo CSV de transações bancárias`
  - `# Calcular total de débitos e créditos`
  - `# Agrupar transações por categoria e somar valores`
  - `# Encontrar o cliente com mais transações`
  - `# Imprimir resumo formatado`
- **Revise sempre** o código gerado antes de aceitar a sugestão
- Lembre do fluxo: **Pensar → Dividir → Pedir → Revisar → Testar**

---

## 💡 Dicas

- Use `encoding='utf-8'` ao abrir arquivos para evitar problemas com acentos
- Os valores no CSV são strings — converta para `float` com `float(valor)`
- Use **dicionários** para agrupar dados por categoria (ex: `gastos_por_categoria = {}`)
- O caminho do CSV é relativo: `../dados/transacoes.csv` (partindo da pasta `labs/`)
- O módulo `csv` já vem instalado no Python, não precisa instalar nada

---

## 📤 Saída esperada

Seu script deve imprimir algo parecido com isto:

```
========================================
   RESUMO DE TRANSAÇÕES BANCÁRIAS
========================================

💰 Total de DÉBITOS:  R$ XXXXX.XX
💳 Total de CRÉDITOS: R$ XXXXX.XX

📊 Gastos por categoria:
   alimentacao:    R$ XXXX.XX
   transporte:     R$ XXXX.XX
   ...

🏆 Categoria com maior gasto: XXXXXXX (R$ XXXX.XX)

👤 Cliente com mais transações: ID X (XX transações)
```

---

## 🚀 Desafio extra (se sobrar tempo)

Se terminar antes, tente adicionar:

1. **Média de gastos por categoria** — divida o total de cada categoria pela quantidade de transações daquela categoria
2. **Transação de maior valor** — encontre a transação com o maior valor absoluto e mostre todos os seus detalhes (id, cliente, data, tipo, categoria, valor e descrição)

---

## ✅ Entrega

Mostre seu script **funcionando** ao instrutor. Ele vai verificar:

- [ ] O script roda sem erros
- [ ] Totais de débito e crédito estão corretos
- [ ] A categoria com maior gasto está identificada
- [ ] O cliente com mais transações está correto
- [ ] O resumo está formatado e legível

---

> **Lembre-se:** O Copilot é um assistente, não uma resposta pronta. Use-o para acelerar seu trabalho, mas entenda cada linha de código que ele sugerir! 🧠
