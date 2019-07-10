import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl


''' 
Función que pausa la ejecución del programa
Entrada:
Proceso: Se printea un mensaje y se espera a una entrada cualquiera
Salida:
'''
def pausa():
    print("Ingrese un caracter para continuar: ")
    input()

''' 
Función que aproxima un valor a su techo más cercano en un arreglo
Entrada:value->entero array->arreglo lógico difuso
Proceso: Se busca el valor con una diferencia más cercana dentro del arreglo
salida: Retorna el valor conocido como techo
'''
def aprox(value, array):
    x = np.copy(array)
    x = x-value
    x = x[x>=0]
    index = x.argmin()
    return(x[index]+value)


'''
Función que escribe en un archivo de texto las salidas
Entrada: antecedentes->Arreglo con antecedentes, salidas->Arreglo con salidas defusificada
Proceso: Se escribe en el archivo los elementos de los arreglos de entrada
Salida:
'''
def salida(antecedentes, salidas):
    file = open("Cafe_"+str(antecedentes[1])+"_"+str(antecedentes[0])+"_"+str(antecedentes[2])+'_'+str(antecedentes[3])+'.txt', 'w')
    file.write("Nivel de agua: "+str(salidas[0])+"ml\n")
    file.write("Cantidad de cafe: "+str(salidas[1])+"grs\n")
    file.write("Cantidad de leche: "+str(salidas[2])+"grs\n")
    file.write("Cantidad de chocolate: "+str(salidas[3])+"grs\n")
    file.write("Tiempo de preparacion: "+str(salidas[4])+"minutos\n")
    file.close()


''' 
Función que retorna los antecedentes a utilizar para aplicar lógica difusa
Entrada:
Proceso: Crea los antecedentes
Salida:
'''
def antecedentes():
    tamano_taza = ctrl.Antecedent(np.arange(0,450,30),'tamanoTaza')
    temperatura_ambiental = ctrl.Antecedent(np.arange(0,45,3),'tempAmbiental')
    intensidad_cafe = ctrl.Antecedent(np.arange(0,6,0.4),'intensidadCafe')
    return tamano_taza, temperatura_ambiental, intensidad_cafe

''' 
Función que retorna los consecuentes a utilizar para aplicar lógica difusa
Entrada:
Proceso: Crea los consecuentes
Salida:
'''
def consecuentes():
    nivel_agua = ctrl.Consequent(np.arange(0, 450, 30),'nivelAgua')
    cantidad_cafe = ctrl.Consequent(np.arange(0,22,1.5),'cantidadCafe')
    cantidad_leche = ctrl.Consequent(np.arange(0,22,1.5),'cantidadLeche')
    cantidad_chocolate = ctrl.Consequent(np.arange(0,22,1.5), 'cantidadChocolate')
    tiempo_preparacion = ctrl.Consequent(np.arange(0,3,0.2),'tpoPreparacion')
    return nivel_agua, cantidad_cafe, cantidad_leche, cantidad_chocolate, tiempo_preparacion


'''
En esta funcion ocurre la lógica principal del programa, ya que se definen las reglas de antecedentes->consecuencias, y luego se calculan las
defusificaciones de los valores consecuentes, los cuales son enviados para ser escritos en un archivo de texto.

Función que se encarga de crear las reglas de la lógica difusa para generar los resultados de los consecuentes.
Entradas: tipo de cafe, cantidad a preparar, temperatura ambiente, intensidad cafe -> flotante
          tamano_taza, temperatura_ambiental, intensidad_cafe -> Antecedentes
          nivel_agua, cantidad_cafe, tiempo_preparacion, cantidad_leche, cantidad_chocolate -> consecuentes
Salida:

'''
def rules(tipo, cantidad_preparar, temperatura_ambiente, intensidad, tamano_taza, temperatura_ambiental, intensidad_cafe, nivel_agua, cantidad_cafe, tiempo_preparacion, cantidad_leche, cantidad_chocolate):
    
    '''
    La funcion Rule, crea las reglas a utilizar en la logica difusa, donde se anotan los antecedentes, con las variables lócias, and, or, not, segun corresponda
    aplicando internamente mamdani, utilizando función mínimo o máximo o complemento según corresponda. 

    Finalmente, al realizar la defusificacion se usa ControlSystem para poder juntar todas las reglas y obtener los valores que mas se acomoden
    a las reglas.

    Con controlSystemSimulation se simula el sistema difuso, y finalmente con input se ingresan las entradas. 
    '''
    if tipo == 'espresso':
        rule1 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'], tiempo_preparacion['media']))
        rule2 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule3 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['poca'], tiempo_preparacion['poca']))
        rule4 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule5 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['media'], tiempo_preparacion['media']))
        rule6 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['media'], tiempo_preparacion['poca']))

        rule7 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule8 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule9 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'], tiempo_preparacion['media']))
        rule10 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule11 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['media'], tiempo_preparacion['media']))
        rule12 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['poca'], tiempo_preparacion['poca']))
        rule13 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], tiempo_preparacion['media']))

        rule14 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['poca'], tiempo_preparacion['media']))
        rule15 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule16 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['poca'], tiempo_preparacion['poca']))
        rule17 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule18 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], tiempo_preparacion['media']))
        rule19 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], tiempo_preparacion['poca']))
        rule20 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], tiempo_preparacion['poca']))

        rule21 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], tiempo_preparacion['media']))
        rule22 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], tiempo_preparacion['poca']))
        rule23 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], tiempo_preparacion['poca']))
        rule24 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], tiempo_preparacion['poca']))
        rule25 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], tiempo_preparacion['media']))
        rule26 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], tiempo_preparacion['poca']))
        rule27 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], tiempo_preparacion['poca']))

        preparacion_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
        preparacion = ctrl.ControlSystemSimulation(preparacion_ctrl)

        preparacion.input['tamanoTaza'] = cantidad_preparar
        preparacion.input['tempAmbiental'] = temperatura_ambiente
        preparacion.input['intensidadCafe'] = intensidad
        preparacion.compute()
        
        ##########################DESCOMENTAR SI SE QUIERE VER GRAFICOS###########################
        # nivel_agua.view(sim=preparacion)
        # pausa()
        # cantidad_cafe.view(sim=preparacion)
        # pausa()
        # tiempo_preparacion.view(sim=preparacion)
        # pausa()
        salida( (tipo,cantidad_preparar,intensidad, temperatura_ambiente), ( aprox(preparacion.output['nivelAgua'], nivel_agua.universe), aprox(preparacion.output['cantidadCafe'], cantidad_cafe.universe),0, 0, aprox(preparacion.output['tpoPreparacion'], tiempo_preparacion.universe) ) )

        


    elif tipo == 'capuccino':
        rule1 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'],cantidad_leche['media'], tiempo_preparacion['media']))
        rule2 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['media'],cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule3 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['media'], tiempo_preparacion['media']))
        rule4 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule5 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], cantidad_leche['media'], tiempo_preparacion['media']))
        rule6 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['mucha']))

        rule7 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['poca'],tiempo_preparacion['poca']))
        rule8 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['media'], tiempo_preparacion['poca']))
        rule9 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule10 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule11 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['mucha'], tiempo_preparacion['media']))
        rule12 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['poca'], cantidad_leche['media'], tiempo_preparacion['poca']))
        rule13 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['media']))

        rule14 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['poca'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule15 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule16 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['poca'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule17 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule18 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule19 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['poca'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule20 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))

        rule21 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule22 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule23 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule24 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['media'], tiempo_preparacion['poca']))
        rule25 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule26 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], cantidad_leche['media'], tiempo_preparacion['poca']))
        rule27 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['poca']))

        preparacion_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
        preparacion = ctrl.ControlSystemSimulation(preparacion_ctrl)

        preparacion.input['tamanoTaza'] = cantidad_preparar
        preparacion.input['tempAmbiental'] = temperatura_ambiente
        preparacion.input['intensidadCafe'] = intensidad
        preparacion.compute()
        # nivel_agua.view(sim=preparacion)
        # pausa()
        # cantidad_cafe.view(sim=preparacion)
        # pausa()
        # cantidad_leche.view(sim=preparacion)
        # pausa()
        # tiempo_preparacion.view(sim=preparacion)
        # pausa()
        salida( (tipo,cantidad_preparar,intensidad, temperatura_ambiente), (aprox(preparacion.output['nivelAgua'],nivel_agua.universe), aprox(preparacion.output['cantidadCafe'], cantidad_cafe.universe), aprox(preparacion.output['cantidadLeche'],cantidad_leche.universe), 0, aprox(preparacion.output['tpoPreparacion'],tiempo_preparacion.universe) ))

    if tipo == 'latte':
        rule1 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'],cantidad_leche['media'], tiempo_preparacion['media']))
        rule2 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['poca'],cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule3 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['media'], tiempo_preparacion['poca']))
        rule4 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['mucha'], cantidad_leche['poca'],  tiempo_preparacion['poca']))
        rule5 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['poca'],  tiempo_preparacion['mucha']))
        rule6 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], cantidad_leche['mucha'],  tiempo_preparacion['media']))

        rule7 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule8 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule9 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'], cantidad_leche['media'], tiempo_preparacion['media']))
        rule10 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule11 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['mucha'], tiempo_preparacion['media']))
        rule12 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule13 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['media'], tiempo_preparacion['media']))

        rule14 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['poca'], cantidad_leche['mucha'], tiempo_preparacion['media']))
        rule15 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule16 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule17 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule18 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule19 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule20 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['media'], tiempo_preparacion['poca']))

        rule21 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['media'], tiempo_preparacion['media']))
        rule22 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule23 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['poca'], tiempo_preparacion['poca']))
        rule24 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['mucha'], tiempo_preparacion['poca']))
        rule25 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['poca'], tiempo_preparacion['media']))
        rule26 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], cantidad_leche['media'], tiempo_preparacion['poca']))
        rule27 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['media'], tiempo_preparacion['poca']))   

        preparacion_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
        preparacion = ctrl.ControlSystemSimulation(preparacion_ctrl)

        preparacion.input['tamanoTaza'] = cantidad_preparar
        preparacion.input['tempAmbiental'] = temperatura_ambiente
        preparacion.input['intensidadCafe'] = intensidad
        preparacion.compute()
        # nivel_agua.view(sim=preparacion)
        # pausa()
        # cantidad_cafe.view(sim=preparacion)
        # pausa()
        # cantidad_leche.view(sim=preparacion)
        # pausa()
        # tiempo_preparacion.view(sim=preparacion)
        # pausa()
        salida( (tipo,cantidad_preparar,intensidad, temperatura_ambiente), (aprox(preparacion.output['nivelAgua'], nivel_agua.universe), aprox( preparacion.output['cantidadCafe'], cantidad_cafe.universe), aprox(preparacion.output['cantidadLeche'], cantidad_leche.universe), 0, aprox(preparacion.output['tpoPreparacion'], tiempo_preparacion.universe ) ) )


    if tipo == 'mokaccino':
        rule1 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['media'],cantidad_leche['poca'], cantidad_chocolate['poca'], tiempo_preparacion['poca']))
        rule2 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'],cantidad_leche['media'], cantidad_chocolate['poca'], tiempo_preparacion['poca']))
        rule3 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['media'], cantidad_chocolate['poca'], tiempo_preparacion['media']))
        rule4 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], cantidad_chocolate['poca'], tiempo_preparacion['poca']))
        rule5 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['media'], cantidad_chocolate['poca'], tiempo_preparacion['mucha']))
        rule6 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], cantidad_leche['media'], cantidad_chocolate['poca'], tiempo_preparacion['media']))

        rule7 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule8 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule9 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['poca'], cantidad_leche['media'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))
        rule10 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule11 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['poca'], cantidad_cafe['media'], cantidad_leche['mucha'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))
        rule12 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule13 = ctrl.Rule(tamano_taza['pequeno'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['poca'], cantidad_cafe['mucha'], cantidad_leche['media'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))

        rule14 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['poca'], cantidad_leche['mucha'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))
        rule15 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule16 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['frio'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['mucha'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule17 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['mucha'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule18 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))
        rule19 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['mucha'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule20 = ctrl.Rule(tamano_taza['mediano'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['media'], cantidad_cafe['media'], cantidad_leche['media'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))

        rule21 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['media'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))
        rule22 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['frio'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['mucha'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule23 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['media'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule24 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['medio'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['mucha'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule25 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['calido'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['poca'], cantidad_chocolate['poca'] ,tiempo_preparacion['media']))
        rule26 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['suave'], ( nivel_agua['mucha'], cantidad_cafe['poca'], cantidad_leche['media'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))
        rule27 = ctrl.Rule(tamano_taza['grande'] & temperatura_ambiental['caluroso'] & intensidad_cafe['fuerte'], ( nivel_agua['mucha'], cantidad_cafe['mucha'], cantidad_leche['media'], cantidad_chocolate['poca'] ,tiempo_preparacion['poca']))   

        preparacion_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
        preparacion = ctrl.ControlSystemSimulation(preparacion_ctrl)

        preparacion.input['tamanoTaza'] = cantidad_preparar
        preparacion.input['tempAmbiental'] = temperatura_ambiente
        preparacion.input['intensidadCafe'] = intensidad
        preparacion.compute()
        # nivel_agua.view(sim=preparacion)
        # pausa()
        # cantidad_cafe.view(sim=preparacion)
        # pausa()
        # cantidad_leche.view(sim=preparacion)
        # pausa()
        # cantidad_chocolate.view(sim=preparacion)
        # pausa()
        # tiempo_preparacion.view(sim=preparacion)
        # pausa()
        salida( (tipo,cantidad_preparar,intensidad, temperatura_ambiente), ( aprox(preparacion.output['nivelAgua'], nivel_agua.universe), aprox(preparacion.output['cantidadCafe'], cantidad_cafe.universe), aprox(preparacion.output['cantidadLeche'], cantidad_leche.universe), aprox(preparacion.output['cantidadChocolate'], cantidad_chocolate.universe), aprox(preparacion.output['tpoPreparacion'], tiempo_preparacion.universe)) )