from limpieza import *
from funciones import *
import matplotlib
from scipy.spatial.distance import pdist, squareform

#Resumen de limpieza:
# Creo la base de datos con la que hacer el sistema de recomendacion.
#pacientes: La base de datos de la union (datos + Tta)
#pacientes_t: Base de datos traspuesta

#Creo la matriz de recomendación
columnas=pacientes["Identificador de paciente"].tolist()
pacientes_t=pacientes.T
pacientes_t.columns = columnas
pacientes_t.drop(["Identificador de paciente"],axis=0,inplace=True)

distancia = pdist(pacientes_t.T, 'euclidean')
distancia_matrix = squareform(distancia)
distancia = pd.DataFrame(1/(1 + distancia_matrix), index=pacientes_t.columns, columns=pacientes_t.columns)

#Escojo un paciente al que recomendarle
pacient=pacientes[pacientes["Identificador de paciente"]==PERSONAL]

#Seleciono los 3 pacientes mas afines a las circustancias de nuestro paciente según su proximidad.
similar = distancia[PERSONAL].sort_values(ascending=False)[1:]
dic = dict(similar.head(3))

#Paso a lista los pacientes guias
guias= (list(dic.keys()))

#Visualizo los farmacos de los pacientes recomendados obteniendo solo las columnas de todos los tratamientos
#posibles
farma=pacientes.columns[-132:]
p_s = pacientes[pacientes["Identificador de paciente"].isin(guias)][farma]

#Aplico la funcion vacias, para eliminar todas las columnas
sin=vacias(p_s)
p_s.drop(sin,axis=1,inplace=True)

#Sumo los farmacos recomendados y ordenos de mas repetidos a menos
p_s = p_s.sum()
p_s.sort_values(axis=0,ascending=False)

#Grafica de sectores para ilustrar las recomendaciones
p_s.plot.pie()

#Paso a DataFrame los farmacos recomendados
x = dict(p_s)
data = pd.Series(x).reset_index(name='Frecuencia').rename(columns={'index':'Farmaco'})
