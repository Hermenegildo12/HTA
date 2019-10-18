import pandas as pd
import numpy as np

#Función para selecionar las columnas que solo tienen valores 0.
def vacias (datos):
    borrar=[]
    columnas=datos.columns.tolist()
    for column in columnas:
        sum_total = datos[column].sum()
        if sum_total == 0:
            borrar.append(column)
        else:
            pass
    return borrar

#Función para volver a poner los valores en 0 y 1 una vez sumados.
def limpiar (e):
    if e>=1:
        return 1
    else:
        return 0

#Funcion para pasar a int la columna sexo (0:F,1:M)
def sexo (e):
    if e=="F":
        return 0
    else:
        return 1