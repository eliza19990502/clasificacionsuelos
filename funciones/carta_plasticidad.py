import pandas as pd #Importamos libreria para trabajar con bases
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.path as mpath

def Carta_Plasticidad(LL,IP):
  #definimos la funcion de carta de plasticidad
  plt.plot(LL, IP, 'ro') #es el punto y toma las coordenadas x,y
  plt.vlines(LL,0,60,'k','--') #linea vertical, le ponemos rango de un punto a otro 
  plt.annotate('LL',(LL,30)) #la coordenada x es en funcion del limite liquido, y la coordenada y es estatica dependiendo lo que se coloque
  plt.annotate('IP',(20,IP+2)) #es un texto, en este caso el eje y es el variable y el +2 lo sube un poco
  plt.hlines(IP,0,100,'k','--') #linea horizontal 
  plt.xlim (0,100) #limita el area de trabajo en ambos ejes
  plt.ylim(0,60) #limite de trabajo del eje y
  region_MH = np.array([[50,0], [50,22], [100,58], [100,0]]) #Se crea un array para cada zona de la carta de plasticidad
  region_ML = np.array([[25.5,4], [12.4,4], [8,0], [20,0], [50,0], [50,22]])
  region_CH = np.array([[50,22], [100,58], [100,60], [75,60], [50,38]])
  region_CL_ML = np.array([[29.5,7], [15.7,7], [12.4,4], [25.5,4]])
  region_CL = np.array([[15.7,7], [29.5,7], [50,22], [50,38]])
  path_MH = mpath.Path(region_MH) #Un Path de indicación de la zona
  path_CH = mpath.Path(region_CH)
  path_CL = mpath.Path(region_CL)
  path_CL_ML = mpath.Path(region_CL_ML)
  path_ML = mpath.Path(region_ML)
  point = np.array([LL,IP])
  if path_MH.contains_point(point): #Condicionales para el suelo y clasificación
    print('El punto se encuentra en la zona MH Limos de alta plasticidad')
  elif path_CH.contains_point(point):
    print('El punto se encuentra en la zona CH Arcillas de alta plasticidad')
  elif path_CL.contains_point(point):
    print('El punto se encuentra en la zona CL Arcillas de Baja plasticidad')
  elif path_CL_ML.contains_point(point):
    print('El punto se encuentra en la zona CL-ML')
  elif path_ML.contains_point(point):
    print('El punto se encuentra en la zona ML Limos de Baja plasticidad')
  else:
    print('El punto no se encuentra en la carta de plasticidad')
  x=np.array([0,100])
  Linea_A=0.9*(x-8)#Definimos las funciones de linea A y Linea U
  Linea_U=0.73*(x-20)
  plt.plot(x,Linea_A,'darkblue',label="Linea A")
  plt.plot(x, Linea_U,'k:',label="Linea U")
  plt.annotate('Linea A',(90,50),rotation=40) #etiquetas para nombrar las 2 lineas en texto
  plt.annotate('Linea U',(60,45),rotation=45) 
  plt.annotate('CL-ML',(15,5))
  plt.annotate('MH',(80,20))
  plt.annotate('CL',(30,15))
  plt.vlines(50,0,60,'g')
  plt.grid()
  plt.title("CARTA DE PLASTICIDAD",fontsize=10)
  plt.xlabel("límite líquido",fontsize=10)
  plt.ylabel("Índice de plasticidad",fontsize=10)
  plt.legend()
  plt.show()