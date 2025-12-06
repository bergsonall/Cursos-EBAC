import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df=pd.read_csv(r'D:\GitHub\Cursos-EBAC\analiseDados\VisualizarComunicarDados\matematicaEstatistica\estatisticaBasica\clientes-v3-preparado.csv')
lista_nivel_educacao = df['nivel_educacao'].unique()
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]

def cria_graficos(selecao_nivel_educacao):
    # Grafico Barra
    filtro_df = df[df['nivel_educacao'].isin(selecao_nivel_educacao)]

    fig1 = px.bar(filtro_df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', color_discrete_sequence=px.colors.sequential.RdBu)
    fig1.update_layout(
        title='Salario por estado civil e nivel de educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salario',
        legend_title='Nivel de educação',
        plot_bgcolor='rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241, 1)'
    )

    # Grafico 3D
    fig2 = px.scatter_3d(df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')
    fig2.update_layout(
        title='Salario vs Idade e Anos de Experiencia',
        scene=dict(
            xaxis_title='Idade',
            yaxis_title='Salario',
            zaxis_title='Anos de Experiencia'
        )
    )
    return fig1, fig2

def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard Interativo'),
        html.Div('''
            Interatividade entre os dados
        '''),
        html.Br(),
        html.H2('Grafico de salario por estado civil'),
        dcc.Checklist(
            id='id_selecao_nivel_educacaor',
            options=options,
            value=[lista_nivel_educacao[0]] # Definir valor padrao
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')
    ])
    return app

if __name__ == '__main__':
    app =  cria_app()

    @app.callback(
        [
            Output('id_grafico_barra', 'figure'),
            Output('id_grafico_3d', 'figure')
        ],
        [Input('id_selecao_nivel_educacaor', 'value')]
    )
    def atualiza_grafico(selecao_nivel_educacao):
        fig1, fig2 = cria_graficos(selecao_nivel_educacao)
        return [fig1, fig2]
    app.run(debug=True, port=8050)