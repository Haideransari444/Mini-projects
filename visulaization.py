import pandas as pd 
import numpy as np 
import matplotlib as plt 
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\muzam\OneDrive\Desktop\Pandas\Data Visulaization.csv')
print (df.info)
df.fillna(np.nan)
print(df.info)
df.replace(["",-999,'NA',np.nan], '')
df.columns = df.iloc[0]
df = df[1:]
df.reset_index(drop=True, inplace=True)
df['First name']= df['First name'].fillna ('')
df['Last name'] = df['Last name'].fillna('')
df['full name'] = df['First name']+ ' '+ df['Last name']
print(df.info)
y = df['full name']
x =df[100]
plt.figure(figsize=(8, 10))
plt.grid(True)
plt.xticks(range(min(x), max(x)+1, 5))
colors = ['red', 'green', 'blue', 'purple', 'orange']
color_list = [colors[i % len(colors)] for i in range(len(x))]
plt.scatter(x, y, color=color_list, edgecolor='black', linewidth=2,marker='x')
plt.show()