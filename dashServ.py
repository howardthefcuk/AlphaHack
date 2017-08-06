import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

with open("contrCode.json") as f:
    country_codes = json.load(f)

with open("dataToUse.json") as f:
    data = json.load(f)

app.layout = html.Div([
    html.Div([
        dcc.Location(id='url', refresh=False),
        html.H1(id='country'),
        html.H3(id='total'),
        html.Div([
            dcc.RadioItems(
                id='graph-type',
                options=[{'label': i, 'value': k} for k, i in 
                    enumerate(['Minimum', 'Average', 'Maximum'])],
                value=0,
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='days-slider',
        min=1,
        max=31,
        value=1,
        step=1,
        marks={str(year): str(year) for year in range(1, 32)}
    )
])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('url', 'pathname'),
     dash.dependencies.Input('graph-type', 'value'),
     dash.dependencies.Input('days-slider', 'value')])
def update_graph(country, graph_type, days_slider):
    global data
    country_data = data[country.strip("/")]
    groups = list(country_data.keys())
    values = [int(country_data[group][graph_type] * days_slider) for group in groups]

    return {
        'data': [go.Pie(
            labels=groups,
            values=values,
            textinfo='value',
            hoverinfo='label+percent'
        )],
        'layout': go.Layout(
            
        )
    }


@app.callback(
    dash.dependencies.Output('country', 'children'),
    [dash.dependencies.Input('url', 'pathname')])
def update_country(country):
    return country_codes[country.strip("/")]

@app.callback(
    dash.dependencies.Output('total', 'children'),
    [dash.dependencies.Input('url', 'pathname'),
     dash.dependencies.Input('graph-type', 'value'),
     dash.dependencies.Input('days-slider', 'value')])
def update_total(country, graph_type, days_slider):
    global data
    country_data = data[country.strip("/")]
    groups = list(country_data.keys())
    values = [int(country_data[group][graph_type] * days_slider) for group in groups]
    return "Total: {} RUB".format(sum(values))

if __name__ == '__main__':
    app.run_server()