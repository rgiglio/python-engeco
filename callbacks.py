from dash import callback_context
from dash.dependencies import Input, Output
from dash_table import FormatTemplate
from dash_table.Format import Format

import backend as be


def register_callbacks(app):
    
    @app.callback(
        [Output('fv-output', 'children')],
        [Input('pv-input', 'value'),
         Input('n-input', 'value'),
         Input('i-input', 'value')]
    )
    def update_de_vp_para_vf(vp, n, i):
        return be.de_vp_para_vf(vp, n, i),

    @app.callback(
        [Output('su-output', 'children')],
        [Input('pv-input', 'value'),
         Input('n-input', 'value'),
         Input('i-input', 'value')]
    )
    def update_de_vp_para_su(vp, n, i):
        return be.de_vp_para_su(vp, n, i),
