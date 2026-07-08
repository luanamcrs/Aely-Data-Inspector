import os

from dotenv import load_dotenv

import google.generativeai as genai


load_dotenv()


API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if API_KEY:

    genai.configure(
        api_key=API_KEY
    )



def generate_local_report(
    summary: dict,
    quality: dict,
):
    """
    Gera relatório automático sem depender da IA.
    """

    score = quality.get(
        "score",
        0
    )

    nulls = quality.get(
        "null_values",
        0
    )

    duplicates = quality.get(
        "duplicate_rows",
        0
    )


    if score >= 90:

        status = (
            "A base apresenta boa qualidade "
            "de dados."
        )

    elif score >= 70:

        status = (
            "A base apresenta qualidade moderada "
            "e necessita de alguns ajustes."
        )

    else:

        status = (
            "A base apresenta problemas relevantes "
            "de qualidade."
        )



    return f"""
## Diagnóstico Executivo Aely

### Situação geral

{status}

O conjunto analisado possui:

- {summary.get("total_rows")} registros;
- {summary.get("total_columns")} colunas;
- {summary.get("total_cells")} células analisadas.

### Indicadores encontrados

Score de qualidade:
**{score}/100**

Valores ausentes:
**{nulls}**

Registros duplicados:
**{duplicates}**

### Recomendações

- Tratar valores ausentes nos campos identificados;
- Revisar registros duplicados;
- Padronizar informações textuais;
- Realizar validações antes da utilização da base.

"""


def generate_executive_report(
    summary: dict,
    quality: dict,
):
    """
    Tenta utilizar Gemini.
    Caso falhe, gera relatório local.
    """


    if not API_KEY:

        return generate_local_report(
            summary,
            quality,
        )



    try:

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )


        prompt = f"""

Gere um diagnóstico executivo profissional
sobre qualidade de dados.

Resumo:

Linhas:
{summary.get("total_rows")}

Colunas:
{summary.get("total_columns")}

Score:
{quality.get("score")}/100

Valores ausentes:
{quality.get("null_values")}

Duplicados:
{quality.get("duplicate_rows")}

Explique situação atual,
problemas encontrados,
impactos e recomendações.

Responda em português.

"""


        response = model.generate_content(
            prompt
        )


        if response and response.text:

            return response.text



    except Exception:

        pass



    # Sempre retorna algo mesmo sem Gemini

    return generate_local_report(
        summary,
        quality,
    )