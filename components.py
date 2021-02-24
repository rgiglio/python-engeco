from datetime import date

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable

from utils import mk_empty_datatable


def mk_nav(base):
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem(dbc.NavLink("VP para VF", href=f'{base}pv2fv')),
                        dbc.DropdownMenuItem(dbc.NavLink("VP para SU", href=f'{base}pv2us'))
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Matemática Financeira"
                )
            ),
        ],
        brand=f'Protótipo',
        brand_href="https://google.com",
        sticky="top",
        color="lightgray"
    )


pv_input = dcc.Input(
    id='pv-input',
    type='number',
    placeholder='PV',
    min=1, max=10**7, step=1, value=1000,
)
fv_input = dcc.Input(
    id='fv-input',
    type='number',
    placeholder='FV',
    min=1, max=10**7, step=1, value=1000,
)
n_input = dcc.Input(
    id='n-input',
    type='number',
    placeholder='N',
    min=0, max=10**4, step=1, value=5,
)
i_input = dcc.Input(
    id='i-input',
    type='number',
    placeholder='i',
    min=0.01, max=10_000, step=0.01, value=0.05,
)
fv_output = html.H3(id='fv-output')
su_output = html.H3(id='su-output')
