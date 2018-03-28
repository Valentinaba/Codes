#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import cm
###############################################
df=pd.read_excel("Accidentalidad_2016.xlsx")

df1=pd.read_excel("Accidentalidad_2014.xlsx")
df2=pd.read_excel("Accidentalidad_2015.xlsx")

###############################################
'''
Dia=df['DIA']
D=pd.value_counts(df['DIA'].values)
D1=pd.Series.tolist(D)
Dx=[1,2,3,4,5,6,7]
#plt.plot(Dx,D1,'*')
'''

################################################
'''
H=pd.value_counts(df['HORA'].values)
#print H
HH=df['HORA']=pd.to_datetime(df['HORA'])

HH=HH.apply(lambda x: x.hour)

#HH=pd.Series.tolist(HH)
print (HH)
'''
#################################################
'''
#pd.Series(df['DIA']).value_counts().plot('bar')
pd.Series(df2['CLASE']).value_counts().plot('bar')
plt.show()
#pd.Series(HH).value_counts().plot('bar')
'''
################################################
#filtro dias 
'''
L=df[(df['DIA']=='LUNES')]
M=df[(df['DIA']=='MARTES')]
W=df[(df['DIA']=='MIÉRCOLES')]
J=df[(df['DIA']=='JUEVES')]
V=df[(df['DIA']=='VIERNES')]
S=df[(df['DIA']=='SÁBADO')]
D=df[(df['DIA']=='DOMINGO')]
'''
################################################
#HISTO COMUNAS
'''
pd.Series(df['COMUNA']).value_counts().plot('bar',title='Accidentalidad por comuna para el 2016')
plt.show()
pd.Series(df1['COMUNA']).value_counts().plot('bar',title='Accidentalidad por comuna para el 2014')
plt.show()
pd.Series(df2['COMUNA']).value_counts().plot('bar',title='Accidentalidad por comuna para el 2015')
plt.show()
'''
################################################
#Accidentalidad por dia en los diferentes anos 
'''
fig1=pd.Series(df['DIA']).value_counts().plot('bar',title='Accidentalidad por dia de semana en el 2016')
plt.savefig('Fig1.png')
plt.show()

plt.close()

fig2=pd.Series(df1['DIA']).value_counts().plot('bar',title='Accidentalidad por dia de semana en el 2014')
plt.savefig('Fig2.png')
plt.show()
plt.close()
fig3=pd.Series(df2['DIA']).value_counts().plot('bar',title='Accidentalidad por dia de semana en el 2015')
plt.savefig('Fig3.png')
plt.show()
plt.savefig()
'''
################################################
#CICLORUTA

'''
Via=df[(df['DISENO']=='Ciclo Ruta')]
from collections import Counter
m=Counter(Via['COMUNA'])
print(m)
pd.Series(Via['COMUNA']).value_counts().plot('bar',title='Accidentes en Ciclo ruta por Comunas')
plt.show()'''
##################################################
'''
Muerto=df[(df['GRAVEDAD']=='MUERTO')]

Hora1= Muerto[(Muerto['HORA']>"00:00:00") & (Muerto['HORA']< "05:00:00")]

pd.Series(Hora1).value_counts().plot('bar',title='Muertes por hora')
plt.show()
'''
################################################
#Muerte por tipo de accidente 
'''
Muerto=df[(df['GRAVEDAD']=='MUERTO')]
HH=Muerto['HORA']=pd.to_datetime(Muerto['HORA'])
HH=HH.apply(lambda x: x.hour)
pd.Series(HH).value_counts().sort_index().plot('bar',title='Muertes por horas para el 2016')
plt.show()

Muerto1=df1[(df1['GRAVEDAD']=='MUERTO')]
HH1=Muerto1['HORA']=pd.to_datetime(Muerto1['HORA'])
HH1=HH1.apply(lambda x: x.hour)
pd.Series(HH1).value_counts().sort_index().plot('bar',title='Muertes por horas para el 2014')
plt.show()

Muerto2=df2[(df2['GRAVEDAD']=='MUERTO')]
HH2=Muerto2['HORA']=pd.to_datetime(Muerto2['HORA'])
HH2=HH2.apply(lambda x: x.hour)
pd.Series(HH2).value_counts().sort_index().plot('bar',title='Muertes por horas para el 2015')
plt.show()
'''
##################################################
H=df['HORA']=pd.to_datetime(df['HORA'])

H=H.apply(lambda x: x.hour)

Y=[]
for i in range (42841):
    
    m=df['GRAVEDAD'][i]
    if m=='MUERTO':
        y=500
    elif m=='HERIDO':
        y=10
        
    elif m=='SOLO DAÑOS':
        y=10
    else:
        pass
    i=i+1
    Y.append(y)
    
    
df.plot(kind="scatter", x="X", y="Y", alpha=0.5,
s=Y, label="Gravedad",
c=H, cmap=plt.get_cmap("binary"), colorbar=True, figsize=(18,20)
)
plt.legend()
plt.show()

