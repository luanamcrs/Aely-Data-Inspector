from streamlit.runtime.uploaded_file_manager import UploadedFile

import pandas as pd


def load_data(file: UploadedFile) -> pd.DataFrame:
    """
    Lê um arquivo CSV ou Excel e retorna um DataFrame.
    """

    file_name = file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(file)

    if file_name.endswith(".xlsx"):
        return pd.read_excel(file)

    raise ValueError("Formato de arquivo não suportado.")


def get_dataset_summary(df: pd.DataFrame) -> dict:
    """
    Retorna um resumo geral da base de dados.
    """

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_cells = total_rows * total_columns

    return {
        "total_rows": total_rows,
        "total_columns": total_columns,
        "total_cells": total_cells,
    }


def analyze_data_quality(df: pd.DataFrame) -> dict:
    """
    Analisa a qualidade geral dos dados.
    """

    total_cells = df.shape[0] * df.shape[1]

    null_values = int(df.isna().sum().sum())

    duplicate_rows = int(df.duplicated().sum())

    empty_columns = [
        column
        for column in df.columns
        if df[column].isna().all()
    ]

    single_value_columns = [
        column
        for column in df.columns
        if df[column].nunique(dropna=False) == 1
    ]

    column_types = {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }

    unique_values = {
        column: int(df[column].nunique(dropna=True))
        for column in df.columns
    }

    fill_percentage = {
        column: round(df[column].notna().mean() * 100, 2)
        for column in df.columns
    }

    score = 100

    if total_cells > 0:
        score -= (null_values / total_cells) * 40

    if len(df) > 0:
        score -= (duplicate_rows / len(df)) * 30

    score -= len(empty_columns) * 10
    score -= len(single_value_columns) * 5

    score = max(0, round(score))

    return {
        "null_values": null_values,
        "duplicate_rows": duplicate_rows,
        "empty_columns": empty_columns,
        "single_value_columns": single_value_columns,
        "column_types": column_types,
        "unique_values": unique_values,
        "fill_percentage": fill_percentage,
        "score": score,
    }


def find_data_issues(df: pd.DataFrame) -> list:
    """
    Encontra problemas específicos da base.

    Retorna somente:
    linha
    coluna
    tipo
    valor
    """

    issues = []

    # Valores ausentes
    for column in df.columns:
        missing_rows = df[df[column].isna()].index

        for row in missing_rows:
            issues.append(
                {
                    "linha": int(row) + 1,
                    "coluna": column,
                    "tipo": "Valor ausente",
                    "valor": None,
                }
            )

    # Espaços extras em textos
    for column in df.select_dtypes(include="object").columns:

        for row, value in df[column].items():

            if isinstance(value, str) and value != value.strip():

                issues.append(
                    {
                        "linha": int(row) + 1,
                        "coluna": column,
                        "tipo": "Espaços extras",
                        "valor": value,
                    }
                )

    # Linhas duplicadas
    duplicated_rows = df[df.duplicated(keep=False)]

    for row in duplicated_rows.index:

        issues.append(
            {
                "linha": int(row) + 1,
                "coluna": "Linha completa",
                "tipo": "Duplicado",
                "valor": "Registro repetido",
            }
        )

    return issues
