import pandas as pd #Importamos libreria para trabajar con bases
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.path as mpath
def Granulometria():
    malla = pd.Series([ #Malla de los tamices 
        "No 4", #tamiza no 4
        "No 10", #tamiz no 10
        "No 20",  #tamiz no 20
        "No 40", #tamiz no 40
        "No 60",  #tamiz no 60
        "No 140", #tamiz no 140
        "No 200",  #tamiz no 200
        "Fondo", #Material que pasa el tamiz #200 (fondo)
    ])
    abertura=pd.Series([ #abertura de tamiz en mm
        4.75, #abertura tamiz #4
        2, #abertura tamiz #10
        0.85, #abertura tamiz #20
        0.425, #abertura tamiz #40
        0.25, #abertura tamiz #60
        0.106, #abertura tamiz #140
        0.075, #abertura tamiz #200
        0.0, ##Consideramos 0 para el fondo
    ])
    retenido=pd.Series([ #Lo retenido en los tamices en g
        15.5, #retenido en el tamiz no 4
        25.8, #retenido en el tamiz no 10
        60.5, #retenido en el tamiz no 20
        40.2, #retenido en el tamiz no 40
        41.2, #retenido en el tamiz no 60
        15.2, #retenido en el tamiz no 140
        13.2, #retenido en el tamiz no 200
        15.0, #Material que pasa el tamiz no 200 (fondo)
    ])
    granulometria=pd.DataFrame({ #llamamos las columnas creadas
        "malla (in)": malla, 
        "abertura (mm)":abertura,
        "retenido (g)":retenido,
    })
    granulometria['peso de material acumulado']=granulometria['retenido (g)'].cumsum() #columna para el peso del material acumulado
    granulometria['retenido acumulado (%)']=granulometria['peso de material acumulado']*100/226.6 #columna para el retenido acumulado porcentaje
    granulometria['Pasa_porcentaje']=100-granulometria['retenido acumulado (%)'] #% que Pasa

    plt.figure(figsize=(10, 4))  #Tamaño del grafico
    plt.plot(abertura, granulometria['Pasa_porcentaje'],linestyle='-', marker='o', color='k', fillstyle='none',label='Granulometria')  #plot de abertura vs %pasa
    f = interp1d(granulometria['Pasa_porcentaje'], abertura) #definimos una interpolacion respecto a eje x y eje y
    #coordenadas de la interpolacion en y
    y1_cord=60 
    y2_cord=30
    y3_cord=10
    #Interpolación con respecto al eje x
    x1_cord=f(y1_cord) 
    x2_cord=f(y2_cord)
    x3_cord=f(y3_cord)
    #codigo para redondear los valores obtenidos en la interpolación
    x1_formatted = '{:.2f}'.format(x1_cord)
    x2_formatted = '{:.2f}'.format(x2_cord)
    x3_formatted = '{:.2f}'.format(x3_cord)
    #Ploter para que aparezcan en el grafico con sibolización
    plt.scatter(x1_cord, y1_cord, marker='s', s=50, color='k', label='D60='+x1_formatted)
    plt.scatter(x2_cord, y2_cord, marker='<', s=50, color='k', label='D30='+x2_formatted)
    plt.scatter(x3_cord, y3_cord, marker='>', s=50, color='k', label='D10='+x3_formatted)
    #Se grafica la línea de la granulometría
    plt.title('CURVA GRANULOMETRICA',fontsize=10)
    plt.xlabel('Diámetro (mm)')
    plt.ylabel('Porcentaje pasa acumulado (%)')
    plt.ylim(-1,100)
    plt.legend() 
    plt.grid(color='k',lw='0.1',ls='-')
    ax1=plt.gca()
    ax1.invert_xaxis()
    #Agregar el segundo eje x para los nombres de los tamices
    ax2 = ax1.twiny()
    ax2.set_xscale("log")
    ax2.set_xticks(abertura)
    ax2.set_xticklabels(malla, rotation=90, fontsize=8)
    #Agregar linas de los tamices
    ax2.set_xlabel('Tamices')
    ax2.set_xlim(0.075,4.75)
    ax2.invert_xaxis()

    #agregamos nombre lineas verticales
    L_No4 = ([4.75,4.75]) 
    L_No10 = ([2,2]) 
    L_No20 = ([0.85,0.85]) 
    L_No40 = ([0.425,0.425])
    L_No60 = ([0.25,0.25])
    L_No140 = ([0.106,0.106])
    L_No200 = ([0.075,0.075])
    L_rango = ([0,100])
    #se indicca en el plot la ubicación de estas líneas
    plt.plot(L_No4, L_rango, color='grey', lw='1.5', ls='--')
    plt.plot(L_No10, L_rango, color='grey', lw='1.5', ls='--')
    plt.plot(L_No20, L_rango, color='grey', lw='1.5', ls='--') 
    plt.plot(L_No40, L_rango, color='grey', lw='1.5', ls='--')
    plt.plot(L_No60, L_rango, color='grey', lw='1.5', ls='--')
    plt.plot(L_No140, L_rango, color='grey', lw='1.5', ls='--')
    plt.plot(L_No200, L_rango, color='grey', lw='1.5', ls='--')
    #se agrega textos
    plt.text(4.75, 2, 'Grava(Fina)', fontsize=8, rotation=90)
    plt.text(1.95, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
    plt.text(0.415, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
    plt.text(0.075, 2, 'Arena(Fina)', fontsize=8, rotation=90)
    x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
    for x in x_values:
        plt.axvline(x=x, color='grey', ls='-', lw='0.3')
    plt.show()