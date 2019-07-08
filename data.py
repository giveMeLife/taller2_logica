import skfuzzy as fuzz
import numpy as numpy
from skfuzzy import control as ctrl

def antecedentes():
    tamano_taza = ctrl.Antecedent(np.arange(0,450,30),'tamanoTaza')
    temperatura_ambiental = ctrl.Antecedent(np.arange(0,45,3),'tempAmbiental')
    intensidad_cafe = ctrl.Antecedent(np.arange(0,6,0.4),'intensidadCafe')
    return tamano_taza, temperatura_ambiental, intensidad_cafe

def consecuentes():
    nivel_agua = ctrl.Consequent(np.arange(0, 450, 30),'nivelAgua')
    cantidad_cafe = ctrl.Consequent(np.arange(0,22,1.5),'cantidadCafe')
    cantidad_leche = ctrl.Consequent(np.arange(0,22,1.5),'cantidadLeche')
    tiempo_preparacion = ctrl.Consequent(np.arange(0,3,0.2),'tpoPreparacion')
    return nivel_agua. cantidad_cafe, cantidad_leche, tiempo_preparacion

def verbalizacionAntecedentes(tipo):
    if tipo == 'tamano':
        tamano_taza['pequeno'] = fuzz.trimf(tamano_taza.universe, [0,0,150])
        tamano_taza['mediano'] = fuzz.trimf(tamano_taza.universe, [90,150,250])
        tamano_taza['grande'] = fuzz.trimf(tamano_taza.universe, [150,450, 450])
        return tamano_taza['pequeno'], tamano_taza['mediano'], tamano_taza['grande']
    
