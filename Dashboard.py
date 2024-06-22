# dashboard/app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Load data
df = pd.read_csv('data/sample_data.csv')

# Initialize the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Sample Dashboard'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Column1'], 'y': df['Column2'], 'type': 'line', 'name': 'Sample Data'},
            ],
            'layout': {
                'title': 'Sample Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
