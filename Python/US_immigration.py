# IMPORTS -------------------------------------------------------------------
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # for plotting
import matplotlib.pyplot as plt # for plotting
import plotly.graph_objects as go
import plotly.express as px
import datetime
import os
import dash
from dash import dcc, html
# from dash import html
from dash.dependencies import Output, State
from dash.development.base_component import Component

# WORKING DIRECTORY ----------------------------------------------------------------------

# Get the current working directory
current_dir = os.getcwd()
# print(current_dir)
# print(os.listdir(current_dir))

# Join the 'Data' directory to the current working directory
imm_dir = os.path.join(current_dir, "US_Immigration_Statistics")

# List the files and directories in the 'Immigration Statistics 20 yrs' directory
# print(os.listdir(current_dir))

# DATA -----------------------------------------------------------------------

file = r'C:\Users\CxLos\OneDrive\Documents\Portfolio Projects\US_Immigration_Statistics\Data\US_Immigration_Statistics.csv'
df = pd.read_csv(file)

years = list(map(str, range(1980, 2021)))
# print('Years:', years)

# Set index to year
df.set_index('Year', inplace=True)

columns_to_convert = ['Immigrants Obtaining Lawful Permanent Resident Status',
                      'Refugee Arrivals',
                      'Noncitizen Apprehensions',
                      'Noncitizen Removals',
                      'Noncitizen Returns']

# Remove commas from the specified columns and convert to numeric
for column in columns_to_convert:
    df[column] = df[column].str.replace(',', '').astype(int)

# Remove leading/trailing spaces from column names if present
# df.columns = df.columns.str.strip()

# To numeric
df['Immigrants Obtaining Lawful Permanent Resident Status'] = pd.to_numeric(df['Immigrants Obtaining Lawful Permanent Resident Status'], errors='coerce')
# df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# print(df.head(10))
# print('Column Names:', df.columns)
# print('DF Shape:', df.shape)
# print('Dtypes:',df.dtypes)
# print('Amt of duplicate rows:', duplicate_len)

# Yearly Immigration to the US ---------------------------------------------------------------------------

# yearly_trend = df.loc['Immigrants Obtaining Lawful Permanent Resident Status', years]
yearly_trend = df.loc[:,'Immigrants Obtaining Lawful Permanent Resident Status']

# Change index values(years) to int:
# yearly_trend.index = yearly_trend.index.map(int) 

# print(yearly_trend)
# print(yearly_trend.dtypes)

# Determine the range of data
max_value = yearly_trend.max()
min_value = yearly_trend.min()
# print('Max value:', max_value)
# print('Min Value:', min_value)

# Find the location of the minimum and maximum values
min_location = yearly_trend.idxmin()
max_location = yearly_trend.idxmax()
# print('Year with highest Immigration:', max_location)
# print('Year with lowest Immigration:', min_location)

# Calculate 4 evenly spaced values within the range
# tick_values = np.linspace(min_value, max_value, 4).astype(np.int64)

# Line Chart
# yearly_trend.plot(kind='line')
# plt.title('Immigrants Obtaining Lawful Permanent Resident Status')
# plt.xlabel('Year')
# plt.ylabel('Number of Immigrants (Millions)')

# Set y-axis ticks to the calculated values
# plt.yticks(tick_values)
# plt.show()

# DASHBOARD ---------------------------------------------------------------------

# Create a dash application layout
app = dash.Dash(__name__)

# Insight paragraph
insight_paragraph = html.P(
    "The chart titled 'Immigrants Obtaining Lawful Permanent Resident Status' provides a visual representation of the trends in legal immigration to the United States over a series of years. By plotting the total number of immigrants who have been granted lawful permanent resident status each year, the chart offers insights into how immigration patterns have evolved. The use of a blue line allows for a clear view of the increase or decrease in numbers annually, which could be influenced by a variety of factors such as changes in immigration law, economic conditions, and global events. The graph's layout, with its bold title and clearly labeled axes, ensures that the information is accessible and understandable. The rounded borders and careful styling of the chart contribute to an aesthetically pleasing presentation that complements the data's significance. This chart is not only informative but also serves as a tool for policymakers, researchers, and the public to understand the impact of immigration policies and trends.",
    style={'margin': '20px', 'textAlign': 'justify'}
)

# Dash app layout
app.layout = html.Div(children=[ 

            # Title
            html.H1('US Immigration Statistics', 
              style={'textAlign': 'center', 'color': 'cadetblue',
              'fontSize': 45, 'font-family':'Calibri'}),

            # html.Br(),

            # Row 1
            html.Div(children=[
                      html.Div(children=[
                              dcc.Graph(
                                    figure=px.line(df.groupby('Year')['Immigrants Obtaining Lawful Permanent Resident Status'].sum().reset_index(), 
                                        x='Year', y='Immigrants Obtaining Lawful Permanent Resident Status').
                                        update_traces(line=dict(color='blue')).  # Change the line color
                                        update_layout(title='Immigrants Obtaining Lawful Permanent Resident Status', 
                                    xaxis_title='Year', 
                                    yaxis_title='Number of Immigrants',
                                    title_x=0.5,
                                    font=dict(
                                          family='Calibri',  # Set the font family to Calibri
                                          size=17,          # Adjust the font size as needed
                                          color='black'))
                                ), 
                                html.P(
                                  "This line chart illustrates the number of immigrants who obtained lawful permanent resident status in the United States over the years. The upward or downward trends can indicate the effects of policy changes, economic factors, and global events on immigration.",
                                  style={
                                      'textAlign': 'justify',
                                      'margin': '20px',
                                      'font-family': 'Calibri', 
                                      'fontSize': '17px',        
                                      'color': 'black'          
                                  })],

                                style={'border':'2px solid black', 'border-radius':'10px', 'margin':'10px', 'width':'48%', 'padding':'10px'}),

                      html.Div(children=[
                              dcc.Graph(
                                    figure=px.line(df.groupby('Year')['Refugee Arrivals'].sum().reset_index(), 
                                        x='Year', y='Refugee Arrivals').
                                        update_traces(line=dict(color='red')).  # Change the line color
                                        update_layout(title='Refugee Arrivals', 
                                    xaxis_title='Year', 
                                    yaxis_title='Refugee Arrivals',
                                    title_x=0.5,
                                    font=dict(
                                          family='Calibri',  # Set the font family to Calibri
                                          size=17,          # Adjust the font size as needed
                                          color='black'))
                                ), 
                                html.P(
                                  "This line chart illustrates the number of immigrants who obtained lawful permanent resident status in the United States over the years. The upward or downward trends can indicate the effects of policy changes, economic factors, and global events on immigration.",
                                  style={
                                      'textAlign': 'justify',
                                      'margin': '20px',
                                      'font-family': 'Calibri', 
                                      'fontSize': '17px',        
                                      'color': 'black' })],
                                style={'border':'2px solid black', 'border-radius':'10px', 'margin':'10px', 'width':'48%'})], 
                                style={'display': 'flex', 'textAlign': 'center'}),

            # Row 2
            html.Div(children=[
                      html.Div(children=[
                             dcc.Graph(
                          figure=px.line(df.groupby('Year')['Noncitizen Apprehensions'].sum().reset_index(), 
                              x='Year', y='Noncitizen Apprehensions').
                              update_traces(line=dict(color='green')).  # Change the line color
                              update_layout(title='Noncitizen Apprehensions', 
                           xaxis_title='Year', 
                           yaxis_title='Noncitizen Apprehensions',
                           title_x=0.5,
                           font=dict(
                                family='Calibri',  # Set the font family to Calibri
                                size=17,          # Adjust the font size as needed
                                color='black'))
                      ), 
                      html.P(
                        "This line chart illustrates the number of immigrants who obtained lawful permanent resident status in the United States over the years. The upward or downward trends can indicate the effects of policy changes, economic factors, and global events on immigration.",
                        style={
                            'textAlign': 'justify',
                            'margin': '20px',
                            'font-family': 'Calibri', 
                            'fontSize': '17px',        
                            'color': 'black' })],
                      style={'border':'2px solid black', 'border-radius':'10px', 'margin':'10px', 'width':'49%'}),

                      html.Div(children=[
                          dcc.Graph(
                          figure=px.line(df.groupby('Year')['Noncitizen Removals'].sum().reset_index(), 
                              x='Year', y='Noncitizen Removals').
                              update_traces(line=dict(color='orange')).  # Change the line color
                              update_layout(title='Noncitizen Removals', 
                           xaxis_title='Year', 
                           yaxis_title='Noncitizen Removals',
                           title_x=0.5,
                           font=dict(
                                family='Calibri',  # Set the font family to Calibri
                                size=17,          # Adjust the font size as needed
                                color='black'))
                      ), 
                      html.P(
                        "This line chart illustrates the number of immigrants who obtained lawful permanent resident status in the United States over the years. The upward or downward trends can indicate the effects of policy changes, economic factors, and global events on immigration.",
                        style={
                            'textAlign': 'justify',
                            'margin': '20px',
                            'font-family': 'Calibri', 
                            'fontSize': '17px',        
                            'color': 'black' })],
                      style={'border':'2px solid black', 'border-radius':'10px', 'margin':'10px', 'width':'48%'})], 
                      style={'display': 'flex', 'textAlign': 'center'})
            ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

#  KILL PORT --------------------------------------------

# netstat -ano | findstr :8050
# taskkill /PID 24772 /F
# npx kill-port 8050

# Host Application ------------------------------

# 1. pip freeze > requirements.txt
# 2. add this to procfile: 'web: gunicorn <your_app_filename>:app'
# 3. heroku login
# 4. heroku create
# 5. git push heroku main