import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import components as cp
from utils import mk_card


pv2fv = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col(mk_card('PV:', cp.pv_input, 'PV input')),
        dbc.Col(mk_card('n:', cp.n_input, 'n input')),
        dbc.Col(mk_card('i:', cp.i_input, 'i input')),
    ]),
    html.Br(),
    html.H1('Valor Presente para Valor Futuro'),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.Spinner(cp.fv_output)),
    ]),
    html.Br(),
], className='container')