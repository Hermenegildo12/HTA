import pandas as pd
import numpy as np
from funciones import *


datos=pd.read_csv("./input/HTA_Enf.csv",sep=";")
borrar=vacias(datos)
datos=datos.drop(columns=borrar,axis=1)
def agrupar(row):
    i="Apnea del sueño (AP)"
    j="Apnea del sueño (Dx)"
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]
datos['Síndrome de apnea obstructiva del sueño (To) I']=datos.apply(lambda row: agrupar(row),axis=1)
una="Apnea del sueño (AP)"
dos="Apnea del sueño (Dx)"
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome de apnea obstructiva del sueño (AP)'
    j='Síndrome de apnea obstructiva del sueño (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]
datos['Síndrome de apnea obstructiva del sueño (To) II']=datos.apply(lambda row: agrupar(row),axis=1)
una='Síndrome de apnea obstructiva del sueño (AP)'
dos='Síndrome de apnea obstructiva del sueño (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Nefritis arteriolar (Dx)'
    j='Nefritis arteriolar (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]
datos['Nefritis arteriolar (To)']=datos.apply(lambda row: agrupar(row),axis=1)
una='Nefritis arteriolar (Dx)'
dos='Nefritis arteriolar (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Arteriosclerosis coronaria (AP)'
    j='Arteriosclerosis coronaria (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Arteriosclerosis coronaria (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Arteriosclerosis coronaria (AP)'
dos='Arteriosclerosis coronaria (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipertrofia ventricular (AP)'
    j='Hipertrofia ventricular (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipertrofia ventricular (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipertrofia ventricular (AP)'
dos='Hipertrofia ventricular (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cardiomegalia hipertrófica (AP)'
    j='Hipertrofia ventricular (To)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipertrofia ventricular (To) I']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cardiomegalia hipertrófica (AP)'
dos='Hipertrofia ventricular (To)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Glomerulonefritis crónica (AP)'
    j='Glomerulonefritis crónica (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Glomerulonefritis crónica (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Glomerulonefritis crónica (AP)'
dos='Glomerulonefritis crónica (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Estenosis de arteria renal (AP)'
    j='Estenosis de arteria renal (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Estenosis de arteria renal (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Estenosis de arteria renal (AP)'
dos='Estenosis de arteria renal (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hiperaldosteronismo primario (AP)'
    j='Hiperaldosteronismo primario (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hiperaldosteronismo primario (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hiperaldosteronismo primario (AP)'
dos='Hiperaldosteronismo primario (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipercortisolismo (AP)'
    j='Hipercortisolismo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipercortisolismo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipercortisolismo (AP)'
dos='Hipercortisolismo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Coartación de aorta (AP)'
    j='Coartación de aorta (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Coartación de aorta (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Coartación de aorta (AP)'
dos='Coartación de aorta (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Estrés aumentado (AP)'
    j='Estrés emocional (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Estrés aumentado (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Estrés aumentado (AP)'
dos='Estrés emocional (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cefalea occipital (AP)'
    j='Cefalea (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cefalea (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cefalea occipital (AP)'
dos='Cefalea (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cefalea (Dx)'
    j='Cefalea vascular (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cefalea (To) I']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cefalea (Dx)'
dos='Cefalea vascular (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cefalea vascular (Dx)'
    j='Cefalea (To) I'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cefalea (To) II']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cefalea vascular (Dx)'
dos='Cefalea (To) I'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cefalea (To)'
    j='Cefalea (To) II'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cefalea (To) 1']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cefalea (To)'
dos='Cefalea (To) II'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome de fatiga crónica (AP)'
    j='Síndrome de fatiga crónica (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Síndrome de fatiga crónica (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Síndrome de fatiga crónica (AP)'
dos='Síndrome de fatiga crónica (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Vértigo y mareos (AP)'
    j='Vértigo y mareos (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Vértigo y mareos (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Vértigo y mareos (AP)'
dos='Vértigo y mareos (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Palpitaciones (AP)'
    j='Palpitaciones (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Palpitaciones (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Palpitaciones (AP)'
dos='Palpitaciones (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Palpitaciones - rápidas (AP)'
    j='Palpitaciones - rápidas (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Palpitaciones - rápidas (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Palpitaciones - rápidas (AP)'
dos='Palpitaciones - rápidas (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Palpitaciones con ritmo regular (AP)'
    j='Palpitaciones con ritmo regular (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Palpitaciones con ritmo regular (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Palpitaciones con ritmo regular (AP)'
dos='Palpitaciones con ritmo regular (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Palpitaciones (0)'
    j='Palpitaciones - rápidas (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Palpitaciones (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Palpitaciones (0)'
dos='Palpitaciones - rápidas (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Palpitaciones (1)'
    j='Palpitaciones con ritmo regular (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Palpitaciones (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Palpitaciones (1)'
dos='Palpitaciones con ritmo regular (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Impotencia (AP)'
    j='Impotencia (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Impotencia (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Impotencia (AP)'
dos='Impotencia (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Vasculopatía (AP)'
    j='Vasculopatía (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Vasculopatía (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Vasculopatía (AP)'
dos='Vasculopatía (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico (IC)'
    j='Accidente cerebrovascular isquémico (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico (IC)'
dos='Accidente cerebrovascular isquémico (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico en territorio de arteria cerebral posterior (AP)'
    j='Accidente cerebrovascular isquémico en territorio de arteria cerebral posterior (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico en territorio de arteria cerebral posterior (AP)'
dos='Accidente cerebrovascular isquémico en territorio de arteria cerebral posterior (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico en territorio de arteria cerebral media (AP)'
    j='Accidente cerebrovascular isquémico en territorio de arteria cerebral media (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (2)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico en territorio de arteria cerebral media (AP)'
dos='Accidente cerebrovascular isquémico en territorio de arteria cerebral media (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico agudo (AP)'
    j='Accidente cerebrovascular isquémico agudo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (3)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico agudo (AP)'
dos='Accidente cerebrovascular isquémico agudo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico en territorio de arteria cerebral anterior (AP)'
    j='Accidente cerebrovascular isquémico (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (4)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico en territorio de arteria cerebral anterior (AP)'
dos='Accidente cerebrovascular isquémico (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico (1)'
    j='Accidente cerebrovascular isquémico (2)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (5)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico (1)'
dos='Accidente cerebrovascular isquémico (2)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico (3)'
    j='Accidente cerebrovascular isquémico (4)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (6)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico (3)'
dos='Accidente cerebrovascular isquémico (4)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Accidente cerebrovascular isquémico (5)'
    j='Accidente cerebrovascular isquémico (6)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Accidente cerebrovascular isquémico (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Accidente cerebrovascular isquémico (5)'
dos='Accidente cerebrovascular isquémico (6)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Trastorno de los vasos capilares (AP)'
    j='Trastorno de los vasos capilares (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Trastorno de los vasos capilares (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Trastorno de los vasos capilares (AP)'
dos='Trastorno de los vasos capilares (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Demencia vascular (AP)'
    j='Demencia vascular (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Demencia vascular (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Demencia vascular (AP)'
dos='Demencia vascular (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Demencia multinfarto (AP)'
    j='Demencia vascular subcortical (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Demencia vascular (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Demencia multinfarto (AP)'
dos='Demencia vascular subcortical (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Demencia vascular mixta cortical y subcortical (Dx)'
    j='Demencia vascular (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Demencia vascular (3)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Demencia vascular mixta cortical y subcortical (Dx)'
dos='Demencia vascular (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Demencia vascular (1)'
    j='Demencia vascular (3)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Demencia vascular (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Demencia vascular (1)'
dos='Demencia vascular (3)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Atrofia cerebral (AP)'
    j='Atrofia cerebral (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Atrofia cerebral (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Atrofia cerebral (AP)'
dos='Atrofia cerebral (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cognición alterada (AP)'
    j='Cognición alterada (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cognición alterada (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cognición alterada (AP)'
dos='Cognición alterada (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Deterioro cognitivo (AP)'
    j='Deterioro cognitivo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Deterioro cognitivo (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Deterioro cognitivo (AP)'
dos='Deterioro cognitivo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cardiopatía hipertensiva (AP)'
    j='Cardiopatía hipertensiva (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cardiopatía hipertensiva (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cardiopatía hipertensiva (AP)'
dos='Cardiopatía hipertensiva (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cognición alterada (To)'
    j='Deterioro cognitivo (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Deterioro cognitivo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cognición alterada (To)'
dos='Deterioro cognitivo (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Cardiopatía isquémica (AP)'
    j='Cardiopatía isquémica (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Cardiopatía isquémica (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Cardiopatía isquémica (AP)'
dos='Cardiopatía isquémica (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Infarto agudo de miocardio (AP)'
    j='Infarto agudo de miocardio (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Infarto agudo de miocardio (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Infarto agudo de miocardio (AP)'
dos='Infarto agudo de miocardio (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Infarto agudo de miocardio sin onda Q (AP)'
    j='Infarto agudo de miocardio sin onda Q (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Infarto agudo de miocardio sin onda Q (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Infarto agudo de miocardio sin onda Q (AP)'
dos='Infarto agudo de miocardio sin onda Q (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Insuficiencia cardíaca sistólica (AP)'
    j='Insuficiencia cardíaca diastólica (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Insuficiencia cardíaca sistólica (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Insuficiencia cardíaca sistólica (AP)'
dos='Insuficiencia cardíaca diastólica (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Insuficiencia cardíaca congestiva (AP)'
    j='Insuficiencia cardíaca congestiva (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Insuficiencia cardíaca congestiva (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Insuficiencia cardíaca congestiva (AP)'
dos='Insuficiencia cardíaca congestiva (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Insuficiencia cardíaca congestiva secundaria (AP)'
    j='Insuficiencia cardíaca congestiva secundaria (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Insuficiencia cardíaca congestiva secundaria (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Insuficiencia cardíaca congestiva secundaria (AP)'
dos='Insuficiencia cardíaca congestiva secundaria (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Fibrilación auricular (AP)'
    j='Fibrilación auricular (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Fibrilación auricular (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Fibrilación auricular (AP)'
dos='Fibrilación auricular (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Fibrilación auricular paroxística (AP)'
    j='Fibrilación auricular paroxística (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Fibrilación auricular paroxística (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Fibrilación auricular paroxística (AP)'
dos='Fibrilación auricular paroxística (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Fibrilación auricular permanente (AP)'
    j='Fibrilación auricular permanente (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Fibrilación auricular permanente (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Fibrilación auricular permanente (AP)'
dos='Fibrilación auricular permanente (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Vasculopatía isquémica periférica (AP)'
    j='Vasculopatía isquémica periférica (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Vasculopatía isquémica periférica (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Vasculopatía isquémica periférica (AP)'
dos='Vasculopatía isquémica periférica (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Dilatación de la aorta (AP)'
    j='Dilatación de la aorta (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Dilatación de la aorta (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Dilatación de la aorta (AP)'
dos='Dilatación de la aorta (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Disfunción renal (AP)'
    j='Disfunción renal (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Disfunción renal (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Disfunción renal (AP)'
dos='Disfunción renal (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Retinopatía hipertensiva (AP)'
    j='Retinopatía hipertensiva (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Retinopatía hipertensiva (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Retinopatía hipertensiva (AP)'
dos='Retinopatía hipertensiva (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Diabetes mellitus (AP)'
    j='Diabetes mellitus (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Diabetes mellitus (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Diabetes mellitus (AP)'
dos='Diabetes mellitus (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Diabetes mellitus tipo 2 (AP)'
    j='Diabetes mellitus tipo 2 (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Diabetes mellitus (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Diabetes mellitus tipo 2 (AP)'
dos='Diabetes mellitus tipo 2 (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Diabetes mellitus (0)'
    j='Diabetes mellitus (1)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Diabetes mellitus (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Diabetes mellitus (0)'
dos='Diabetes mellitus (1)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome de dependencia del tabaco (AP)'
    j='Síndrome de dependencia del tabaco (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Síndrome de dependencia del tabaco (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Síndrome de dependencia del tabaco (AP)'
dos='Síndrome de dependencia del tabaco (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Tabaquismo (AP)'
    j='Tabaquismo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Tabaquismo (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Tabaquismo (AP)'
dos='Tabaquismo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome de dependencia del tabaco (0)'
    j='Tabaquismo (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Tabaquismo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Síndrome de dependencia del tabaco (0)'
dos='Tabaquismo (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipercolesterolemia (AP)'
    j='Hipercolesterolemia (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipercolesterolemia (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipercolesterolemia (AP)'
dos='Hipercolesterolemia (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Dislipemia sin tratamiento (AP)'
    j='Dislipemia mixta (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Dislipemia sin tratamiento (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Dislipemia sin tratamiento (AP)'
dos='Dislipemia mixta (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Dislipemia mixta (Dx)'
    j='Dislipemia sin tratamiento (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Dislipemia (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Dislipemia sin tratamiento (0)'
dos='Dislipemia mixta (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Obesidad (AP)'
    j='Obesidad (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Obesidad (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Obesidad (AP)'
dos='Obesidad (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Obesidad mórbida (AP)'
    j='Obesidad mórbida (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Obesidad mórbida (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Obesidad mórbida (AP)'
dos='Obesidad mórbida (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Obesidad central (AP)'
    j='Obesidad central (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Obesidad central (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Obesidad central (AP)'
dos='Obesidad central (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Obesidad abdominal (AP)'
    j='Obesidad central (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Obesidad central (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Obesidad abdominal (AP)'
dos='Obesidad central (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome metabólico X (AP)'
    j='Síndrome metabólico X (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Síndrome metabólico 0']=datos.apply(lambda row: agrupar(row),axis=1)

una='Síndrome metabólico X (AP)'
dos='Síndrome metabólico X (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Enfermedad metabólica (AP)'
    j='Enfermedad metabólica (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Síndrome metabólico 1']=datos.apply(lambda row: agrupar(row),axis=1)

una='Enfermedad metabólica (AP)'
dos='Enfermedad metabólica (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome metabólico 0'
    j='Síndrome metabólico 1'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Síndrome metabólico (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Síndrome metabólico 0'
dos='Síndrome metabólico 1'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Obesidad (0)'
    j='Obesidad mórbida (To)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Obesidad (9)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Obesidad (0)'
dos='Obesidad mórbida (To)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Obesidad central (To)'
    j='Obesidad (9)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Obesidad (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Obesidad central (To)'
dos='Obesidad (9)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Alcoholismo (AP)'
    j='Alcoholismo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Alcoholismo (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Alcoholismo (AP)'
dos='Alcoholismo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Bebedor de alcohol (AP)'
    j='Bebedor de alcohol (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Alcoholismo (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Bebedor de alcohol (AP)'
dos='Bebedor de alcohol (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Alcoholismo (0)'
    j='Alcoholismo (1)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Alcoholismo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Alcoholismo (0)'
dos='Alcoholismo (1)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Análisis de orina (IC)'
    j='Análisis de orina (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Análisis de orina (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Análisis de orina (IC)'
dos='Análisis de orina (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hematuria (AP)'
    j='Hematuria (AP).1'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hematuria (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hematuria (AP)'
dos='Hematuria (AP).1'
datos.drop([una,dos],axis=1,inplace=True)


def agrupar(row):
    i='Doppler de riñón (IC)'
    j='Doppler de riñón (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Doppler de riñón (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Doppler de riñón (IC)'
dos='Doppler de riñón (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='ECG ambulatorio (IC)'
    j='ECG ambulatorio (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['ECG ambulatorio (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='ECG ambulatorio (IC)'
dos='ECG ambulatorio (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma de 24 horas (IC)'
    j='Electrocardiograma de 24 horas (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma de 24 horas (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma de 24 horas (IC)'
dos='Electrocardiograma de 24 horas (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma: fibrilación auricular (AP)'
    j='Electrocardiograma: fibrilación auricular (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma: fibrilación auricular (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma: fibrilación auricular (AP)'
dos='Electrocardiograma: fibrilación auricular (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma: bloqueo cardíaco (AP)'
    j='Electrocardiograma: bloqueo cardíaco (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma: bloqueo cardíaco (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma: bloqueo cardíaco (AP)'
dos='Electrocardiograma: bloqueo cardíaco (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma: bloqueo auriculoventricular completo (AP)'
    j='Electrocardiograma: bloqueo auriculoventricular completo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma: bloqueo auriculoventricular completo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma: bloqueo auriculoventricular completo (AP)'
dos='Electrocardiograma: bloqueo auriculoventricular completo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Bloqueo auriculoventricular de segundo grado tipo Mobitz I en electrocardiograma (AP)'
    j='Bloqueo auriculoventricular de segundo grado tipo Mobitz I en electrocardiograma (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Bloqueo auriculoventricular de segundo grado tipo Mobitz I en electrocardiograma (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Bloqueo auriculoventricular de segundo grado tipo Mobitz I en electrocardiograma (AP)'
dos='Bloqueo auriculoventricular de segundo grado tipo Mobitz I en electrocardiograma (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma: taquicardia supraventricular (AP)'
    j='Electrocardiograma: arritmia ventricular (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma: taquiarritmias (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma: taquicardia supraventricular (AP)'
dos='Electrocardiograma: arritmia ventricular (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma: fibrilación ventricular (Dx)'
    j='Electrocardiograma: taquiarritmias (0)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma: taquiarritmias (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma: fibrilación ventricular (Dx)'
dos='Electrocardiograma: taquiarritmias (0)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Monitoreo electrocardiográfico (IC)'
    j='Monitoreo electrocardiográfico (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Monitoreo electrocardiográfico (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Monitoreo electrocardiográfico (IC)'
dos='Monitoreo electrocardiográfico (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Dilatación de aurícula cardíaca (AP)'
    j='Dilatación de aurícula cardíaca (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Dilatación de aurícula cardíaca (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Dilatación de aurícula cardíaca (AP)'
dos='Dilatación de aurícula cardíaca (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Dilatación auricular (AP)'
    j='Dilatación auricular (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Dilatación de aurícula cardíaca (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Dilatación auricular (AP)'
dos='Dilatación auricular (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipersomnia diurna (AP)'
    j='Hipersomnia (AP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipersomnia diurna (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipersomnia diurna (AP)'
dos='Hipersomnia (AP)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipersomnia diurna (Dx)'
    j='Hipersomnia (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipersomnia diurna (2)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipersomnia diurna (Dx)'
dos='Hipersomnia (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Edema agudo de pulmón (AP)'
    j='Edema agudo de pulmón (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Edema agudo de pulmón (0)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Edema agudo de pulmón (AP)'
dos='Edema agudo de pulmón (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Edema agudo de pulmón de causa cardíaca (AP)'
    j='Edema agudo de pulmón de causa cardíaca (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Edema agudo de pulmón (1)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Edema agudo de pulmón de causa cardíaca (AP)'
dos='Edema agudo de pulmón de causa cardíaca (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Edema agudo de pulmón (0)'
    j='Edema agudo de pulmón (1)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Edema agudo de pulmón (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Edema agudo de pulmón (0)'
dos='Edema agudo de pulmón (1)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipersomnia diurna (0)'
    j='Hipersomnia diurna (2)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipersomnia diurna (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipersomnia diurna (0)'
dos='Hipersomnia diurna (2)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Dilatación de aurícula cardíaca (0)'
    j='Dilatación de aurícula cardíaca (1)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Dilatación de aurícula cardíaca (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Dilatación de aurícula cardíaca (0)'
dos='Dilatación de aurícula cardíaca (1)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Síndrome de apnea obstructiva del sueño (To) I'
    j='Síndrome de apnea obstructiva del sueño (To) II'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Síndrome de apnea obstructiva del sueño (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Síndrome de apnea obstructiva del sueño (To) I'
dos='Síndrome de apnea obstructiva del sueño (To) II'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hiperparatiroidismo (AP)'
    j='Hiperparatiroidismo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hiperparatiroidismo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hiperparatiroidismo (AP)'
dos='Hiperparatiroidismo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Hipertiroidismo (AP)'
    j='Hipertiroidismo (Dx)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Hipertiroidismo (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Hipertiroidismo (AP)'
dos='Hipertiroidismo (Dx)'
datos.drop([una,dos],axis=1,inplace=True)

def agrupar(row):
    i='Electrocardiograma (IC)'
    j='Electrocardiograma (ICP)'
    if row[i]==row[j]:
        return row[i]
    elif row[i]>row[j]:
        return row[i]
    else:
        return row[j]

datos['Electrocardiograma (To)']=datos.apply(lambda row: agrupar(row),axis=1)

una='Electrocardiograma (IC)'
dos='Electrocardiograma (ICP)'
datos.drop([una,dos],axis=1,inplace=True)

#Elimino las filas que solo tenga 0.

columnas=datos.columns[6:].tolist()
datos['recuento'] = datos[columnas].sum(axis=1)
fil_vac=datos[datos["recuento"]==0].index
datos.drop(fil_vac,axis=0,inplace=True)

#Elimino la columna recuento que habia usado para localizar las filas con valor 0.

datos.drop(['recuento'],axis=1,inplace=True)

#Importo la base de datos con los tratamientos
Tta=pd.read_csv("./input/HTA_Tta.csv",sep=";")

#Funcion para eliminar las columnas que tienen solo valores 0
borrar=vacias(Tta)
Tta=Tta.drop(borrar,axis=1)
Tta.drop(["Tipo de documento"],axis=1,inplace=True)

#Borro las filas que solo contengan valores 0.
columnas=Tta.columns[5:].tolist()
Tta['recuento'] = Tta[columnas].sum(axis=1)
fil_vac=Tta[Tta["recuento"]==0].index
Tta.drop(fil_vac,axis=0,inplace=True)

#Unir datos de los sintomas de los pacientes con sus tratamientos:
#Borro estas columnas para que no se dupliquen cuando la una las bases de datos.
Tta=Tta.drop(["Identificador de episodio", "Fecha del documento","Sexo","Edad","recuento"],axis=1)
union=datos.merge(Tta,how="inner",on="Identificador de paciente")

#Elimino las filas que no tengan ningun valor de la nueva base de datos.
columnas=union.columns[6:].tolist()
union['recuento'] = union[columnas].sum(axis=1)
fil_vac=union[union["recuento"]==0].index
union.drop(fil_vac,axis=0,inplace=True)

#Voy a fusionar todos los episodios de los pacientes en uno solo. Para darle mas peso al sistema de reocomendación.
pacientes=union.drop(["Identificador de episodio","Fecha del documento","Fecha del documento","Tipo de documento",
                      "recuento"],axis=1)
#Agrupo en base a estas variables, dando mas importancia a edad
pacientes=pacientes.groupby(by=["Identificador de paciente","Sexo","Edad"]).sum()

#Al haber hecho el agrupado vuelvo a establecer los valores en presencia(1) o ausencia(0)
columnas=pacientes.columns[:]
for x in pacientes.columns:
    pacientes[x]=pacientes[x].apply(limpiar)
pacientes.reset_index(inplace=True)

#Aplico la funcion sexo a "Sexo" para tenerla en int.
pacientes["Sexo"]=pacientes["Sexo"].apply(sexo)

