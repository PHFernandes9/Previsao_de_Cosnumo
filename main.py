# ------------------Bibliotecas ------------------------------------#


import numpy as np
import pandas as pd
import calendar
from datetime import datetime
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

Curva_tipica = [
    #  CT-08 (Industrial)

         0.44828, 0.44448, 0.42443, 0.40285, 0.41609, 0.44226, 0.50296, 0.84177,
         1.41840, 1.61855, 1.72690, 1.62080, 1.61110, 1.60163, 1.64404, 1.75534,
         1.64330, 1.40273, 1.17373, 0.83101, 0.62876, 0.48362, 0.47292, 0.44404 ]



Multiplicador = [1,1,1,1,1,0.8,0.7]

Curva_Típica_na_semana = []

for i in Multiplicador:
    for j in Curva_tipica:
        Curva_Típica_na_semana.append((i*j))

#Tamanho do Vetor

Tam = len(Curva_Típica_na_semana)


# for i in Curva_Típica_na_semana:
#     Curva_Típica_na_semana[6]


# print(Curva_Típica_na_semana)

# contador = 1
# Lista=[]
# for i in Curva_Típica_na_semana:
#     if contador < 7 == 0:
#         Lista.append(i)
#     contador +=1
             


Segunda=[],Terca=[],Quarta=[],Quinta=[],Sexta=[],Sabado=[],Domingo=[]



for i in range(0,Tam):
    if i < 24:
        Segunda.append({'Segunda': Curva_Típica_na_semana[i]})
    elif (i > 23) and (i <48)  :
        Terca.append({'Terça': Curva_Típica_na_semana[i]})
    elif (i > 47) and (i <72)  :
        Quarta.append({'Quarta': Curva_Típica_na_semana[i]})
    elif (i > 71) and (i <96)  :
        Quinta.append({'Quinta': Curva_Típica_na_semana[i]})
    elif (i > 95) and (i <120)  :
        Sexta.append({'Sexta': Curva_Típica_na_semana[i]})      
    elif (i > 119) and (i <144)  :
        Sabado.append({'Sabado': Curva_Típica_na_semana[i]})             
    elif (i > 143) and (i <168)  :
        Domingo.append({'Domingo': Curva_Típica_na_semana[i]})      
    
df1=pd.DataFrame(Segunda)
df2=pd.DataFrame(Terca)
df3=pd.DataFrame(Quarta)
df4=pd.DataFrame(Quinta)
df5=pd.DataFrame(Sexta)
df6=pd.DataFrame(Sabado)
df7=pd.DataFrame(Domingo)


novo = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1)




