import os

from dash import Dash
from dash_bootstrap_components.themes import FLATLY as theme
from dash.dependencies import Input, Output
import dash_html_components as html

from callbacks import register_callbacks
from components import mk_nav
import layout


app = Dash(__name__, external_stylesheets=[theme])
app.config.suppress_callback_exceptions = True
app.title = 'Python Engeco'
server = app.server
app.layout = layout.layout_div
register_callbacks(app)


base = '/'
if app.config['url_base_pathname'] is not None:
    base = app.config['url_base_pathname']
nav = mk_nav(base)


@app.callback(Output('page-content', 'children'),
             [Input('url', 'pathname')])
def display_page(pathname):
    base = '/'
    if app.config['url_base_pathname'] is not None:
        base = app.config['url_base_pathname']
    if pathname == base or pathname == f'{base}pv2fv':
        return html.Div([nav, layout.pv2fv])
    elif pathname == base or pathname == f'{base}pv2us':
        return html.Div([nav, layout.pv2us])
    else:
        return html.Div([nav, layout.pv2fv])


if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    debug = os.getenv('DEBUG') == 'true'
    app.run_server(host='0.0.0.0', port=port, debug=debug)
