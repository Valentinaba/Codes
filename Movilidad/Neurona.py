import numpy as np
import matplotlib.pyplot as plt
#Las entradas de las matrices son los dos valores ingresados y el valor esperado respectivamente 
#Tabla AND
A=np.array([[1,1,1],[-1,1,-1],[1,-1,-1],[-1,-1,-1]])
#Tabla OR
O=np.array([[1,1,1],[-1,1,1],[1,-1,1],[-1,-1,-1]])
#Tabla XOR compuesta por OR y la negacion del AND, es decir, si P es OR y Q es AND entonces es P y ~Q   
X=np.array([[-1,1,-1],[1,1,1],[1,1,1],[-1,1,-1]])
def Neurona(A):
        #Definicion aleatoria de Pesos y Umbral
        w1=1
        w2=-10
        t=0.5
        for i in range (4):
                #Suma de las entradas multiplicadas por los pesos
                Y=(A[i,0]*w1)+(A[i,1]*w2)+t
                print ('Y=',Y)
                while Y!=A[i,2]:
                        #Supera el umbral o no 
                        if Y > 0:
                                Y=1
                                #Si la salida concuerda con el valor esperado devolver la salida
                                if Y==A[i,2]:
                                        print (Y)
                                        
                                #Reasignacion de pesos y theta     
                                else:
                                        w1=w1+(A[i,2]*A[i,0])
                                        w2=w2+(A[i,2]*A[i,1])
                                        t=t+A[i,2]
                                        Y=(A[i,0]*w1)+(A[i,1]*w2)+t
                                        print w1,w2,t
                                        
                              
                        else:
                                Y=-1
                                #Si la salida concuerda con el valor esperado devolver la salida
                                if Y==A[i,2]:
                                        print (Y)
                                #Reasignacion de pesos y theta             
                                else:
                                        w1=w1+(A[i,2]*A[i,0])
                                       
                                        w2=w2+(A[i,2]*A[i,1])
                                        
                                        t=t+A[i,2]
                                        Y=(A[i,0]*w1)+(A[i,1]*w2)+t
                                        print w1,w2,t
                                        
               
                                   

#Prueba
#AND
print ('AND')
print (Neurona(A))
#OR
print ('OR')
print (Neurona(O))
#XOR
print ('XOR')
print (Neurona(X))
C=np.array([[1,1,-1],[-1,1,-1],[1,-1,-1],[-1,-1,-1]])
Neurona(C)

