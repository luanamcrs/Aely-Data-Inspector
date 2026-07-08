# Aely Data Inspector 📊

> Plataforma inteligente para análise de qualidade de dados, identificação de inconsistências e geração de diagnósticos executivos utilizando Python, Streamlit e Inteligência Artificial.

![Aely Data Inspector](screenshots/dashboard.png)

---

## 📌 Sobre o projeto

O **Aely Data Inspector** é uma aplicação desenvolvida para automatizar uma das etapas mais importantes em projetos de dados: a **análise da qualidade das informações antes da tomada de decisão**.

Bases de dados reais frequentemente possuem problemas como valores ausentes, registros duplicados e inconsistências de preenchimento. Esses problemas podem comprometer análises, indicadores e decisões estratégicas.

O Aely foi criado para facilitar esse processo, permitindo que usuários carreguem uma base de dados, visualizem indicadores de qualidade, encontrem problemas automaticamente e recebam um diagnóstico executivo.

---

# 🚀 Funcionalidades

## 📂 Upload de dados

Permite carregar arquivos:

- CSV
- Excel (.xlsx)

Após o carregamento, a aplicação realiza uma análise inicial da estrutura da base.

---

## 🔎 Análise de Data Quality

O sistema identifica automaticamente:

✅ Valores ausentes  
✅ Registros duplicados  
✅ Inconsistências em dados textuais  
✅ Distribuição dos tipos de dados  
✅ Indicadores gerais da qualidade da base  

---

## 📊 Dashboard de qualidade

A aplicação apresenta:

- Quantidade de registros
- Quantidade de colunas
- Total de células analisadas
- Score de qualidade dos dados
- Quantidade de problemas encontrados

---

## ⚠️ Identificação de problemas

O usuário consegue visualizar uma tabela detalhada contendo:

| Linha | Coluna | Problema | Valor |
|---|---|---|---|
| 15 | Idade | Valor ausente | - |
| 28 | Nome | Espaços extras | " João " |
| 42 | Cliente | Duplicado | Registro repetido |

Essa etapa permite entender exatamente onde estão as inconsistências.

---

## 🤖 Diagnóstico Executivo com IA

Após a análise, o Aely utiliza Inteligência Artificial para gerar uma interpretação dos resultados.

O relatório apresenta:

- Situação geral da qualidade dos dados
- Principais problemas encontrados
- Impactos possíveis
- Recomendações de melhoria

---

## 📄 Exportação de relatórios

A aplicação permite:

- Exportar problemas encontrados em Excel
- Gerar relatório executivo em PDF

---

# 🏗️ Arquitetura do projeto

Fluxo da aplicação:
          Upload CSV/XLSX
                |
                ↓
        Leitura dos dados
                |
                ↓
    Análise de qualidade (Pandas)
                |
                ↓
   Identificação de inconsistências
                |
                ↓
      Dashboard e indicadores
                |
                ↓
      Diagnóstico executivo IA
                |
                ↓
          Relatórios PDF

---

# 🛠️ Tecnologias utilizadas

## Linguagem

- Python

## Manipulação e análise de dados

- Pandas

## Interface

- Streamlit

## Visualização

- Plotly

## Arquivos

- OpenPyXL

## Inteligência Artificial

- Google Gemini API

## Relatórios

- ReportLab

---

# 📁 Estrutura do projeto
Aely-Data-Inspector/

│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── assets/
│ └── style.css
│
├── utils/
│ ├── analysis.py
│ ├── ai.py
│ ├── charts.py
│ ├── export.py
│ ├── pdf.py
│ └── quality.py
│
└── screenshots/
└── dashboard.png

---

# ⚙️ Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/luanamcrs/Aely-Data-Inspector.git
2. Acesse a pasta
cd Aely-Data-Inspector
3. Crie um ambiente virtual
python -m venv .venv

Ative o ambiente:

Windows:

.venv\Scripts\activate
4. Instale as dependências
pip install -r requirements.txt
5. Configure a API de IA

Crie um arquivo .env:

GEMINI_API_KEY=sua_chave_aqui
6. Execute a aplicação
streamlit run app.py
🎯 Objetivos do projeto

Este projeto foi desenvolvido com foco em:

Data Quality
Análise exploratória de dados
Automação de processos analíticos
Aplicação prática de Inteligência Artificial
Construção de ferramentas para suporte à decisão
📚 Aprendizados

Durante o desenvolvimento foram aplicados conceitos de:

Manipulação de dados com Pandas
Construção de dashboards interativos
Organização de projetos Python
Integração com APIs de IA
Geração automática de relatórios
Desenvolvimento de aplicações analíticas
🔮 Próximas melhorias

Possíveis evoluções:

Conexão com bancos de dados
Mais regras de validação de qualidade
Histórico de análises
Pipeline ETL automatizado
Perguntas em linguagem natural sobre os dados
👩‍💻 Autora

Luana

Projeto desenvolvido como parte da minha jornada em Dados, Analytics e Inteligência Artificial.