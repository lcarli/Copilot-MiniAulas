# 🔧 Lab 1 — Refatoração com Copilot

**Tempo estimado:** ~15 minutos

## Objetivo

Praticar o uso do GitHub Copilot para **identificar problemas** em código legado e **refatorar** para um código limpo, organizado e robusto.

---

## Contexto

Você herdou o código abaixo de um colega que saiu da empresa. O código funciona, mas é difícil de entender, manter e estender. Sua missão é refatorá-lo com a ajuda do Copilot.

---

## Código Original (copie para um arquivo `.py`)

```python
import csv

a = "../../aula1/dados/clientes.csv"
f = open(a, encoding="utf-8")
r = csv.reader(f)
h = next(r)
t = 0
c = 0
x = []
b = {}
for l in r:
    s = float(l[6])
    t = t + s
    c = c + 1
    x.append(s)
    ag = l[3]
    if ag in b:
        b[ag] = b[ag] + s
    else:
        b[ag] = s
    if s > 10000:
        print("ALERTA: " + l[1] + " tem saldo " + str(s))
    if s < 0:
        print("NEGATIVO: " + l[1] + " saldo " + str(s))
f.close()
m = t / c
print("Total: " + str(t))
print("Media: " + str(m))
print("Qtd: " + str(c))
x.sort()
print("Menor: " + str(x[0]))
print("Maior: " + str(x[-1]))
for k in b:
    print("Agencia " + k + ": R$ " + str(b[k]))
```

---

## Problemas deste Código

Antes de começar, observe os problemas:

- ❌ Variáveis com nomes sem significado (`a`, `f`, `r`, `h`, `t`, `c`, `x`, `b`, `l`, `s`, `m`, `k`)
- ❌ Código monolítico — tudo em um bloco só
- ❌ Sem funções
- ❌ Sem tratamento de exceções (e se o arquivo não existir?)
- ❌ Prints misturados com lógica de negócio
- ❌ Sem docstrings ou comentários explicativos
- ❌ Recurso de arquivo não usa `with` (gerenciador de contexto)

---

## Tarefas

### 1. Copie o código para um novo arquivo

Crie o arquivo `aula2/labs/lab01_meu_codigo.py` e cole o código acima.

### 2. Peça ao Copilot para identificar problemas

No chat do Copilot, use prompts como:

> "Analise este código e liste todos os problemas de qualidade, legibilidade e boas práticas."

> "Quais são os code smells neste código?"

### 3. Refatore em funções com nomes claros

Peça ao Copilot:

> "Refatore este código criando funções separadas para cada responsabilidade. Use nomes descritivos para variáveis e funções."

Sugestão de funções:
- `carregar_clientes(caminho)` → lê o CSV e retorna lista de dicts
- `calcular_estatisticas(clientes)` → retorna total, média, menor, maior
- `agrupar_por_agencia(clientes)` → retorna dict com totais por agência
- `verificar_alertas(clientes)` → retorna lista de alertas
- `exibir_relatorio(...)` → imprime tudo formatado

### 4. Adicione tratamento de exceções

> "Adicione tratamento de exceções para arquivo não encontrado e dados inválidos."

- `FileNotFoundError` para arquivo inexistente
- `ValueError` para dados numéricos inválidos
- Bloco `try/except` nos pontos críticos

### 5. Adicione docstrings

> "Adicione docstrings em todas as funções seguindo o padrão Google Style."

---

## Checklist de Conclusão

- [ ] Variáveis têm nomes descritivos
- [ ] Código dividido em funções com responsabilidade única
- [ ] Usa `with` para abrir arquivos
- [ ] Tratamento de `FileNotFoundError`
- [ ] Tratamento de `ValueError` para conversão numérica
- [ ] Todas as funções possuem docstrings
- [ ] Prints separados da lógica de negócio
- [ ] Código executa sem erros com os dados existentes

---

## Dica

Compare seu resultado com a solução de referência em `lab01_solucao.py` depois de terminar!
