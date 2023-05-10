from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container(
   [
        html.H2('Ingrese los datos con los que cuenta'),
        html.Hr(),
        html.Label('Gravedad especifica'),
        dbc.Input(value="Gs"),
        html.Label('Peso del suelo'),
        dbc.Input(value="Wt"),
        html.Label('Contenido de humedad'),
        dbc.Input(value="."),
        html.Label('Volumen Total'),
        dbc.Input(value="Vt"),
        html.Label('Peso seco'),
        dbc.Input(value="Ws"),
    ]
)