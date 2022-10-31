# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:54:51 2022

@author: alumno.invitado
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
  
archivo_excel = pd.read_excel('IBEX35_Sept2018.xls')
#print(archivo_excel.columns)

fecha = archivo_excel['Fecha'].values
promedio = archivo_excel['Promedio'].values
lw = 2 
#Función teorica
plt.plot(fecha , promedio, color='blue', linewidth=lw,label="Funciónteórica")
plt.scatter(fecha, promedio, color='navy', s=30, marker='o', label="Puntos de entrenamiento")
plt.title("Función teórica y puntos de entrenamiento")
plt.show() 
#colores
colors = ['red','orange', 'green', 'purple', 'black', 'brown', 'pink', 'yellow', 'violet', 'teal', 'fuchsia', 'silver', 'indigo']

plt.title("Regresión polinómica")
plt.plot(fecha, promedio, color='blue', linewidth=lw,label="Función teórica")
# y los puntos utilizados para entrenamiento
plt.scatter(fecha, promedio, color='navy', s=30, marker='o', label="Puntos de entrenamiento") 

# Realizar el ajuste de los polinomios de grados 3,4 y 5
for count, degree in enumerate([3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):
 # Ajuste del polinomio de grado 'degree' a los datos de entrenamiento x,y
 coeffs = np.polyfit(fecha,promedio,deg=degree)
 # Determinar y escribir la forma del polinomio
 p = np.poly1d(np.polyfit(fecha, promedio, deg=degree), variable='X')
 print("Polinomio de grado ",degree," : ")
 print(p)
 print("")

 y_pred = np.polyval(np.poly1d(coeffs), fecha)
 print("Error cuadrático medio (ECM): ",1/20*(sum((promedio-y_pred)**2)))
 print("")

 # Dibujar la gráfica del polinomio
 # Calcular la y de la gráfica 'y_plot'
 y_plot = np.polyval(np.poly1d(coeffs), fecha)  
 # Dibujar la gráfica
 plt.plot(fecha, y_plot, color=colors[count], linewidth=lw,label="grado %d" % degree) 
 
 # Leyenda del gráfico
plt.legend(loc='lower left')
# Dibujar el gráfico
plt.show() 
print(fecha)
