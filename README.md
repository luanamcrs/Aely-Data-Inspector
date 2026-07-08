<img width="1897" height="910" alt="Captura de tela 2026-07-07 224504" src="https://github.com/user-attachments/assets/5cd14099-142a-4c52-b8f5-5faf7cf73091" />
# 📊 Aely Data Inspector

<p align="center">

**Plataforma inteligente para análise de qualidade de dados com Python, Streamlit e Inteligência Artificial.**

Analise arquivos CSV e Excel, identifique inconsistências automaticamente, visualize indicadores de qualidade e gere diagnósticos executivos em poucos segundos.

</p>

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 📸 Demonstração

## Home

![Home](screenshots/home.png)

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Análise de Problemas

![Problemas](screenshots/IdentificaErros.png)

## Relatório Executivo

![Relatório](screenshots/ia.png)

---

# 🎯 Sobre o projeto

O **Aely Data Inspector** foi desenvolvido para automatizar uma das etapas mais importantes de qualquer projeto de dados: a **avaliação da qualidade das informações antes da tomada de decisão**.

Bases de dados reais frequentemente apresentam problemas como:

- valores ausentes;
- registros duplicados;
- inconsistências de preenchimento;
- diferentes tipos de dados;
- informações incompletas.

Essas falhas comprometem dashboards, modelos analíticos e decisões de negócio.

O objetivo do projeto é fornecer uma ferramenta simples, intuitiva e automatizada para identificar esses problemas e gerar uma visão executiva da qualidade da base.

---

# ✨ Funcionalidades

## 📂 Upload de arquivos

Suporte para:

- CSV
- Excel (.xlsx)

---

## 📊 Dashboard de Data Quality

Após o upload são apresentados indicadores como:

- Total de linhas
- Total de colunas
- Total de células
- Score de qualidade
- Valores ausentes
- Registros duplicados

---

## 🔎 Identificação automática de problemas

O sistema identifica automaticamente:

- Valores ausentes
- Registros duplicados
- Inconsistências em dados textuais
- Distribuição dos tipos de dados
- Problemas encontrados por coluna

Os resultados são exibidos em uma tabela organizada para facilitar a inspeção.

---

## 📈 Visualizações

O dashboard apresenta gráficos interativos utilizando Plotly.

- Distribuição de valores ausentes
- Distribuição dos tipos de dados

---

## 🤖 Diagnóstico Executivo com IA

Utilizando a API do Google Gemini, o sistema gera automaticamente um relatório contendo:

- Situação geral da qualidade dos dados
- Principais problemas encontrados
- Impactos para o negócio
- Recomendações de melhoria

Caso o limite da API seja atingido, o sistema trata a exceção e informa o usuário sem interromper a aplicação.

---

## 📄 Exportação

É possível exportar:

- Relatório de problemas em Excel
- Relatório executivo em PDF

---

# 🏗️ Fluxo da aplicação

```text
Upload CSV/XLSX
        │
        ▼
Leitura da Base
        │
        ▼
Análise de Qualidade
        │
        ▼
Identificação de Problemas
        │
        ▼
Dashboard Interativo
        │
        ▼
Diagnóstico com IA
        │
        ▼
Exportação dos Relatórios
```

---

# 🛠️ Tecnologias

| Tecnologia | Finalidade |
|------------|------------|
| Python | Desenvolvimento |
| Pandas | Manipulação de dados |
| Streamlit | Interface Web |
| Plotly | Visualizações |
| OpenPyXL | Exportação Excel |
| ReportLab | Geração de PDF |
| Google Gemini API | Diagnóstico Executivo |

---

# 📁 Estrutura do projeto

```text
Aely-Data-Inspector/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── assets/
│   └── style.css
│
├── utils/
│   ├── analysis.py
│   ├── ai.py
│   ├── charts.py
│   ├── export.py
│   ├── pdf.py
│   └── quality.py
│
└── screenshots/
    ├── dashboard.png
    ├── problems.png
    └── report.png
```

---

# ⚙️ Como executar

## Clone o projeto

```bash
git clone https://github.com/luanamcrs/Aely-Data-Inspector.git
```

Entre na pasta:

```bash
cd Aely-Data-Inspector
```

---

## Crie um ambiente virtual

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Configure a API do Gemini

Crie um arquivo `.env`

```env
GEMINI_API_KEY=sua_chave_aqui
```

---

## Execute

```bash
streamlit run app.py
```

---

# 💡 Principais aprendizados

Durante o desenvolvimento foram aplicados conceitos de:

- Data Quality
- Data Analysis
- Pandas
- Streamlit
- Plotly
- Organização de projetos Python
- Consumo de APIs
- Inteligência Artificial Generativa
- Geração de relatórios em PDF

---

# 🚀 Próximas melhorias

- Integração com bancos de dados
- Histórico de análises
- Novas regras de validação
- Pipeline ETL
- Perguntas em linguagem natural sobre a base
- Deploy em nuvem

---

# 👩‍💻 Autora

**Luana Monteiro**

Estudante de Tecnologia em Informática para Negócios, com foco em Dados, Analytics e Inteligência Artificial.

Desenvolvi o **Aely Data Inspector** como projeto de portfólio para demonstrar conhecimentos em análise de dados, visualização, desenvolvimento de aplicações e integração com IA.

---

⭐ Se este projeto foi interessante para você, considere deixar uma estrela no repositório.
