import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
features=pd.read_csv("Features data set.csv")
sales=pd.read_csv("sales data-set.csv")
stores=pd.read_csv("stores data-set.csv")
#print(type(features))
#print(features.head(5))
#print(sales.head(5))
#print(stores.head(5))
#print(features.tail(5))
# print(sales.tail(5))
# print(stores.tail(5))
# features['Date']=pd.to_datetime(features['Date'])
# sales['Date']=pd.to_datetime(sales['Date'])
# print(features['Date'])
#TO KNOW THE NUMBER OF ROWS AND COLUMN
# print(features.shape)
# print(sales.shape)
# print(stores.shape)
#features.info()
#sales.info()
#stores.info()
# print("\n Columns in Feature table\n", features.columns)
# print("\n Columns in Stores table\n", stores.columns)
# print("\n Columns in Sales table\n", sales.columns)
#Merge the Data in a Unique DataFrame
df=pd.merge(sales,features, on =['Store','Date','IsHoliday'], how='left')
#print(df)
df=pd.merge(df,stores, on=['Store'], how='left')
#print(df)
df=df.fillna(0)
m=df.sort_values(['Date',"Weekly_Sales"], ascending=[True,False])
#print(m)
# print(df.head(7))
# print(df.shape)
# print(df.columns)
# print(df.describe())
# print(df.index)
# print(df.values)
#Subsetting
# subset=sales[['Weekly_Sales','Date']]
# print(subset.head())
# #print(df.head())
#print(df.loc[0])
#print(df.loc[[0,99]])
#print(df.iloc[0])
#print(df.iloc[-1])
# df.ix[0]
#subset=df.loc[:, ['Store','Date','Weekly_Sales']]
#print(subset.head())
#subset=df.iloc[:, [2,4]]
#print(subset.head())
#subset=df.iloc[-5::2, :]
#subset.head()
#print(df.groupby(['Date']) ['CPI'].mean().head(5))
#print(df.groupby(['Store','Date']) [['Weekly_Sales','Unemployment']].mean())
#print(df.groupby(['Store','Date']) [['Weekly_Sales','Unemployment']].mean().reset_index().head(5))
#VISUALIZATION
#(df.groupby(['Store'])[['Weekly_Sales']].mean().plot())
#plt.show()
#df.plot(kind='scatter',x='Store',y='Weekly_Sales',rot=70)
#plt.show()
df.boxplot(column='Weekly_Sales', by='Store')
plt.show()

