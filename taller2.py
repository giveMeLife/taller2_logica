import  skfuzzy  as  fuzz 
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import sys
sys.path.append('//data.py')
import data



cantidadCafe = 90
temperatura = 120
intensidad = 3
tipo = 'Espresso'


tamano_taza = ctrl.Antecedent(np.arange(0,450,30),'tamanoTaza')
temperatura_ambiental = ctrl.Antecedent(np.arange(0,45,3),'tempAmbiental')
intensidad_cafe = ctrl.Antecedent(np.arange(0,6,0.4),'intensidadCafe')

nivel_agua = ctrl.Consequent(np.arange(0, 450, 30),'nivelAgua')
cantidad_cafe = ctrl.Consequent(np.arange(0,22,1.5),'cantidadCafe')
cantidad_leche = ctrl.Consequent(np.arange(0,22,1.5),'cantidadLeche')
cantidad_chocolate = ctrl.Consequent(np.arange(0,22,1.5),'cantidadChocolate')
tiempo_preparacion = ctrl.Consequent(np.arange(0,3,0.2),'tpoPreparacion')

#Antecedentes
tamano_taza['pequeno'] = fuzz.trimf(tamano_taza.universe, [0,0,150])
tamano_taza['mediano'] = fuzz.trimf(tamano_taza.universe, [90,150,250])
tamano_taza['grande'] = fuzz.trimf(tamano_taza.universe, [150,450, 450])

temperatura_ambiental['frio'] = fuzz.trimf(temperatura_ambiental.universe, [0,0,21])
temperatura_ambiental['calido'] = fuzz.trimf(temperatura_ambiental.universe, [15,24,30])
temperatura_ambiental['caluroso'] = fuzz.trimf(temperatura_ambiental.universe, [27,45, 45])

intensidad_cafe['suave'] = fuzz.trimf(intensidad_cafe.universe, [0,0,3])
intensidad_cafe['fuerte'] = fuzz.trimf(intensidad_cafe.universe, [1,2,3])
intensidad_cafe['medio'] = fuzz.trimf(intensidad_cafe.universe, [3,5, 5])



#Consecuentes
nivel_agua['poca'] = fuzz.trimf(nivel_agua.universe, [0,0,150])
nivel_agua['media'] = fuzz.trimf(nivel_agua.universe, [90,150,250])
nivel_agua['mucha'] = fuzz.trimf(nivel_agua.universe, [150,450,450])

cantidad_cafe['poca'] = fuzz.trimf(cantidad_cafe.universe, [0,0,9])
cantidad_cafe['media'] = fuzz.trimf(cantidad_cafe.universe, [7.5,9,15])
cantidad_cafe['mucha'] = fuzz.trimf(cantidad_cafe.universe, [13.5,15,21])

cantidad_leche['poca'] = fuzz.trimf(cantidad_leche.universe, [0,0,9])
cantidad_leche['media'] = fuzz.trimf(cantidad_leche.universe, [7.5,9,15])
cantidad_leche['mucha'] = fuzz.trimf(cantidad_leche.universe, [13.5,15,21])

cantidad_chocolate['poca'] = fuzz.trimf(cantidad_chocolate.universe, [0,0,9])
cantidad_chocolate['media'] = fuzz.trimf(cantidad_chocolate.universe, [7.5,9,15])
cantidad_chocolate['mucha'] = fuzz.trimf(cantidad_chocolate.universe, [13.5,15,21])

tiempo_preparacion['poca'] = fuzz.trimf(tiempo_preparacion.universe, [0,0,1])
tiempo_preparacion['media'] = fuzz.trimf(tiempo_preparacion.universe, [0.8,1,2])
tiempo_preparacion['mucha'] = fuzz.trimf(tiempo_preparacion.universe, [1.8,2,3])


data.rules('mokaccino',cantidadCafe, temperatura, intensidad, tamano_taza, temperatura_ambiental, intensidad_cafe, nivel_agua, cantidad_cafe, tiempo_preparacion, cantidad_leche, cantidad_chocolate)