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



#%%



#%%
df= Dst.get_data(table_id = 'BB1S', variables={'TID':['*'], 
                                               'SÆSON':['2'], 'LAND':['W1'], 'POST':['*'], 'INDUDBOP':['N']})


#%%
df.sort_values(['TID'], inplace=True)


#%%
df.head(5)


#%%
df['TID'] = df['TID'].str.replace('M', '-')


#%%
df['TID'] = pd.to_datetime(df['TID'])


#%%
PI  = df.loc[df['POST'] == 'PRIMARY INCOME', :]
S   = df.loc[df['POST'] == 'SERVICES', :]
SI  = df.loc[df['POST'] == 'SECONDARY INCOME', :]
G   = df.loc[df['POST'] == 'GOODS (FOB)', :]
CA  = df.loc[df['POST'] == 'CURRENT ACCOUNT', :]


#%%
PI['TID'].head()


#%%
df.groupby('POST').describe()


#%%



#%%



#%%



#%%
# plt.style.use('seaborn')
from matplotlib.gridspec import GridSpec

fig, axs = plt.subplots(3,2,figsize=(15,15))

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.4)


# gs1 = GridSpec(3, 2)
# ax1 = plt.subplot(gs1[0, 0])
# ax2 = plt.subplot(gs1[0, 1])
# ax3 = plt.subplot(gs1[1, 0])
# 

plt.subplot(3, 2, 1)
plt.plot(PI['TID'],PI['INDHOLD'])
plt.xlabel('Time')
plt.ylabel('Primary Income')
plt.title('Primary Income')

plt.subplot(3, 2, 2)
plt.plot(S['TID'],S['INDHOLD'])
plt.xlabel('Time')
plt.ylabel('Services')
plt.title('Services')

plt.subplot(3, 2, 3)
plt.plot(SI['TID'],SI['INDHOLD'])
plt.xlabel('Time')
plt.ylabel('Secondary Income')
plt.title('Secondary Income')

plt.subplot(3, 2, 4)
plt.plot(G['TID'],G['INDHOLD'])
plt.xlabel('Time')
plt.ylabel('Goods (FOB)')
plt.title('Goods (FOB)')



ax = fig.add_subplot(gs[2, :])
gs = gridspec.GridSpec(3, 2)

#plt.subplot(3, 2, 5)
ax.plot(CA['TID'],CA['INDHOLD'])
plt.xlabel('Time')
plt.ylabel('Current Account')
plt.title('Current Account')


plt.savefig('Historical plot', bbox_inches='tight')


#%%
plt.subplot(1, 1, 1)
plt.plot(CA['TID'].iloc[1:],CA['INDHOLD'].diff().iloc[1:])
plt.xlabel('Time')
plt.ylabel('Current Account 1-lag-diff')
plt.title('Current Account 1-lag-diff')


#%%



#%%



#%%



