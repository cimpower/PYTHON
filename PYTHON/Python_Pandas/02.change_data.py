import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# SUMAR COLUMNAS
df ['Total']= df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))
# OTRA FORMA DE HACERLO
df['Total']=df.iloc[:,4:10].sum(axis=1)
# BORRAR COLUMNA
#df= df.drop(columns=['Total'])

# MOVER COLUMNAS
cols = list(df.columns)
print(cols)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(5))