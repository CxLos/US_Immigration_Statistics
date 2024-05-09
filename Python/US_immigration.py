# IMPORTS -------------------------------------------------------------------
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # for plotting
import matplotlib.pyplot as plt # for plotting
import datetime
import os
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

# print(df['Year'])

# yearly_trend = df.loc['Immigrants Obtaining Lawful Permanent Resident Status', years]
yearly_trend = df.loc[:,'Immigrants Obtaining Lawful Permanent Resident Status']

# Change index values(years) to int:
# yearly_trend.index = yearly_trend.index.map(int) 

# print(yearly_trend)
# print(yearly_trend.dtypes)

# Determine the range of data
max_value = yearly_trend.max()
min_value = yearly_trend.min()
print('Max value:', max_value)
print('Min Value:', min_value)

# Find the location of the minimum and maximum values
min_location = yearly_trend.idxmin()
max_location = yearly_trend.idxmax()
print('Year with highest Immigration:', max_location)
print('Year with lowest Immigration:', min_location)

# Calculate 4 evenly spaced values within the range
# tick_values = np.linspace(min_value, max_value, 4).astype(np.int64)

# Line Chart
yearly_trend.plot(kind='line')
plt.title('Immigrants Obtaining Lawful Permanent Resident Status')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants (Millions)')

# Set y-axis ticks to the calculated values
# plt.yticks(tick_values)
plt.show()

# DASHBOARD ---------------------------------------------------------------------

# Create a dash application layout
app = dash.Dash(__name__)