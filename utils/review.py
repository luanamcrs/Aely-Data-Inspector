import pandas as pd
import streamlit as st



def render_data_review(
    df: pd.DataFrame,
    suggestions: list,
):
    """
    Central de revisão de problemas de qualidade.

    Fluxo:
    1. Exibe resumo dos problemas.
    2. Analista abre detalhes se desejar.
    3. Executa ações de correção.
    """


    if "resolved_issues" not in st.session_state:

        st.session_state.resolved_issues = []


    if "df_final" not in st.session_state:

        st.session_state.df_final = df.copy()



    df_final = st.session_state.df_final



    st.subheader(
        "Revisão de Qualidade dos Dados"
    )



    if not suggestions:

        st.success(
            "Nenhum problema encontrado."
        )

        return df_final



    # ==========================
    # RESUMO DOS PROBLEMAS
    # ==========================


    summary = {}


    for issue in suggestions:

        problem_type = issue.get(
            "tipo",
            "Outro"
        )

        summary[problem_type] = (
            summary.get(problem_type, 0)
            + 1
        )



    st.markdown(
        "### Resumo da Análise"
    )



    cols = st.columns(
        len(summary)
    )


    for col, (problem, total) in zip(
        cols,
        summary.items()
    ):

        with col:

            st.metric(
                label=problem,
                value=total
            )



    st.info(
        f"Total de problemas encontrados: {len(suggestions)}"
    )



    # ==========================
    # DETALHES
    # ==========================


    with st.expander(
        "Ver detalhes dos problemas"
    ):


        st.dataframe(

            pd.DataFrame(
                suggestions
            ),

            use_container_width=True,

            hide_index=True,

        )



    st.markdown("---")



    st.subheader(
        "Tratamento Manual"
    )


    selected_index = st.selectbox(

        "Selecione um problema para tratar:",

        options=range(
            len(suggestions)
        ),

        format_func=lambda x:
            (
                f"Linha {suggestions[x]['linha']} | "
                f"{suggestions[x]['coluna']} | "
                f"{suggestions[x]['tipo']}"
            )

    )



    issue = suggestions[selected_index]


    linha = issue.get(
        "linha"
    )

    coluna = issue.get(
        "coluna"
    )

    tipo = issue.get(
        "tipo"
    )

    valor = issue.get(
        "valor"
    )



    st.write(
        f"**Linha:** {linha}"
    )

    st.write(
        f"**Coluna:** {coluna}"
    )

    st.write(
        f"**Problema:** {tipo}"
    )

    st.write(
        f"**Valor atual:** {valor}"
    )



    # ==========================
    # VALOR AUSENTE
    # ==========================


    if tipo == "Valor ausente":


        novo_valor = st.text_input(
            "Novo valor:",
            key="new_value"
        )



        if st.button(
            "Preencher valor"
        ):


            if novo_valor.strip():


                df_final.loc[
                    linha - 1,
                    coluna
                ] = novo_valor


                st.session_state.resolved_issues.append(
                    issue
                )


                st.success(
                    "Valor preenchido."
                )



            else:

                st.warning(
                    "Digite um valor."
                )



    # ==========================
    # ESPAÇOS EXTRAS
    # ==========================


    elif tipo == "Espaços extras":


        if st.button(
            "Corrigir espaços"
        ):


            df_final.loc[
                linha - 1,
                coluna
            ] = str(valor).strip()



            st.session_state.resolved_issues.append(
                issue
            )


            st.success(
                "Texto corrigido."
            )



    # ==========================
    # DUPLICADO
    # ==========================


    elif tipo == "Duplicado":


        st.warning(
            "Esse registro está duplicado."
        )


        if st.button(
            "Excluir linha"
        ):


            df_final.drop(

                index=linha - 1,

                inplace=True,

                errors="ignore"

            )


            df_final.reset_index(
                drop=True,
                inplace=True
            )


            st.session_state.resolved_issues.append(
                issue
            )


            st.success(
                "Linha excluída."
            )



    st.markdown("---")


    st.success(
        f"{len(st.session_state.resolved_issues)} problemas tratados."
    )



    st.session_state.df_final = df_final



    return df_final