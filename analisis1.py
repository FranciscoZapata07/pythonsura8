from cgitb import text
from distutils import text_file
import pandas as pd

#CARGAR LOS DATOS
dataFrame=pd.read_csv('./empleados.csv')
#print(dataFrame)

#cargar todos los datos
#print(dataFrame.to_string())

#cargar los primeros registros de un banco de datos
#print(dataFrame.head(20))

#cargar los ultimos n registros de un banco e datos
#print(dataFrame.tail())

#obtener informaion de los datos cargados
#print(dataFrame.info())
#print(dataFrame.describe())

#acceder a datos o registros especificos
#print(dataFrame["nombres"].head())
#print(dataFrame["salario"].tail(20))

#acceder a registros por su indice
#print(dataFrame.iloc[20:30])
#print(dataFrame.loc[[10,20,30,40]])
#tabla=(dataFrame.loc[[1,5,10],["nombres"]])

'''
html=tabla.to_html()
text_file=open("index.html","w")
text_file.write(html)
text_file.close()
'''
#filtros con condiciones logicas
print(dataFrame[(dataFrame["salario"]>5500000) & (dataFrame["cargo"]=="analista2")])