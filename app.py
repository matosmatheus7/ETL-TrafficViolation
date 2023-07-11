import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,

                external_stylesheets=[dbc.themes.MORPH,
                                      'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
                                      'https://fonts.googleapis.com/css2?family=Joan&family=Roboto:ital,wght@0,100;1,300&family=Source+Sans+Pro:ital,wght@0,400;1,300&display=swap'
                                      ],

                use_pages=True,

                title='Brazil Traffic Violations Dashboard'
                )

app.layout = html.Div(
    [
        # main app framework
        html.Div("Brazil Traffic Violations Dashboard", style={
                 'background-color': '#D9E3F1', 'fontSize': 30, 'textAlign': 'center', 'margin-top': '1%'}),
        html.Div([
            dcc.Link(page['name'], href=page['path'], style={
                'background-color': '#378DFC',
                'textAlign': 'center',
                'border': 'none',
                'color': 'white',
                'text-align': 'center',
                'text-decoration': 'none',
                'display': 'inline-block',
                'font-size': '16px',
                'margin': '4px 2px',
                'cursor': 'pointer',
                'padding': '15px 32px',
                'margin-left': '30%'
            })
            for page in dash.page_registry.values()
        ], style={'background-color': '#D9E3F1'}),
        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
