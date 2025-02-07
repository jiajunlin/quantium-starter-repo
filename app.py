from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import csv

app = Dash(__name__)


def load_data():
    input_files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]
    # Create a list to store the rows
    data = []

    # Process each input file
    for file in input_files:
        with open(file, "r") as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip the header row

            # Iterate through each row
            for row in reader:
                product = row[0]
                price = float(row[1].replace("$", ""))  # Remove the dollar sign
                quantity = float(row[2])
                date = row[3]
                region = row[4]

                # Calculate sales
                sales = quantity * price

                # Add the row to the list
                data.append([sales, date, region])

    return pd.DataFrame(data, columns=["Sales", "Dates", "Region"])


df = load_data()

df["Before/After"] = df["Dates"].apply(lambda x: "Before" if x < "2021-01-15" else "After")

colors = {
    'background': '#505050',
    'text': '#eadedb'

}

fig = px.line(df, x="Dates", y="Sales")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    showlegend=True
)

# Add a vertical line to show the date increased price

fig.add_shape(
    type="line",
    x0="2021-01-15",
    y0=df["Sales"].min(),
    x1="2021-01-15",
    y1=df["Sales"].max(),
    line=dict(color="red", width=2, dash="dash"),
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Soul Foods Sales Trend',
        style={
            'textAlign': 'center',
            'color': '#eadedb'
        }
    ),

    html.Div(children='Soul Foods Sales higher or lower after Pink Morsel price increase', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Br(),

    html.Div(children=[
        html.Label("Filter with callback"),
        dcc.RadioItems(
            id='region-filter',  # assign an ID to the Radio items component
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all'
        )
    ],
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])


@app.callback(
    Output('example-graph-2', 'figure'),
    [Input('region-filter', 'value')]
)
def update_graph(selected):
    if selected == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected]

    fig1 = px.line(filtered_df, x="Dates", y="Sales")

    fig1.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        showlegend=True
    )

    # Add a vertical line to show the date increased price
    fig1.add_shape(
        type="line",
        x0="2021-01-15",
        y0=filtered_df["Sales"].min(),
        x1="2021-01-15",
        y1=filtered_df["Sales"].max(),
        line=dict(color="red", width=1, dash="dash"),
    )
    return fig1


if __name__ == '__main__':
    app.run_server(debug=True)
