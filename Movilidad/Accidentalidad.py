import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
############################################
#LECTURA DE DATOS 
df=pd.read_excel("Accidentalidad_2016.xlsx")
df1=pd.read_excel("Accidentalidad_2014.xlsx")
df2=pd.read_excel("Accidentalidad_2015.xlsx")


############################################
#PRIMERA SECCION PREVENCION DE ACCIDENTES
############################################
#ACCIDENTES CICLORUTA
#Genera un histograma de los accidentes en ciclorutas por comunas
Via=df[(df['DISENO']=='Ciclo Ruta')]
pd.Series(Via['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentes en Ciclo ruta por Comunas para el 2016')
plt.show()
############################################
#COMUNA
#Genera un histograma de accidentalidad por comuna
pd.Series(df['COMUNA']).value_counts().sort_index().plot('bar',title='Accidentalidad por comuna para el 2016')
plt.show()


############################################
#SEGUNDA SECCION DATOS ESPERADOS 
############################################
#ACCIDENTALIDAD POR DIA DE LA SEMANA
pd.Series(df['DIA']).value_counts().sort_index().plot('bar',title='Accidentalidad por dia para el 2016')
plt.show()
###########################################
#TIPO DE ACCIDENTE
#Genera un histograma por tipo de accidente
pd.Series(df['CLASE']).value_counts().plot('bar',title='Tipo de accidente para el 2016')
plt.show()
############################################
#MUERTES POR CLASE 
Muerto=df[(df['GRAVEDAD']=='MUERTO')]
M=Muerto['CLASE']

pd.Series(M).value_counts().plot('bar',title='Muertes por clase para el 2016')
plt.show()
############################################
#Gravedad por choque
Choque=df[(df['CLASE']=='Choque')]
C=Choque['GRAVEDAD']

pd.Series(C).value_counts().plot('bar',title='Gravedad por choque para el 2016')
plt.show()
############################################
#GRAFICO MUERTES 
GRAVEDAD=[]
for i in range (len(df)):
    
    m=df['GRAVEDAD'][i]
    if m=='MUERTO':
        y=100
    elif m=='HERIDO':
        y=50
        
    elif m=='SOLO DAÑOS':
        y=0
    else:
        pass
    i=i+1
    GRAVEDAD.append(y)
Y1=[]
for i in range (len(df)):
    
    m=df['GRAVEDAD'][i]
    if m=='MUERTO':
        y=300
    elif m=='HERIDO':
        y=20
        
    elif m=='SOLO DAÑOS':
        y=10
    else:
        pass
    i=i+1
    Y1.append(y)
df.plot(kind="scatter", x="X", y="Y", alpha=0.4,
s=Y1, label="Gravedad",
c=GRAVEDAD, cmap=plt.get_cmap("YlOrRd"), colorbar=True, figsize=(18,20),
)
plt.legend()
plt.title('2016')
############################################
############################################
#SECCION 2015
############################################
#COnversion de formato AM Y PM A 24 hora 
df3=pd.read_excel("Accidentalidad_2016.xlsx")
df3['HORA']=pd.to_datetime(df3['HORA']).apply(lambda x: x.hour)
############################################
#Porcentaje de muerte
acc_per_hour = pd.value_counts(df3['HORA'].values).sort_index()
Y=[]
X=np.arange(0,24,1)
for i in range(len(acc_per_hour) ):
    l=df3[(df3['HORA']==i)]
    l=l[l['GRAVEDAD']=='MUERTO']
    S=(len(l)/acc_per_hour[i])*100
    #print(i,S)
    Y.append(S)
############################################
#Accidentes por hora 
pd.Series(df1['HORA']).value_counts().sort_index().plot('bar',title='Accidentes por hora en el 2015').set(xlabel="Hora", ylabel="Intensidad de Accidentalidad")
plt.grid(alpha=0.4)
plt.savefig('AccPorHora1.png')


plt.plot(X,Y,'.')
plt.title('Porcentaje de muerte por hora')
plt.xlabel('Hora del dia')
plt.ylabel('Porcentaje')
plt.grid(alpha=0.4)
#########################################
#MUertes por hora
Muerto=df[(df['GRAVEDAD']=='MUERTO')]
HH=Muerto['HORA']=pd.to_datetime(Muerto['HORA'])
HH=HH.apply(lambda x: x.hour)
pd.Series(HH).value_counts().sort_index().plot('bar',title='Muertes por horas para el 2016')
plt.show()
#########################################
#Arreglo basado en el promedio 
X=np.arange(0,24,1)
Y=[500,400,300,200,300,1000,2200,2500,2000,1800,2000,2200,2500,2600,2600,2600,2700,3000,2600,2400,2000,1600,1100,600]
plt.plot(X,Y,'o')
plt.xlabel=('Horas')
plt.ylabel=('Intensidad')
plt.grid(alpha=0.4)
plt.title('Correcion datos del 2015')
plt.savefig('AccPorHora4.png')
#########################################
#Superposicion 
pd.Series(df1['HORA']).value_counts().sort_index().plot('bar',title='Accidentes por hora en el 2015').grid(alpha=0.4)
X=np.arange(0,24,1)
Y=[500,400,300,200,300,1000,2200,2500,2000,1800,2000,2200,2500,2600,2600,2600,2700,3000,2600,2400,2000,1600,1100,600]
plt.plot(X,Y,'o',c='black')
plt.grid(alpha=0.4)
plt.title('Correcion datos del 2015')
plt.savefig('AccPorHora5.png')
