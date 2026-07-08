import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


BACKGROUND = "rgba(0,0,0,0)"
CARD = "rgba(255,255,255,0.02)"

PINK = "#F4A7C7"
LIGHT_PINK = "#FFD1E3"
PURPLE = "#D8B4FE"

TEXT = "#FFFFFF"
SECONDARY_TEXT = "#B8B8C2"



def apply_chart_style(
    fig: go.Figure,
    height: int = 420
) -> go.Figure:
    """
    Aplica o padrão visual premium do Aely Data Inspector.
    """


    fig.update_layout(

        template="plotly_dark",

        height=height,


        paper_bgcolor=BACKGROUND,

        plot_bgcolor=BACKGROUND,


        font=dict(

            family="Inter",

            color=TEXT,

            size=13,

        ),


        title=dict(

            font=dict(

                size=18,

                color=LIGHT_PINK,

            ),

            x=0.5,

            xanchor="center",

        ),


        margin=dict(

            l=20,

            r=20,

            t=70,

            b=30,

        ),


        legend=dict(

            font=dict(

                color=SECONDARY_TEXT,

            ),

            bgcolor="rgba(0,0,0,0)",

        ),

    )


    fig.update_xaxes(

        showgrid=False,

        tickfont_color=SECONDARY_TEXT,

    )


    fig.update_yaxes(

        showgrid=True,

        gridcolor="rgba(255,255,255,0.06)",

        tickfont_color=SECONDARY_TEXT,

    )


    return fig





def create_null_chart(df: pd.DataFrame) -> go.Figure:
    """
    Gráfico de valores ausentes.
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


        textfont=dict(

            color=TEXT,

            size=12,

        ),


        marker=dict(

            cornerradius=8

        )

    )



    return apply_chart_style(fig)







def create_dtype_chart(df: pd.DataFrame) -> go.Figure:
    """
    Gráfico de distribuição dos tipos de dados.
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

        hole=0.62,


        color_discrete_sequence=[

            PINK,

            LIGHT_PINK,

            PURPLE,

        ]

    )




    fig.update_traces(


        textfont=dict(

            color=TEXT,

            size=13,

        ),


        marker=dict(

            line=dict(

                color="#07070A",

                width=3,

            )

        ),


        hovertemplate=

        "<b>%{label}</b><br>" +

        "%{value} colunas"

    )



    return apply_chart_style(
        fig,
        height=430
    )