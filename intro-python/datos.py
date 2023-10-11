import numpy as np
import pandas as pd

# numeros = [1,2,3,4,5,6,7,8,9,10]
# np_array = np.array(numeros)

ciudades = np.array(['Madrid', 'Chernobyl','Barcelona', 'Sevilla', 'Valencia', 'Zaragoza'])
poblaciones = np.array([3.2, 0, 1.6, 4.9, 7.9, 6.6]) # millones de personas

data = np.array([ciudades, poblaciones])

# print(data)

# series de datos
series_ciudades = pd.Series(ciudades)
serie_dic = pd.Series({'Madrid': 3223334, 'Barcelona': 1620343, 'Sevilla': 693878, 'Valencia': 791413, 'Zaragoza': 666880})

# print(series_ciudades)
# print(serie_dic)

data_dic = {
    'ciudades': ciudades,
    'poblacion': poblaciones  
}

# dataframes
df = pd.DataFrame(data_dic, columns=['ciudades', 'poblacion'])

# print(df.shape) # dimensiones
# print(df.head(10)) # primeros 10 elementos
# print(df.columns)

# print(df['poblacion'].sum()) # suma de la columna poblacion
# print(df['poblacion'].median()) # mediana de la columna poblacion
# print(df['poblacion'].mean()) # media de la columna poblacion

# condicion = df['poblacion'] > 6

# cada prueba lógica debe ir entre paréntesis
# el operador & es el operador lógico AND
# el operador | es el operador lógico OR
condicion = (df['poblacion'] > 3) & (df['poblacion'] < 7)

print(df[condicion])