import dash_html_components as html
import dash_core_components as dcc

from pages.pv2fv import pv2fv
from pages.pv2us import pv2us


layout_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])