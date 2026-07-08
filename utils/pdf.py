from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


def format_ai_report(report: str, elements, styles):
    """
    Organiza a resposta da IA em seções profissionais.
    """

    sections = {
        "Diagnóstico Executivo": [],
        "Principais Problemas": [],
        "Impacto para o Negócio": [],
        "Recomendações": [],
    }

    current_section = None

    for line in report.split("\n"):

        line = line.strip()

        if not line:
            continue


        clean_title = (
            line
            .replace("#", "")
            .strip()
        )


        if clean_title in sections:

            current_section = clean_title

            elements.append(
                Spacer(1, 12)
            )

            elements.append(
                Paragraph(
                    clean_title,
                    styles["Heading2"],
                )
            )

            continue


        if current_section:

            if line.startswith("-"):

                line = line.replace(
                    "-",
                    "•",
                    1,
                )

            sections[current_section].append(line)


    for title, content in sections.items():

        if content:

            elements.append(
                Paragraph(
                    title,
                    styles["Heading2"],
                )
            )

            for item in content:

                elements.append(
                    Paragraph(
                        item,
                        styles["BodyText"],
                    )
                )

                elements.append(
                    Spacer(1, 5)
                )



def generate_pdf(
    summary: dict,
    quality: dict,
    report: str,
) -> BytesIO:
    """
    Gera relatório executivo em PDF.
    """

    buffer = BytesIO()


    document = SimpleDocTemplate(
        buffer
    )


    styles = getSampleStyleSheet()


    elements = []


    # Cabeçalho

    elements.append(
        Paragraph(
            "Aely Data Inspector",
            styles["Title"],
        )
    )


    elements.append(
        Paragraph(
            "Relatório Executivo de Qualidade dos Dados",
            styles["Heading2"],
        )
    )


    elements.append(
        Spacer(1, 20)
    )


    # Resumo

    elements.append(
        Paragraph(
            "Resumo da Base",
            styles["Heading2"],
        )
    )


    summary_items = [
        f"Quantidade de linhas: {summary['total_rows']}",
        f"Quantidade de colunas: {summary['total_columns']}",
        f"Quantidade de células: {summary['total_cells']}",
    ]


    for item in summary_items:

        elements.append(
            Paragraph(
                item,
                styles["BodyText"],
            )
        )


    elements.append(
        Spacer(1, 15)
    )


    # Qualidade

    elements.append(
        Paragraph(
            "Indicadores de Qualidade",
            styles["Heading2"],
        )
    )


    quality_items = [
        f"Score de qualidade: {quality['score']}/100",
        f"Valores nulos encontrados: {quality['null_values']}",
        f"Linhas duplicadas: {quality['duplicate_rows']}",
        f"Colunas totalmente vazias: {len(quality['empty_columns'])}",
        f"Colunas com apenas um valor: {len(quality['single_value_columns'])}",
    ]


    for item in quality_items:

        elements.append(
            Paragraph(
                item,
                styles["BodyText"],
            )
        )


    elements.append(
        Spacer(1, 15)
    )


    # IA

    elements.append(
        Paragraph(
            "Diagnóstico Executivo da IA",
            styles["Heading2"],
        )
    )


    format_ai_report(
        report,
        elements,
        styles,
    )


    document.build(
        elements
    )


    buffer.seek(0)


    return buffer