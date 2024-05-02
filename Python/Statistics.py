# -------------------------------------------------------------------
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # for plotting
import matplotlib.pyplot as plt # for plotting
import datetime
import os

# Get the current working directory
current_dir = os.getcwd()
# print(current_dir)
# print(os.listdir(current_dir))

# Join the 'Data' directory to the current working directory
imm_dir = os.path.join(current_dir, "Immigration Statistics 20 yrs")

# List the files and directories in the 'Immigration Statistics 20 yrs' directory
# print(os.listdir(imm_dir))
# -----------------------------------------------------------------------

file = r'C:\Users\CxLos\OneDrive\Documents\Personal Projects\Immigration Statistics 20 yrs\Data\US_Immigration_Statistics.csv'
data = pd.read_csv(file)
print(data.head(20))
# ---------------------------------------------------------------------------