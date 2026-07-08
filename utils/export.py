from io import BytesIO

import pandas as pd


def export_treated_excel(
    treated_df: pd.DataFrame,
    decisions: list,
) -> BytesIO:
    """
    Exporta a planilha tratada juntamente
    com o histórico das alterações.
    """

    output = BytesIO()

    history = pd.DataFrame(decisions)

    with pd.ExcelWriter(
        output,
        engine="openpyxl",
    ) as writer:

        treated_df.to_excel(
            writer,
            sheet_name="Dados_Tratados",
            index=False,
        )

        history.to_excel(
            writer,
            sheet_name="Historico_Alteracoes",
            index=False,
        )

    output.seek(0)

    return output