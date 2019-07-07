#!/usr/bin/env python
# -*- coding: utf-8 -*
import  skfuzzy  as  fuzz 
import numpy as np
import matplotlib.pyplot as plt

tamano_taza = np.arange(0, 450, 30)
temperatura_ambiental = np.arange(0, 45, 3)
intensidad_cafe = np.arange(0,6, 0.4 )


nivel_agua = np.arange(0, 450, 30)
cantidad_cafe = np.arange(0,22,1.5)
cantidad_leche = np.arange(0,22,1.5)
cantidad_chocolate = np.arange(0,22,1.5)
tiempo_preparacion = np.arange(0,3,0.2)

'''
FUSIFICACIÓN

trimp(x,[a,b,c]) 
x = arreglo al que se le asignará la pertenencia
a = valor inicial de la función de pertenencia
b = valor que tendrá pertenencia 1
c = valor final de la función de pertenencia
retorna un arreglo con los resultados de las funciones de pertenencia del
x ingresado
'''
#ANTECEDENTES
def antecedentesTaza():
    tamT_lo = fuzz.trimf(tamano_taza, [0, 0, 150])
    tamT_md = fuzz.trimf(tamano_taza, [90, 150, 250])
    tamT_hi = fuzz.trimf(tamano_taza, [150, 450, 450])
    return tamT_lo, tamT_md, tamT_hi

def antecedentesTemperatura():
    tempA_lo = fuzz.trimf(temperatura_ambiental, [0, 0, 18])
    tempA_md = fuzz.trimf(temperatura_ambiental, [9, 24, 30])
    tempA_hi = fuzz.trimf(temperatura_ambiental, [27, 45, 45])
    return tempA_lo, tempA_md, tempA_hi

def antecedentesIntensidad():
    intC_lo = fuzz.trimf(intensidad_cafe, [0, 0, 3])
    intC_md = fuzz.trimf(intensidad_cafe, [0, 3, 4])
    intC_hi = fuzz.trimf(intensidad_cafe, [3, 5, 5])
    return intC_lo, intC_md, intC_hi

#CONSECUENCIAS
def consecuenciasNivel():
    nivelA_lo = fuzz.trimf(nivel_agua, [0,0,150])
    nivelA_md = fuzz.trimf(nivel_agua, [90,150,250])
    nivelA_hi = fuzz.trimf(nivel_agua, [150,450,450]) 
    return nivelA_lo, nivelA_md, nivelA_hi

def consecuenciasCantCafe():
    cantC_lo = fuzz.trimf(cantidad_cafe, [0,0,9])
    cantC_md = fuzz.trimf(cantidad_cafe, [7.5,9,15])
    cantC_hi = fuzz.trimf(cantidad_cafe, [13.5,15,21]) 
    return cantC_lo, cantC_md, cantC_hi

def consecuenciasCantLeche():
    cantL_lo = fuzz.trimf(cantidad_leche, [0,0,9])
    cantL_md = fuzz.trimf(cantidad_leche, [7.5,9,15])
    cantL_hi = fuzz.trimf(cantidad_leche, [13.5,15,21]) 
    return cantL_lo, cantL_md, cantL_hi

def consecuenciasCantTiempo():
    cantT_lo = fuzz.trimf(tiempo_preparacion, [0,0,1])
    cantT_md = fuzz.trimf(tiempo_preparacion, [0.8,1,2])
    cantT_hi = fuzz.trimf(tiempo_preparacion, [1.8,2,3]) 
    return cantT_lo, cantT_md, cantT_hi

def consecuenciasCantChocolate():
    cantChoc_lo = fuzz.trimf(cantidad_chocolate, [0,0,9])
    cantChoc_md = fuzz.trimf(cantidad_chocolate, [7.5,9,15])
    cantChoc_hi = fuzz.trimf(cantidad_chocolate, [13.5, 15, 21])
    return cantChoc_lo, cantChoc_md, cantChoc_hi

#Interpolaciones
'''
interp_membership obtiene el valor de pertenencia para el parámetro ingresado
si es que este no se encuentra en el arreglo definido anteriormente (con trimf)
Se debe realizar para cada parámetro que se ingresa al inicio del programa

interp_membership(x, y, z)
x = arreglo con valores posibles de entrada 
y = valores de función de pertenencia
z = valor que se busca en la pertenencia 

'''
def interpNivelCafe(tamano_taza, tamT_lo, tamT_md, tamT_hi, cantidadCafe):
    nivel_cafe_lo = fuzz.interp_membership(tamano_taza, tamT_lo, cantidadCafe)
    nivel_cafe_md = fuzz.interp_membership(tamano_taza, tamT_md, cantidadCafe)
    nivel_cafe_hi = fuzz.interp_membership(tamano_taza, tamT_hi, cantidadCafe)
    return nivel_cafe_lo, nivel_cafe_md, nivel_cafe_hi

def interpNivelTemp(temperatura_ambiental, tempA_lo, tempA_md, tempA_hi, temperatura):
    nivel_temp_lo = fuzz.interp_membership(temperatura_ambiental, tempA_lo, temperatura)
    nivel_temp_md = fuzz.interp_membership(temperatura_ambiental, tempA_md, temperatura)
    nivel_temp_hi = fuzz.interp_membership(temperatura_ambiental, tempA_hi, temperatura)
    return nivel_temp_lo, nivel_temp_md, nivel_temp_hi

def interpIntensidad(intensidad_cafe, intC_lo, intC_md, intC_hi, intensidad):
    nivel_int_lo = fuzz.interp_membership(intensidad_cafe, intC_lo, intensidad)
    nivel_int_md = fuzz.interp_membership(intensidad_cafe, intC_md, intensidad)
    nivel_int_hi = fuzz.interp_membership(intensidad_cafe, intC_hi, intensidad)
    return nivel_int_lo, nivel_int_md, nivel_int_hi

def appendLvls(lista, a, b, c):
    lista.append(a), lista.append(b), lista.append(c)
    return lista

def plotFuzzy(rangos, lows, mediums, highs):
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

    ax0.plot(rangos[0], lows[0], 'b', linewidth=1.5, label='Pequeno')
    ax0.plot(rangos[0], mediums[0], 'g', linewidth=1.5, label='Mediano')
    ax0.plot(rangos[0], highs[0], 'r', linewidth=1.5, label='Grande')
    ax0.set_title('Tamano Taza')
    ax0.legend()

    ax1.plot(rangos[1], lows[1], 'b', linewidth=1.5, label='Frio')
    ax1.plot(rangos[1], mediums[1], 'g', linewidth=1.5, label='Calido')
    ax1.plot(rangos[1], highs[1], 'r', linewidth=1.5, label='Caluroso')
    ax1.set_title('Temperatura ambiental')
    ax1.legend()


    ax2.plot(rangos[2], lows[2], 'b', linewidth=1.5, label='Suave')
    ax2.plot(rangos[2], mediums[2], 'g', linewidth=1.5, label='Medio')
    ax2.plot(rangos[2], highs[2], 'r', linewidth=1.5, label='Fuerte')
    ax2.set_title('Intensidad cafe')
    ax2.legend()

    plt.show()


def plotDefuzz(aggregated, defusificado, activation, levels, rango):
    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))
    zeros = np.zeros_like(rango)
    ax0.plot(rango, levels[0], 'b', linewidth=0.5, linestyle='--', )
    ax0.plot(rango, levels[1], 'g', linewidth=0.5, linestyle='--')
    ax0.plot(rango, levels[2], 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(rango, zeros, aggregated, facecolor='Orange', alpha=0.7)
    ax0.plot([defusificado, defusificado], [0, activation], 'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Aggregated membership and result (line)')

    # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    plt.tight_layout()
    plt.show()



def defusificacion(rango, cons1, cons2, cons3, cons4, cons5, cons6, levels):
    print('hola')
    aggregated = np.fmax(cons1, np.fmax(cons2, np.fmax(cons3,np.fmax(cons4,np.fmax(cons5,cons6)))))
    defusificado = fuzz.defuzz(rango, aggregated, 'centroid')
    activation = fuzz.interp_membership(rango, aggregated, defusificado)
    plotDefuzz(aggregated, defusificado, activation, levels, rango)
    return defusificado, activation

'''
En esta seccion se obtienen lso valores pertinentes para comenzar a aplicar lógica
difusa y se comienzan a aplicar las reglas pertinentes

'''
def aplicarReglas(cantidadCafe, temperatura, intensidad, tipo):
    #ANTECEDENTES
    tamT_lo, tamT_md, tamT_hi = antecedentesTaza()
    tempA_lo, tempA_md, tempA_hi = antecedentesTemperatura()
    intC_lo, intC_md, intC_hi = antecedentesIntensidad()

    #CONSECUENCIAS
    nivelA_lo, nivelA_md, nivelA_hi = consecuenciasNivel()
    cantC_lo, cantC_md, cantC_hi = consecuenciasCantCafe()
    cantL_lo, cantL_md, cantL_hi = consecuenciasCantLeche()
    cantT_lo, cantT_md, cantT_hi = consecuenciasCantTiempo()
    cantCho_lo, cantCho_md, cantCho_hi = consecuenciasCantChocolate()

    #INTERPOLACIONES
    nivel_cafe_lo, nivel_cafe_md, nivel_cafe_hi = interpNivelCafe(tamano_taza, tamT_lo, tamT_md, tamT_hi, cantidadCafe)
    nivel_temp_lo, nivel_temp_md, nivel_temp_hi = interpNivelTemp(temperatura_ambiental, tempA_hi,tempA_md, tempA_hi, temperatura)
    nivel_int_lo, nivel_int_md, nivel_int_hi = interpIntensidad(intensidad_cafe, intC_lo, intC_md, intC_hi, intensidad)


    listaRangos = []
    listaLo = []
    listaMd = []
    listaHi = []
    levels = []
    defusificados = []
    activations = []
    defu = 0.0
    activ = 0.0
    listaRangos.append(nivel_agua), listaRangos.append(cantidad_cafe), listaRangos.append(cantidad_leche)
    listaLo = appendLvls(listaLo, tamT_lo, tempA_lo, intC_lo)
    listaMd = appendLvls(listaMd, tamT_md, tempA_md, intC_md)
    listaHi = appendLvls(listaHi, tamT_hi, tempA_md, intC_hi)

    #GRAFICO de los conjuntos difusos
    plotFuzzy(listaRangos, listaLo, listaMd, listaHi)
    cons1=0
    cons2=0
    cons3=0
    cons4=0
    cons5=0
    cons6=0

    if tipo == 'Espresso':
        active_rule1 = np.fmax(nivel_cafe_lo, np.fmax( nivel_temp_lo,nivel_int_lo))
        active_rule2 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_md, nivel_int_hi))
        active_rule3 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_md, nivel_int_md))
        active_rule4 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_hi, nivel_int_hi))
        active_rule5 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_lo, nivel_int_lo))
        active_rule6 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_hi, nivel_int_md))

        cons1 = np.fmin(active_rule1, np.fmin(nivelA_lo, np.fmin(cantC_lo, cantT_md)) )
        cons2 = np.fmin(active_rule2, np.fmin(nivelA_lo, np.fmin(cantC_md, cantT_lo)) )
        cons3 = np.fmin(active_rule3, np.fmin(nivelA_md, np.fmin(cantC_lo, cantT_lo)) )
        cons4 = np.fmin(active_rule4, np.fmin(nivelA_md, np.fmin(cantC_md, cantT_lo)) )
        cons5 = np.fmin(active_rule5, np.fmin(nivelA_hi, np.fmin(cantC_md, cantT_md)) )
        cons6 = np.fmin(active_rule6, np.fmin(nivelA_hi, np.fmin(cantC_md, cantT_lo)) )

    elif tipo == 'Capuccino':
        active_rule1 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_lo, nivel_int_lo))
        active_rule2 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_md, nivel_int_hi))
        active_rule3 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_md, nivel_int_md))
        active_rule4 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_hi, nivel_int_hi))
        active_rule5 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_md, nivel_int_lo))
        active_rule6 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_lo, nivel_int_hi))

        cons1 = np.fmin(active_rule1, np.fmin(nivelA_lo, np.fmin(cantC_lo, np.fmin(cantL_md, cantT_md))))
        cons2 = np.fmin(active_rule2, np.fmin(nivelA_lo, np.fmin(cantC_md, np.fmin(cantL_lo, cantT_lo))))
        cons3 = np.fmin(active_rule3, np.fmin(nivelA_md, np.fmin(cantC_md, np.fmin(cantL_md, cantT_md))))
        cons4 = np.fmin(active_rule4, np.fmin(nivelA_md, np.fmin(cantC_md, np.fmin(cantL_lo, cantT_lo))))
        cons5 = np.fmin(active_rule5, np.fmin(nivelA_hi, np.fmin(cantC_lo, np.fmin(cantL_md, cantT_md))))
        cons6 = np.fmin(active_rule6, np.fmin(nivelA_hi, np.fmin(cantC_md, np.fmin(cantL_lo, cantT_hi))))

    elif tipo == 'Latte':
        active_rule1 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_lo, nivel_int_lo))
        active_rule2 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_hi, nivel_int_md))
        active_rule3 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_md, nivel_int_md))
        active_rule4 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_hi, nivel_int_hi))
        active_rule5 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_lo, nivel_int_hi))
        active_rule6 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_md, nivel_int_lo))

        cons1 = np.fmin(active_rule1, np.fmin(nivelA_lo, np.fmin(cantC_lo, np.fmin(cantL_md, cantT_md))))
        cons2 = np.fmin(active_rule2, np.fmin(nivelA_lo, np.fmin(cantC_lo, np.fmin(cantL_lo, cantT_lo))))
        cons3 = np.fmin(active_rule3, np.fmin(nivelA_md, np.fmin(cantC_md, np.fmin(cantL_md, cantT_lo))))
        cons4 = np.fmin(active_rule4, np.fmin(nivelA_md, np.fmin(cantC_hi, np.fmin(cantL_lo, cantT_lo))))
        cons5 = np.fmin(active_rule5, np.fmin(nivelA_hi, np.fmin(cantC_hi, np.fmin(cantL_lo, cantT_hi))))
        cons6 = np.fmin(active_rule6, np.fmin(nivelA_hi, np.fmin(cantC_lo, np.fmin(cantL_hi, cantT_md))))

    elif tipo == 'Mokaccino':
        active_rule1 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_md, nivel_int_hi))
        active_rule2 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_hi, nivel_int_lo))
        active_rule3 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_lo, nivel_int_md))
        active_rule4 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_hi, nivel_int_hi))
        active_rule5 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_lo, nivel_int_hi))
        active_rule6 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_md, nivel_int_lo))

        cons1 = np.fmin(active_rule1, np.fmin(nivelA_lo, np.fmin(cantC_md, np.fmin(cantL_lo, np.fmin(cantCho_lo, cantT_lo)))))
        cons2 = np.fmin(active_rule2, np.fmin(nivelA_lo, np.fmin(cantC_lo, np.fmin(cantL_md, np.fmin(cantCho_lo, cantT_lo)))))
        cons3 = np.fmin(active_rule3, np.fmin(nivelA_md, np.fmin(cantC_md, np.fmin(cantL_md, np.fmin(cantCho_lo, cantT_md)))))
        cons4 = np.fmin(active_rule4, np.fmin(nivelA_md, np.fmin(cantC_md, np.fmin(cantL_lo, np.fmin(cantCho_lo, cantT_lo)))))
        cons5 = np.fmin(active_rule5, np.fmin(nivelA_hi, np.fmin(cantC_md, np.fmin(cantL_md, np.fmin(cantCho_lo, cantT_hi)))))
        cons6 = np.fmin(active_rule6, np.fmin(nivelA_hi, np.fmin(cantC_lo, np.fmin(cantL_md, np.fmin(cantCho_lo, cantT_md)))))

    
    if tipo != 'Mokaccino' and tipo != 'Espresso':
        l = []
        levels = []
        l.append(nivel_agua)
        l.append(cantidad_cafe)
        l.append(cantidad_leche)
        l.append(tiempo_preparacion)
        for i in range(0,4):
            if i == 0:
                levels = appendLvls(levels, nivelA_lo, nivelA_md, nivelA_hi)
            elif i == 1:
                levels = appendLvls(levels, cantC_lo, cantC_md, cantC_hi)
            elif i == 2:
                levels = appendLvls(levels, cantL_lo, cantL_md, cantL_hi)
            elif i ==3:
                levels = appendLvls(levels, cantT_lo, cantT_md, cantT_hi)
            defu, activ = defusificacion(l[i], cons1, cons2, cons3, cons4, cons5, cons6, levels)
            levels = []
    elif tipo == 'Mokaccino':
        l = []
        levels = []
        l.append(nivel_agua)
        l.append(cantidad_cafe)
        l.append(cantidad_leche)
        l.append(cantidad_chocolate)
        l.append(tiempo_preparacion)
        for i in range(0,5):
            if i == 0:
                levels = appendLvls(levels, nivelA_lo, nivelA_md, nivelA_hi)
            elif i == 1:
                levels = appendLvls(levels,cantC_lo, cantC_md, cantC_hi)
            elif i == 2:
                levels = appendLvls(levels, cantL_lo, cantL_md, cantL_hi)
            elif i == 3:
                levels = appendLvls(levels,cantCho_lo, cantCho_md, cantCho_hi)
            elif i == 4:
                levels = appendLvls(levels,cantT_lo, cantT_md, cantT_hi)
            defu, activ = defusificacion(l[i], cons1, cons2, cons3, cons4, cons5, cons6, levels)
            levels = []
    elif tipo == 'Espresso':
        l = []
        levels = []
        l.append(nivel_agua)
        l.append(cantidad_cafe)
        l.append(tiempo_preparacion)
        for i in range(0,3):
            if i == 0:
                levels = appendLvls(levels, nivelA_lo, nivelA_md, nivelA_hi)
            elif i == 1:
                levels = appendLvls(levels,cantC_lo, cantC_md, cantC_hi)
            elif i == 2:
                levels = appendLvls(levels,cantT_lo, cantT_md, cantT_hi)
            defu, activ = defusificacion(l[i], cons1, cons2, cons3, cons4, cons5, cons6, levels)
            levels = []
















##########################MAIN########################
cantidadCafe = 100
temperatura = 25
intensidad = 4
tipo = 'Espresso'

aplicarReglas(cantidadCafe, temperatura, intensidad, tipo)



