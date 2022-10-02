import os
from tkinter.ttk import Style
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
                html.H1("MyBudgets", className="text-primary"),
                html.P("By JOSIAS", className="text-info"),
                html.Hr(),

                #  secção PERFIL -----------
                dbc.Button(
                    id="botao_avatar", 
                    children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='avatar', className='perfil_name')],
                    style={'background-color': 'transparent', 'border-color': 'transparent'}
                )
            ])





# =========  Callbacks  =========== #
# Pop-up receita
