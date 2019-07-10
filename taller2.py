import  skfuzzy  as  fuzz 
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import random
import sys
sys.path.append('//data.py')
import data


def comprobacion(argv):
    if len(argv)<4:
        return False,'Cantidad de argumentos menor a 3'    
    elif len(argv)>4:
        return False,'Cantidad de argumentos mayor a 3'
    else:
        try:
            float(argv[2])
            float(argv[3])
            if(argv[1].lower() != 'espresso' and argv[1].lower() != 'latte' and argv[1].lower() != 'mokaccino' and argv[1].lower() != 'capuccino' ):
                return False, 'Los tipos de preparacion son: Espresso, Latte, Capuccino o Mokaccino'
            return True, '0'
        except ValueError:
            return False, 'cantidadCafe e intensidad deben ser valores numericos'
        
tamano_taza, temperatura_ambiental, intensidad_cafe = data.antecedentes()

nivel_agua, cantidad_cafe, cantidad_leche, cantidad_chocolate, tiempo_preparacion = data.consecuentes()

temperatura = random.choice(temperatura_ambiental.universe)
aux = comprobacion(sys.argv)
if aux[0] == False:
    print(aux[1])
    sys.exit()
else:
    print('los valores ingresados son:\n >Tipo preparacion: %s \n >Tamano taza: %s \n >Temperatura ambiental: %s \n >Intensidad preparacion: %s' %(sys.argv[1], sys.argv[2], str(temperatura), sys.argv[3]))
cantidadCafe = float(sys.argv[2])
intensidad = float(sys.argv[3])
tipo = sys.argv[1].lower()





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


############################DESCOMENTAR SI SE QUIERE VER GRAFICOS#############################
#graficos antecedentes
# tamano_taza.view()
# data.pausa()

# temperatura_ambiental.view()
# data.pausa()
# intensidad_cafe.view()
# data.pausa()

data.rules(tipo,cantidadCafe, temperatura, intensidad, tamano_taza, temperatura_ambiental, intensidad_cafe, nivel_agua, cantidad_cafe, tiempo_preparacion, cantidad_leche, cantidad_chocolate)
print("Programa finalizado con exito!!! Disfrute su cafe!!!")