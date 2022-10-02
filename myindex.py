from dash import Dash, html, dcc
# import dash_html_components as html 
# import dash_core_components as dcc 

import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

from app import *
from components import sidebar, dashboards, extratos


# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    # dbc.Row: linha
    dbc.Row([
        # dbc.Col: coluna
        dbc.Col([
            dcc.Location(id='url'),
            # instanciar novo component 
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])
# fluid: responsivo
], fluid=True,)


# colback
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname): 
    if pathname == '/' or pathname == '/dashboard': 
        return dashboards.layout

    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)