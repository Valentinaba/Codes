import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
############################################
#LECTURA DE DATOS 
df=pd.read_excel("Accidentalidad_2016.xlsx")
df1=pd.read_excel("Accidentalidad_2014.xlsx")
df2=pd.read_excel("Accidentalidad_2015.xlsx")
############################################
'''
Via=df[(df['DISENO']=='Ciclo Ruta')]
pd.Series(Via['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentes en Ciclo ruta por Comunas para el 2016')
plt.show()

Via=df1[(df1['DISENO']=='Ciclo Ruta')]
pd.Series(Via['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentes en Ciclo ruta por Comunas para el 2014')
plt.show()

Via=df2[(df2['DISENO']=='Ciclo Ruta')]
pd.Series(Via['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentes en Ciclo ruta por Comunas para el 2015')
plt.show()'''
############################################
#TIPO DE ACCIDENTE
'''
#Genera un histograma por tipo de accidente
df=pd.read_excel("Accidentalidad_2015.xlsx")
pd.Series(df['CLASE']).value_counts().plot('bar',title='Tipo de accidente para el 2015')
plt.show()'''
############################################
#COMUNA
'''
pd.Series(df['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentalidad por comuna para el 2016')
plt.show()
pd.Series(df1['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentalidad por comuna para el 2014')
plt.show()
pd.Series(df2['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentalidad por comuna para el 2015')
plt.show()
'''
############################################
#DIA
'''
df=pd.read_excel("Accidentalidad_2016.xlsx")
df1=pd.read_excel("Accidentalidad_2014.xlsx")
df2=pd.read_excel("Accidentalidad_2015.xlsx")

pd.Series(df['DIA']).value_counts().sort_index().plot('bar',title='Accidentalidad por dia para el 2016')
plt.show()
pd.Series(df1['DIA']).value_counts().sort_index().plot('bar',title='Accidentalidad por dia para el 2014')
plt.show()
pd.Series(df2['DIA']).value_counts().sort_index().plot('bar',title='Accidentalidad por dia para el 2015')
plt.show()'''

Choque=df2[(df2['CLASE']=='Choque')]
C=Choque['GRAVEDAD']

pd.Series(C).value_counts().plot('bar',title='Gravedad por choque para el 2015')
plt.show()

