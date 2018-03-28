'''
import pandas as pd

import matplotlib.pyplot as plt
datos=pd.read_csv('Accidentalidad_2014.csv')
#print datos.head()
#print datos.info()
#print(datos['DIA'])
#print (datos.sort_values(by='DIA'))
#print datos['DIA'].describe()
print datos['DIA'].keys()
#DIA=datos['DIA']
#print DIA[DIA==LUNES]
#print L

datos.head()


'''

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("Accidentalidad_2016.xlsx")
Dia=df['DIA']
D=pd.value_counts(df['DIA'].values)
D1=pd.Series.tolist(D)
Dx=[1,2,3,4,5,6,7]
plt.plot(Dx,D1)
plt.show()

