import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print (df.head(3))
#print (df[['Name','HP']])
#print (df.iloc[2,1])

#for index, row in df.iterrows():
#    print(index, row['Name'])

#df.loc[df['Type 1'] == "Fire"]

#df.describe()

#df.sort_values('Name', ascending=True)
#df.sort_values(['Type 1','HP'])
orden=df.sort_values(['Type 1','HP'],ascending=[1,0])
print(orden)