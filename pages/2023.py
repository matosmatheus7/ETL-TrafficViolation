import dash
from dash import dcc, html
import plotly.express as px

import dash
from dash import dcc, html
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

dash.register_page(__name__, title='Brazil 2023 Traffic Violations Dashboard')
# Benchmark do Dash
'https://dash.gallery/dash-manufacture-spc-dashboard/'
from dash.dependencies import Input, Output

# Ler os dados
violations_per_day = pd.read_csv(r'.\datalake\gold\violations_per_day_2023.csv')
month_ticket_value = pd.read_csv(r'.\datalake\gold\month_ticket_value_2023.csv')
df_uf_tickets_value = pd.read_csv(r'.\datalake\gold\uf_tickets_value_2023.csv')
df_pivot_violations_month_state = pd.read_csv(r'.\datalake\gold\violations_month_state_2023.csv')
df_violations_per_state = pd.read_csv(r'.\datalake\gold\violations_per_state_2023.csv')
df_violations_per_day = pd.read_csv(r'.\datalake\gold\violations_per_day_2023.csv')
month_dictionary = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
frequent_infractions = pd.read_csv(r'.\datalake\gold\frequent_infractions_2023.csv')
df_time_acum = pd.read_csv(r'.\datalake\gold\time_infractions_2023.csv')
df_city_acum = pd.read_csv(r'.\datalake\gold\city_infractions_2023.csv')


layout = html.Div(

    children=[
        html.Div(
            className='banner',
            style={
                'height': 'fit-content',
                'display': 'flex',
                'flex-direction': 'row',
                'align-items': 'center',
                'justify-content': 'space-between',
                'border-bottom': '2px solid #378DFC',
                'color':'black',
                'padding': '1rem 5rem',
                'width': '100%',
            },

            children=[

                html.Div(
                    className='banner-title',
                    children=[
                        html.H5(
                            ['2023 Traffic Violations Analysis'], 
                            style={
                                'font-family':'open sans semi bold,sans-serif', 
                                'font-weight': '500'
                            } 
                        ),
                    ]
                ),
            ]
        ),

        html.Div(

            className='app-content',
            style={
                'padding': '1rem 5rem',
                'width': '100%',
            },

            children=[

                html.Div(
                    className='content',
                    style={
                        'display': 'grid', 
                        'grid-template-columns': '20% 80%',
                        'height' : '100%'
                    },

                    children=[

                        html.Div(
                            className='left-div',
                            style={
                                'display': 'flex',
                                'flex-direction': 'column',
                                'justify-content': 'space-evenly',
                                'align-items': 'center',
                                'margin': '0',
                                'padding': '0',
                                'width': '100%',
                                'height' : '30%',
                                'margin-bottom': '3rem',
                                'background-color':'#FFFFFF',
                                'border': '#D9E3F1 solid 0.2rem' 
                            },
                            children=[

                                html.Div(
                                    className='top',
                                    children=[
                                        html.H4(
                                            [f'{df_city_acum.iat[0,0]}'],
                                            style={
                                                'font-size': '1.5em',
                                                'line-height': '1.6',
                                                'font-weight': '400',
                                                'color': '#378DFC',
                                                'border-radius': '3px',
                                                'padding': '12px 8px 12px 14px',
                                                'border': '1px solid #D3D3D3',
                                                'background': '#D9E3F1',
                                                'box-sizing': 'border-box',
                                                'width': '100%',
                                                'display': 'flex',
                                                'flex-direction': 'row',
                                                'justify-content': 'center',
                                            }
                                        ),
                                        html.H5(
                                            ['City with Highest Infractions'], 
                                            style={
                                                'line-height': '1.6',
                                                'box-sizing': 'border-box',
                                                'margin': '1rem',
                                                'color':'black',
                                                'font-weight': '500',
                                                'align-self': 'flex-start',
                                            }),
                                    ]
                                ),

                                html.Div(
                                    className='top',
                                    children=[
                                        html.H4(
                                            [f'{ round( violations_per_day.Violations_Count.sum() /1000000, 1 )  } mi'],
                                            style={
                                                'font-size': '1.5em',
                                                'line-height': '1.6',
                                                'font-weight': '400',
                                                'color': '#378DFC',
                                                'border-radius': '3px',
                                                'padding': '12px 8px 12px 14px',
                                                'border': '1px solid #D3D3D3',
                                                'background': '#D9E3F1',
                                                'box-sizing': 'border-box',
                                                'width': '100%',
                                                'display': 'flex',
                                                'flex-direction': 'row',
                                                'justify-content': 'center',
                                            }
                                        ),
                                        html.H5(
                                            ['Traffic Fines'], 
                                            style={
                                                'line-height': '1.6',
                                                'box-sizing': 'border-box',
                                                'margin': '1rem',
                                                'color':'black',
                                                'font-weight': '500',
                                                'align-self': 'flex-start',
                                            }),
                                    ]
                                ),

                                html.Div(
                                    className='inner-div',
                                    children=[
                                        html.H4(
                                            [f'R$ { int( round( month_ticket_value.Ticket_Value.sum() /1000000, 0 ) )  } mi'],
                                            style={
                                                'font-size': '1.5em',
                                                'line-height': '1.6',
                                                'font-weight': '400',
                                                'color': '#378DFC',
                                                'border-radius': '3px',
                                                'padding': '12px 8px 12px 14px',
                                                'border': '1px solid #D3D3D3',
                                                'background': '#D9E3F1',
                                                'box-sizing': 'border-box',
                                                'width': '100%',
                                                'display': 'flex',
                                                'flex-direction': 'row',
                                                'justify-content': 'center',
                                            }
                                        ),
                                        html.H5(
                                            ['Collected'], 
                                            style={
                                                'color':'black',
                                                'line-height': '1.6',
                                                'box-sizing': 'border-box',
                                                'margin': '1rem',
                                                'font-weight': '500',
                                                'align-self': 'flex-start',
                                                
                                            }
                                        )
                                    ]
                                ),
                                 html.Div(
                                    className='inner-div',
                                    children=[
                                        html.H4(
                                            [f'{frequent_infractions.iat[0,0]} - {frequent_infractions.iat[0,1]} '],
                                            style={
                                                'font-size': '1em',
                                                'line-height': '1.6',
                                                'font-weight': '400',
                                                'color': '#378DFC',
                                                'border-radius': '3px',
                                                'padding': '12px 8px 12px 14px',
                                                'border-left': '40px solid #FFFFFF',
                                                'border-right': '40px solid #FFFFFF',
                                                'background': '#D9E3F1',
                                                'box-sizing': 'border-box',
                                                'width': '100%',
                                                'display': 'flex',
                                                'flex-direction': 'row',
                                                'justify-content': 'center',
                                            }
                                        ),
                                        html.H5(
                                            ['Top 1 Registered Infraction'], 
                                            style={
                                                'color':'black',
                                                'line-height': '1.6',
                                                'box-sizing': 'border-box',
                                                'margin': '1rem',
                                                'font-weight': '500',
                                                'text-align':'center',
                                                'align-self': 'flex-start',
                                                
                                            }
                                        )
                                    ]
                                )
                            ]
                        ),

                        html.Div(

                            className='right-div',
                            style={
                                'display': 'flex',
                                'flex-direction': 'column',
                                'justify-content': 'space-evenly',
                                'align-items': 'center',
                                'margin': '0',
                                'padding': '0',
                                'width': '100%',
                                'margin-bottom': '3rem',
                                'background-color':'#FFFFFF',
                                'border': '#FFFFFF solid 0.2rem' 
                            },

                            children=[

                                html.Div(
                                    className='inner-div',
                                            style={
                                                'margin-top': '0%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#FFFFFF solid 0.2rem'
                                            },

                                    children=[
                                        dcc.Graph(id='line-fig',
                                            figure=px.line(
                                                    df_violations_per_day,
                                                    height=400, 
                                                    width=1050,
                                                    x='Date',
                                                    y='Violations_Count',
                                                    title='Registered Fines per Day',
                                                    labels={
                                                        'Violations_Count':'Violations Count',
                                                        'Date':'Date'
                                                    }
                                                ), style={'margin-top': '0px','margin-left':'10px'}),
                                    
                                    ]
                                ),

                                html.Div(
                                    className='inner-div',
                                            style={
                                                'margin-top': '6%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#D9E3F1 solid 0.2rem'
                                            },

                                    children=[
                                        dcc.Graph(
                                        id='chart2',
                                        figure=px.bar(
                                                month_ticket_value,
                                                x=month_dictionary,
                                                y='Ticket_Value',
                                                height=400, 
                                                width=1050,
                                                title='Collected Value per Month',
                                                labels={
                                                        'Ticket_Value':'Ticket Value',
                                                        'month_dictionary':'Month'
                                                    }
                                            ).update_layout(xaxis_title="Month"), style={'margin-top': '10px','margin-left':'10px'}
                                        ),
                                    ]
                                ),
                                html.Div(
                                            className='inner-div',
                                            style={
                                                'margin-top': '6%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#D9E3F1 solid 0.2rem'
                                            },
                                            children=[
                                                dcc.Graph(id='scatter-fig',
                                                figure=px.scatter(
                                                            df_uf_tickets_value,
                                                            x='Violations_Count',
                                                            y='Total_ticket_value',
                                                            color='Infraction_State',
                                                            size='Violations_Count',
                                                            height=400, 
                                                            width=1050,
                                                            log_x=True,
                                                            size_max=60,
                                                            labels={
                                                            'Violations_Count':'Violations Count',
                                                            'Total_ticket_value':'Total Tickets Value'
                                                        },
                                                            title='State Violations Scatter Plot' ), style={'margin-top': '0%','margin-left':'10px'}),
                                            ]
                                        ),
                                    html.Div(
                                            className='inner-div',
                                            style={
                                                'margin-top': '6%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#D9E3F1 solid 0.2rem'
                                            },
                                            children=[
                                                dcc.Graph(id='heatmap-fig',
                                                figure=px.imshow(
                                                df_pivot_violations_month_state,
                                                height=400, 
                                                width=1050,
                                                title=' Heatmap Monthly Traffic Violations by State 2022'),
                                                style={'margin-top': '0%','margin-left':'10px'}),
                                            ]
                                        ),
                                    html.Div(
                                            className='inner-div',
                                            style={
                                                'margin-top': '6%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#D9E3F1 solid 0.2rem'
                                            },
                                            children=[
                                                dcc.Graph(id='funnel-fig2',
                                                figure=px.funnel(
                                                        df_violations_per_state[ df_violations_per_state['cumulative_sum'] < 0.5 ],
                                                        y='Infraction_State',
                                                        x='Violations_Count',
                                                        height=360, 
                                                        width=1050,
                                                        title='State Concentration of 50% Traffic Infractions'
                                                    ),
                                                style={'margin-top': '0%','margin-left':'10px'}),
                                            ]
                                        ),
                                        html.Div(
                                            className='inner-div',
                                            style={
                                                'margin-top': '6%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#D9E3F1 solid 0.2rem'
                                            },
                                            children=[
                                                dcc.Graph(id='funnel-fig2',
                                                figure=
                                                    px.funnel(
                                                        frequent_infractions,
                                                        y='Abbreviated_Infraction_Description',
                                                        x='count',
                                                        height=360, 
                                                        labels={
                                                        'Abbreviated_Infraction_Description':'Infraction Description',
                                                        'count':'Number of Registered infractions'
                                                        },
                                                        width=1050,
                                                        title='Most Commons Registered Infractions'
                                                    ),
                                                style={'margin-top': '0%','margin-left':'10px'}),
                                            ]
                                        ),
                                        html.Div(
                                            className='inner-div',
                                            style={
                                                'margin-top': '6%',
                                                'padding': '0',
                                                'width': '100%', 
                                                'height': '350px',
                                                'border-top': '#D9E3F1 solid 0.2rem'
                                            },
                                            children=[
                                                dcc.Graph(id='funnel-fig2',
                                                figure=
                                                px.funnel(
                                                    df_time_acum[ df_time_acum['Acum'] < 0.5 ],
                                                    y='Time',
                                                    height=400, 
                                                    width=1050,
                                                    x='Violations_Count',
                                                    title='Most Common Times that Offenses were Committed (24 hours Format on BRT Time zone)'
                                                ),
                                                style={'margin-top': '0%','margin-left':'10px'}),
                                            ]
                                        ),
                            ]
                        )
                    ]
                )
            ],
        )
    ],
)
