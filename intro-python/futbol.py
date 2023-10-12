import pandas as pd

df_datos = pd.read_csv('csv/Fullmetadata.csv')

columnas = ['player_id', 'player_name', 'goals', 'games' , 'assists',
        'yellow_cards', 'red_cards', 'position', 'team_name', 'year']

# print(df_datos[columnas].head())

# maximos goleadores del 2014
juagadores = df_datos['year'] == 2014
print(df_datos[juagadores].sort_values(by='goals', ascending=False)[columnas].head())

# maximos goleadores del 2014 del Real Madrid
juagadores = (df_datos['year'] == 2014) & (df_datos['team_name'] == 'Real Madrid')
print(df_datos[juagadores].sort_values(by='goals', ascending=False)[columnas].head())

# goles por equipo por año
condicion = df_datos['year'] == 2020
print(df_datos[ condicion ].groupby(['team_name'])['goals'].sum()) #.sort_values(by='goals', ascending=False).head(10)
