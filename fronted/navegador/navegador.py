from dash import html
import dash_bootstrap_components as dbc

#importar componentes del navegador
from .descripcion.visualizacion import visualizacion
from .descripcion.rayas import rayas
from .descripcion.usuario import usuario


navegador = dbc.Container(
    [
        html.H1('RELACIONES GRAVIMETRICAS Y VOLUMETRICAS'),
        dbc.Row(
            [
                dbc.Col(visualizacion, md=3, style={'background-color':'black'}),
                dbc.Col(rayas, md=6 , style={'background-color':'gray'}),
                dbc.Col(usuario,md =3, style={'background-color':'yellow'}),
            ]
        )
    ]
)