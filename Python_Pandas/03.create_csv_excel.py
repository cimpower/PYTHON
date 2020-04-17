import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# ENVIAR A CSV

# df ['Total']= df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.head(5))
# df.to_csv('modified.csv')

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# ENVIAR A EXCEL

# df ['Total']= df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.head(5))

# df.to_excel('modified.xlsx',index=False)

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# ENVIAR A CSV CON SEPRADORES TABULADOS

df ['Total']= df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

df.to_csv('modified_2.txt',index=False, sep='\t')