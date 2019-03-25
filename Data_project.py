#%% [markdown]
# # Data Analysis Project

#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# from matplotlib_venn import venn2
import pydst # Danmarks Statistik
from datetime import datetime


#%%
Dst = pydst.Dst(lang='en') # Set language to English


#%%
Dst.get_subjects() # Get overview of Statistics Denmark's subjects


#%%
Dst.get_data(table_id = 'BB1S')


#%%
Var = Dst.get_variables(table_id = 'BB1S')


#%%
Var[:]


#%%
Var['values'][3][:10]

#%%
df= Dst.get_data(table_id = 'BB1S', variables={'TID':['*'], 'SÆSON':['2'], 'LAND':['W1'], 'POST':['*'], 'INDUDBOP':['N']})


#%%
df.sort_values(['TID'], inplace=True)


#%%



#%%
df.head(5)


#%%
df['TID'] = df['TID'].str.replace('M', '-')


#%%
df['TID'] = pd.to_datetime(df['TID'])


#%%
PI  = df.loc[df['POST'] == 'PRIMARY INCOME', :]


#%%
PI['TID']


#%%



#%%



#%%



#%%



#%%
fig, ax = plt.subplots()

ax.plot(PI['TID'],PI['INDHOLD'])


plt.show()



