import numpy as np
import matplotlib.pyplot as plt

#1 def --->Estoy definiendo una funcion 
#2. def ff ---> Definirun nombre el que desee para llamar a la funcion 
#3. def ff(a,b) ---> Definir los parámetros a considerar dentro de mi función
#4.     zz = a +np.exp(b) ---> Opereción usando los parámetros que ingrese
#5.1    print(zz) ---> Outlet imprimir el resultado
#5.2    return zz ---> Retornando el valor de la operación

def kg(a,b):
    fg = a + np.exp(b)
    #print(fg)
    return fg

def kg2(a,b,c):
    fg = np.sin(a-b) + np.log(c)
    return fg

def ave(X):
    fg = np.sum(X)/len(X)
    return fg

a1, a2, a3 = np.pi/4, np.pi/8, 2*np.pi/3
A1 = [21, np.pi/3,28,65]
karo1 = kg(a1,a2)  #aplicación de la primera f
karo2 = kg2(a1,a2,a3)  #aplicación de la segunda f
karo3 = karo1 + karo2  #suma de las 2 funciones

karo4 = ave(A1)
karo5 = np.average(A1)

print(karo4)
print(karo5)







