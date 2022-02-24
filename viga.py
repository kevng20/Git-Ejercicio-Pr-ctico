
import numpy as np
import matplotlib.pyplot as plt


# Parámetros de longitud

x1=np.linspace(0,2,10)
x2=np.linspace(2,4,10)
x3=np.linspace(4,4.5,10)
x_total= np.hstack([x1,x2,x3])
#print(x_total)

# Cálculo de los momentos

M1= 6.5625*x1
M2= -15*(x2**2) + 66.5625*x2 - 60
M3= -15*(x3**2) + 165*x3 - 453.75
M_total= np.hstack([M1,M2,M3])
#print(M_total)

print(x_total, M_total)

# Tamaño de letras en ejes
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# Propiedades de los ejes
fig, ax1 = plt.subplots(1,1,figsize=(4,3))
ax1.plot(x_total, M_total, '--k',lw=1.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_position(('data',0))
plt.yticks(np.arange(-40,20,10))
ax1.invert_yaxis()
#plt.savefig("vigaPy.jpg")
plt.show()

