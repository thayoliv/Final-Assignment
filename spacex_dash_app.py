# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                html.Div(children='Choose a site:', style={
                                    'font-style': 'italic',
                                    'font-weight': 'bold'
                                }),
                                html.Div([
                                    dcc.Dropdown(
                                        id='site-dropdown',
                                        options=[
                                            {'label': 'All sites', 'value': 'ALL'},
                                            {'label': 'CCAFS LC-40', 'value': 'CCAFS'}
                                        ],
                                        placeholder='Select a site...',
                                        style={
                                            'width': '50%'
                                        }
                                    ),
                                    html.Div(id='site-output')
                                ])
                            ])

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),
                                html.P("Payload range (Kg):"),

                                @app.callback(
                                    Output(component_id='success-pie-chart', component_property='figure')
                                    Input(component_id='site-dropdown', component_property='value')
                                )
                                def get_pie_chart(entered_site):
                                filtered_df = spacex_df
                                if entered_site == 'ALL':
                                    fig = px.pie(spacex_df, values='class', 
                                    names='pie chart names', 
                                    title='title')
                                    return fig
                                else:
                                    fig1 = px.pie(spacex_df, values='class', 
                                    names='pie chart names', 
                                    title='title')
                                    return fig1
                                    # return the outcomes piechart for a selected site






                                
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min = 0,
                                                max = 10000,
                                                step = 1000,
                                                value = [min_payload, max_payload])

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])
                                    fig2 =px.scatter(
                                            spacex_df, x="Payload Mass (kg)", y="class", 
                                            color="size", facet_col="day"
                                    )


# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()
