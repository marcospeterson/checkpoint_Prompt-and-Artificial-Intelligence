# Prompt Toolkit

Framework educacional desenvolvido em Python para estudo e comparação de técnicas de Prompt Engineering utilizando Large Language Models (LLMs) via API do Ollama.

O projeto executa automaticamente diferentes técnicas de prompting, compara os resultados, mede desempenho e gera relatórios automáticos com gráficos e métricas.

---

# Objetivo do Projeto

O sistema foi desenvolvido para:

- estudar Prompt Engineering;
- comparar técnicas de prompting;
- avaliar desempenho de LLMs;
- automatizar testes de prompts;
- gerar relatórios comparativos;
- analisar acurácia e consistência.

---

# Funcionalidades

- Zero-Shot Prompting
- Few-Shot Prompting
- Chain-of-Thought (CoT)
- Role Prompting
- Avaliação automática de respostas
- Medição de tokens
- Medição de tempo
- Teste de consistência
- Teste de temperatura
- Geração automática de gráficos
- Exportação CSV
- Sistema modular de tarefas

---

# Tecnologias Utilizadas

- Python 3.10+
- Ollama API
- Requests
- Pandas
- Matplotlib
- Tiktoken
- Python Dotenv

---

# Estrutura do Projeto

```text
prompt-toolkit/
├── README.md
├── requirements.txt
├── .env.example
├── main.py
├── src/
│   ├── __init__.py
│   ├── llm_client.py
│   ├── prompt_builder.py
│   ├── techniques.py
│   ├── tasks.py
│   ├── evaluator.py
│   └── report.py
├── data/
│   ├── inputs.json
│   └── examples.json
├── prompts/
│   ├── system_prompts.json
│   └── templates.json
├── output/
│   ├── resultados.csv
│   └── graficos/
└── docs/
```

---

# Como Rodar o Projeto

# 1. Instalar Python

Baixe o Python:

https://www.python.org/downloads/

Durante a instalação:

Marque a opção:

```text id="5w66km"
Add Python to PATH
```

Após instalar, teste:

```bash id="v91hm6"
python --version
```

---

# 2. Instalar Git

Download:

https://git-scm.com/downloads

Teste no terminal:

```bash id="kz3trn"
git --version
```

---

# 3. Clonar o Repositório

Abra o terminal na pasta desejada e execute:

```bash id="4tl2gg"
git clone https://github.com/SEU-USUARIO/prompt-toolkit.git
```

Entrar na pasta do projeto:

```bash id="r7zw9d"
cd prompt-toolkit
```

---

# 4. Criar Ambiente Virtual

## Windows

Criar ambiente virtual:

```bash id="lp2k6x"
python -m venv venv
```

Ativar ambiente virtual:

```bash id="m3n3m0"
venv\Scripts\activate
```

---

## Linux / Mac

Criar ambiente virtual:

```bash id="ys8glr"
python3 -m venv venv
```

Ativar ambiente virtual:

```bash id="6l4kks"
source venv/bin/activate
```

---

# 5. Instalar Dependências

Execute:

```bash id="gj5v7o"
pip install -r requirements.txt
```

---

# Configuração da API do Ollama

O projeto utiliza a API do Ollama para comunicação com modelos LLM.

Acesse o site do Ollama: https://ollama.com/

Depois:

1. Faça login na sua conta
2. Vá em **Settings**
3. Acesse **Keys**
4. Clique em **Add API Key**
5. Gere sua chave de API

Este projeto **não executa o modelo localmente** no computador.

A comunicação com o modelo é feita através de uma URL configurada no arquivo `.env`.

---

# 6. Criar Arquivo `.env`

Na raiz do projeto, crie um arquivo chamado:

```text id="71gtbm"
.env
```

Dentro do arquivo coloque a chave que você criou:

```env id="ulldzt"
OLLAMA_API_KEY=SuaChaveAPIdoOllama
```

---


# Como Executar

Após configurar o `.env`, execute:

```bash id="g9x1sn"
python main.py
```

---

# Fluxo da Execução

Quando o sistema inicia, ele:

1. Carrega:
   - `.env`
   - `inputs.json`
   - `examples.json`
   - `system_prompts.json`

2. Executa:
   - Zero-Shot
   - Few-Shot
   - Chain-of-Thought
   - Role Prompting

3. Para cada:
   - tarefa
   - input
   - técnica

o sistema:
- monta prompts;
- envia prompts para API;
- mede tokens;
- mede tempo;
- calcula acurácia;
- calcula consistência.

4. Ao final:
- gera CSV;
- gera gráficos;
- recomenda melhor técnica;
- executa teste de temperatura.

---

# Técnicas de Prompting

## Zero-Shot

Executa tarefas sem exemplos prévios.

---

## Few-Shot

Executa tarefas utilizando exemplos armazenados em `examples.json`.

---

## Chain-of-Thought

Força o modelo a raciocinar passo a passo antes de responder.

---

## Role Prompting

Utiliza personas definidas em `system_prompts.json`.

---

# Tipos de Tarefas

O projeto possui suporte para:

- Classificação
- Extração
- Sumarização

Exemplos implementados:

- classificação de sentimento;
- extração de dados;
- resumo de tickets.

---

# Arquivos de Configuração

## tasks.py

Define as tarefas do sistema.

---

## examples.json

Armazena exemplos utilizados no Few-Shot.

---

## templates.json

Armazena templates reutilizáveis de prompts.

---

## system_prompts.json

Armazena personas utilizadas no Role Prompting.

---

# Relatórios Gerados

Após a execução, o sistema gera:

```text id="4d0xzk"
output/
├── resultados.csv
└── graficos/
    ├── acuracia.png
    ├── custo.png
    └── temperatura.png
```

---

# Métricas Avaliadas

O sistema mede automaticamente:

- Acurácia
- Tempo de resposta
- Quantidade de tokens
- Consistência
- Desempenho por técnica

---

# Exemplo de Execução

```text id="y2j4m7"
===================================
TAREFA: classificacao_sentimento
===================================

[Zero-Shot]
Resposta: POSITIVO

[Few-Shot]
Resposta: POSITIVO

[Chain-of-Thought]
Resposta: POSITIVO

[Role Prompting]
Resposta: POSITIVO
```

---

# Observações

- O projeto utiliza apenas ferramentas gratuitas.
- É necessário possuir acesso a uma API do Ollama.
- O endereço da API deve ser configurado no `.env`.
- Os gráficos são gerados automaticamente após a execução.

---

# Integrantes

- Nome — RM
- Nome — RM
- Nome — RM

```