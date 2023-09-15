import itertools
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

DataSetName = r"C:\Users\USUARIO\Pictures\Universidad\Semestre 4\Analítica Datos\AnalisisBD\BD_computer+hardware\machine.data "
Data = pd.read_csv(DataSetName, sep=',', header=None)
# print(Data.head())
# print("\n",Data.describe())

NumSamples = Data.shape[0]#Escogemos todas las filas
#print(NumSamples)

PRP_0_20 = Data.loc[ (Data[:][8]>=0) & (Data[:][8]<=20) ]
PRP_21_100 = Data.loc[ (Data[:][8]>=21) & (Data[:][8]<=100) ]
PRP_101_200 = Data.loc[ (Data[:][8]>=101) & (Data[:][8]<=200) ]
PRP_201_300 = Data.loc[ (Data[:][8]>=201) & (Data[:][8]<=300) ]
PRP_301_400 = Data.loc[ (Data[:][8]>=301) & (Data[:][8]<=400) ]
PRP_401_500 = Data.loc[ (Data[:][8]>=401) & (Data[:][8]<=500) ]
PRP_501_600 = Data.loc[ (Data[:][8]>=501) & (Data[:][8]<=600) ]
PRP_600 = Data.loc[ Data[:][8]>=600 ]

NumSamplesPRP1 = (PRP_0_20.shape[0])
NumSamplesPRP2 = (PRP_21_100.shape[0])
NumSamplesPRP3 = (PRP_101_200.shape[0])
NumSamplesPRP4 = (PRP_201_300.shape[0])
NumSamplesPRP5 = (PRP_301_400.shape[0])
NumSamplesPRP6 = (PRP_401_500.shape[0])
NumSamplesPRP7 = (PRP_501_600.shape[0])
NumSamplesPRP8 = (PRP_600.shape[0])

## Imprimiendo resultados
print('Número de muestras totales: ', NumSamples)
print('Número de muestras por clase 1: ',NumSamplesPRP1,' (',100*NumSamplesPRP1/NumSamples,' %)')
print('Número de muestras por clase 2: '+str(NumSamplesPRP2)+' ('+str(round(100*NumSamplesPRP2/NumSamples))+' %)')
print('Número de muestras por clase 3: '+str(NumSamplesPRP3)+' ('+str(round(100*NumSamplesPRP3/NumSamples))+' %)')
