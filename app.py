import pandas as pd
from pathlib import Path
from io import BytesIO

import streamlit as st

from utils.analysis import (
    analyze_data_quality,
    find_data_issues,
    get_dataset_summary,
    load_data,
)

from utils.charts import (
    create_dtype_chart,
    create_null_chart,
)

from utils.ai import generate_executive_report

from utils.pdf import generate_pdf



def load_css():

    css_path = Path("assets/style.css")

    if css_path.exists():

        with open(
            css_path,
            "r",
            encoding="utf-8"
        ) as file:

            st.markdown(
                f"""
                <style>
                {file.read()}
                </style>
                """,
                unsafe_allow_html=True,
            )



def create_kpi_card(
    title,
    value
):

    st.markdown(
        f"""
        <div class="kpi-wrapper">
            <span class="kpi-title">{title}</span>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )



def generate_issues_excel(
    issues
):

    df_issues = pd.DataFrame(
        issues
    )

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df_issues.to_excel(
            writer,
            sheet_name="Problemas",
            index=False
        )

    output.seek(0)

    return output



st.set_page_config(
    page_title="Aely Data Inspector",
    page_icon="📊",
    layout="wide",
)



load_css()



# ==========================
# SESSION STATE
# ==========================

if "issues" not in st.session_state:

    st.session_state.issues = []


if "analysis_done" not in st.session_state:

    st.session_state.analysis_done = False


if "report" not in st.session_state:

    st.session_state.report = None


if "df_final" not in st.session_state:

    st.session_state.df_final = None



# ==========================
# HEADER
# ==========================


st.title(
    "AELY DATA INSPECTOR"
)


st.markdown(
    """
    **Data Quality Intelligence Platform**

    Analise automaticamente a qualidade dos seus dados,
    identifique inconsistências e gere diagnósticos executivos.
    """
)



st.sidebar.title(
    "AELY"
)



uploaded_file = st.sidebar.file_uploader(
    "Upload da Base",
    type=[
        "csv",
        "xlsx"
    ],
)



if uploaded_file is None:

    st.info(
        "Envie um arquivo CSV ou Excel para começar."
    )

    st.stop()



try:


    df = load_data(
        uploaded_file
    )


    summary = get_dataset_summary(
        df
    )


    quality = analyze_data_quality(
        df
    )



    st.success(
        f"Arquivo carregado: {uploaded_file.name}"
    )



    # ==========================
    # BOTÃO ANALISAR
    # ==========================


    if st.sidebar.button(
        "Analisar Data Quality",
        use_container_width=True
    ):


        st.session_state.issues = find_data_issues(
            df
        )


        st.session_state.df_final = df.copy()


        st.session_state.analysis_done = True


        st.session_state.report = None




    # ==========================
    # PROBLEMAS
    # ==========================


    if st.session_state.analysis_done:


        st.subheader(
            "Problemas Encontrados"
        )


        if st.session_state.issues:


            issues_df = pd.DataFrame(
                st.session_state.issues
            )


            st.dataframe(
                issues_df,
                use_container_width=True,
                hide_index=True
            )


            st.info(
                f"{len(st.session_state.issues)} problemas encontrados."
            )


            st.download_button(

                label="Baixar Relatório de Problemas",

                data=generate_issues_excel(
                    st.session_state.issues
                ),

                file_name="aely_problemas_encontrados.xlsx",

                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            )


        else:


            st.success(
                "Nenhum problema encontrado."
            )



    # ==========================
    # BASE
    # ==========================


    st.subheader(
        "Pré-visualização da Base"
    )


    st.dataframe(
        df,
        use_container_width=True
    )



    # ==========================
    # RESUMO
    # ==========================


    st.subheader(
        "Resumo da Base"
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        create_kpi_card(
            "Linhas",
            summary["total_rows"]
        )


    with c2:

        create_kpi_card(
            "Colunas",
            summary["total_columns"]
        )


    with c3:

        create_kpi_card(
            "Células",
            summary["total_cells"]
        )



    # ==========================
    # QUALIDADE
    # ==========================


    st.subheader(
        "Qualidade dos Dados"
    )


    q1, q2, q3 = st.columns(3)


    with q1:

        create_kpi_card(
            "Score",
            f"{quality['score']}/100"
        )


    with q2:

        create_kpi_card(
            "Valores ausentes",
            quality["null_values"]
        )


    with q3:

        create_kpi_card(
            "Duplicados",
            quality["duplicate_rows"]
        )



    # ==========================
    # GRÁFICOS
    # ==========================


    st.subheader(
        "Visualização dos Dados"
    )


    chart1, chart2 = st.columns(2)


    with chart1:

        st.plotly_chart(
            create_null_chart(df),
            use_container_width=True
        )


    with chart2:

        st.plotly_chart(
            create_dtype_chart(df),
            use_container_width=True
        )



    # ==========================
    # IA
    # ==========================


    st.divider()


    st.subheader(
        "Diagnóstico Executivo com IA"
    )



    if st.button(
        "Gerar Relatório IA",
    ):


        with st.spinner(
            "Gerando relatório..."
        ):


            st.session_state.report = generate_executive_report(
                summary,
                quality
            )



    if st.session_state.report:


        st.subheader(
            "Relatório Executivo"
        )


        st.markdown(
            st.session_state.report
        )



        pdf = generate_pdf(
            summary,
            quality,
            st.session_state.report
        )



        st.download_button(
            "Baixar Relatório PDF",
            data=pdf,
            file_name="aely_data_report.pdf",
            mime="application/pdf",
        )



except Exception as error:


    st.error(
        f"Erro: {error}"
    )