# %% 
import pandas as pd 
import numpy as np
import plotly.express as px
import os
# %%

PATH = os.path.join(os.getcwd(), 'data', 'titanic.csv')

df = pd.read_csv(PATH)

# %%
df.drop(inplace=True, columns=["PassengerId",'Name', 'Ticket', 'Cabin'])
df	

# %%
df.isna().sum()
# %%
# drop rows with missing values
df.dropna(inplace=True)

# %%
# label encoding
df["Sex"] = df["Sex"].apply(lambda x: 1 if x == "male" else 0)
# %%
df["Embarked"] = df["Embarked"].apply(lambda x: 0 if x == "S" else 1 if x == "C" else 2)
# %%
df

# %%
df.describe()
# %%

df 

# %%
