import pandas as pd

from utils.analysis import analyze_data_quality



def compare_quality(
    original_df: pd.DataFrame,
    treated_df: pd.DataFrame,
) -> dict:
    """
    Compara a qualidade dos dados
    antes e depois do tratamento.
    """


    before = analyze_data_quality(
        original_df
    )


    after = analyze_data_quality(
        treated_df
    )


    return {

        "before": before,

        "after": after,

        "score_gain": (
            after.get("score", 0)
            -
            before.get("score", 0)
        ),

        "nulls_removed": (
            before.get("null_values", 0)
            -
            after.get("null_values", 0)
        ),

        "duplicates_removed": (
            before.get("duplicate_rows", 0)
            -
            after.get("duplicate_rows", 0)
        ),

    }



def generate_quality_summary(
    comparison: dict,
) -> dict:
    """
    Retorna somente os indicadores
    necessários para apresentação.
    """


    before = comparison["before"]

    after = comparison["after"]


    return {

        "score_before": before["score"],

        "score_after": after["score"],

        "score_gain": comparison["score_gain"],

        "nulls_before": before["null_values"],

        "nulls_after": after["null_values"],

        "duplicates_before": before["duplicate_rows"],

        "duplicates_after": after["duplicate_rows"],

    }