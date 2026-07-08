import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


BACKGROUND = "#080808"
CARD = "#111111"
PINK = "#FF8FB1"
TEXT = "#FFFFFF"
SECONDARY_TEXT = "#B8B8C2"


def apply_chart_style(fig: go.Figure, height: int = 420) -> go.Figure:
    """
    Aplica o padrão visual do Aely Data Inspector aos gráficos.
    """

    fig.update_layout(
        template="plotly_dark",
        height=height,
        paper_bgcolor=BACKGROUND,
        plot_bgcolor=CARD,
        font=dict(
            family="Inter",
            color=TEXT,
            size=13,
        ),
        title=dict(
            font=dict(
                size=18,
                color=TEXT,
            ),
            x=0.02,
            xanchor="left",
        ),
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30,
        ),
        showlegend=True,
        legend=dict(
            font=dict(
                color=TEXT,
            )
        ),
    )

    return fig



def create_null_chart(df: pd.DataFrame) -> go.Figure:
    """
    Cria um gráfico de barras com valores nulos por coluna.
    """

    nulls = df.isnull().sum().reset_index()

    nulls.columns = [
        "Coluna",
        "Valores Nulos",
    ]

    fig = px.bar(
        nulls,
        x="Coluna",
        y="Valores Nulos",
        title="Valores Nulos por Coluna",
        text="Valores Nulos",
        color_discrete_sequence=[
            PINK
        ],
    )


    fig.update_traces(
        marker_line_width=0,
        textposition="outside",
        textfont_color=TEXT,
    )


    fig.update_xaxes(
        tickfont_color=SECONDARY_TEXT,
        title="",
    )


    fig.update_yaxes(
        tickfont_color=SECONDARY_TEXT,
        title="",
    )


    return apply_chart_style(fig)



def create_dtype_chart(df: pd.DataFrame) -> go.Figure:
    """
    Cria um gráfico de pizza mostrando os tipos das colunas.
    """

    dtype_count = (
        df.dtypes.astype(str)
        .value_counts()
        .reset_index()
    )


    dtype_count.columns = [
        "Tipo",
        "Quantidade",
    ]


    fig = px.pie(
        dtype_count,
        names="Tipo",
        values="Quantidade",
        title="Distribuição dos Tipos de Dados",
        hole=0.55,
    )


    fig.update_traces(
        textfont_color=TEXT,
        marker=dict(
            line=dict(
                color=BACKGROUND,
                width=2,
            )
        ),
    )


    fig.update_layout(
        legend=dict(
            font=dict(
                color=TEXT
            )
        )
    )


    return apply_chart_style(fig)