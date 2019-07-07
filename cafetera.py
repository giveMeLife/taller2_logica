#!/usr/bin/env python
# -*- coding: utf-8 -*
import  skfuzzy  as  fuzz 
import numpy as np
import matplotlib.pyplot as plt

cantidadCafe = 100
temperatura = 25
intensidad = 4
tipo = 'Espresso'


tamano_taza = np.arange(0, 450, 30)
temperatura_ambiental = np.arange(0, 45, 3)
intensidad_cafe = np.arange(0,6, 0.4 )


nivel_agua = np.arange(0, 450, 30)
cantidad_cafe = np.arange(0,22,1.5)
cantidad_leche = np.arange(0,22,1.5)
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
tamT_lo = fuzz.trimf(tamano_taza, [0, 0, 150])
tamT_md = fuzz.trimf(tamano_taza, [90, 150, 250])
tamT_hi = fuzz.trimf(tamano_taza, [150, 450, 450])

tempA_lo = fuzz.trimf(temperatura_ambiental, [0, 0, 18])
tempA_md = fuzz.trimf(temperatura_ambiental, [9, 24, 30])
tempA_hi = fuzz.trimf(temperatura_ambiental, [27, 45, 45])

intC_lo = fuzz.trimf(intensidad_cafe, [0, 0, 3])
intC_md = fuzz.trimf(intensidad_cafe, [0, 3, 4])
intC_hi = fuzz.trimf(intensidad_cafe, [3, 5, 5])

#CONSECUENCIAS
nivelA_lo = fuzz.trimf(nivel_agua, [0,0,150])
nivelA_md = fuzz.trimf(nivel_agua, [90,150,250])
nivelA_hi = fuzz.trimf(nivel_agua, [150,450,450]) 

cantC_lo = fuzz.trimf(cantidad_cafe, [0,0,9])
cantC_md = fuzz.trimf(cantidad_cafe, [7.5,9,15])
cantC_hi = fuzz.trimf(cantidad_cafe, [13.5,15,21]) 

cantL_lo = fuzz.trimf(cantidad_leche, [0,0,9])
cantL_md = fuzz.trimf(cantidad_leche, [7.5,9,15])
cantL_hi = fuzz.trimf(cantidad_leche, [13.5,15,21]) 

cantT_lo = fuzz.trimf(tiempo_preparacion, [0,0,1])
cantT_md = fuzz.trimf(tiempo_preparacion, [0.8,1,2])
cantT_hi = fuzz.trimf(tiempo_preparacion, [1.8,2,3]) 


'''
interp_membership obtiene el valor de pertenencia para el parámetro ingresado
si es que este no se encuentra en el arreglo definido anteriormente (con trimf)
Se debe realizar para cada parámetro que se ingresa al inicio del programa

interp_membership(x, y, z)
x = arreglo con valores posibles de entrada 
y = valores de función de pertenencia
z = valor que se busca en la pertenencia 

'''

nivel_cafe_lo = fuzz.interp_membership(tamano_taza, tamT_lo, cantidadCafe)
nivel_cafe_md = fuzz.interp_membership(tamano_taza, tamT_md, cantidadCafe)
nivel_cafe_hi = fuzz.interp_membership(tamano_taza, tamT_hi, cantidadCafe)

nivel_temp_lo = fuzz.interp_membership(temperatura_ambiental, tempA_lo, temperatura)
nivel_temp_md = fuzz.interp_membership(temperatura_ambiental, tempA_md, temperatura)
nivel_temp_hi = fuzz.interp_membership(temperatura_ambiental, tempA_hi, temperatura)

nivel_int_lo = fuzz.interp_membership(intensidad_cafe, intC_lo, intensidad)
nivel_int_md = fuzz.interp_membership(intensidad_cafe, intC_md, intensidad)
nivel_int_hi = fuzz.interp_membership(intensidad_cafe, intC_hi, intensidad)



'''
SISTEMA DE INFERENCIA (REGLAS)
regla 1: consecuencia: nivel agua poca
regla 2: consecuencia: nivel de agua media
regla 3: consecuencia: nivel de agua mucha

regla 4: consecuencia: cantidad café poca
regla 5: consecuencia: cantidad café media
regla 6: consecuencia: cantidad café mucha

'''
'''
GRÁFICOS
'''
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(tamano_taza, tamT_lo, 'b', linewidth=1.5, label='Pequeno')
ax0.plot(tamano_taza, tamT_md, 'g', linewidth=1.5, label='Mediano')
ax0.plot(tamano_taza, tamT_hi, 'r', linewidth=1.5, label='Grande')
ax0.set_title('Tamano Taza')
ax0.legend()

ax1.plot(temperatura_ambiental, tempA_lo, 'b', linewidth=1.5, label='Frio')
ax1.plot(temperatura_ambiental, tempA_md, 'g', linewidth=1.5, label='Calido')
ax1.plot(temperatura_ambiental, tempA_hi, 'r', linewidth=1.5, label='Caluroso')
ax1.set_title('Temperatura ambiental')
ax1.legend()


ax2.plot(intensidad_cafe, intC_lo, 'b', linewidth=1.5, label='Suave')
ax2.plot(intensidad_cafe, intC_md, 'g', linewidth=1.5, label='Medio')
ax2.plot(intensidad_cafe, intC_hi, 'r', linewidth=1.5, label='Fuerte')
ax2.set_title('Intensidad cafe')
ax2.legend()

plt.show()

if tipo == 'Espresso':
    active_rule1 = np.fmax(nivel_cafe_lo, np.fmax( nivel_temp_lo,nivel_int_lo))
    active_rule2 = np.fmax(nivel_cafe_lo, np.fmax(nivel_temp_md, nivel_int_lo))
    active_rule3 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_md, nivel_int_md))
    active_rule4 = np.fmax(nivel_cafe_md, np.fmax(nivel_temp_hi, nivel_int_hi))
    active_rule5 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_lo, nivel_int_lo))
    active_rule6 = np.fmax(nivel_cafe_hi, np.fmax(nivel_temp_hi, nivel_int_md))

    cons1 = np.fmin(active_rule1, np.fmin(nivelA_lo,cantC_lo, cantT_md) )
    cons2 = np.fmin(active_rule2, np.fmin(nivelA_lo,cantC_md, cantT_lo) )
    cons3 = np.fmin(active_rule3, np.fmin(nivelA_md,cantC_lo, cantT_lo) )
    cons4 = np.fmin(active_rule4, np.fmin(nivelA_md,cantC_md, cantT_lo) )
    cons5 = np.fmin(active_rule5, np.fmin(nivelA_hi,cantC_md, cantT_md) )
    cons6 = np.fmin(active_rule6, np.fmin(nivelA_hi,cantC_md, cantT_lo) )
    print(nivelA_lo)
    print(cantC_lo)
    print(cantT_md)

    print(cons1)
    aggregated = np.fmax(cons1, np.fmax(cons2, np.fmax(cons3,np.fmax(cons4,np.fmax(cons5,cons6)))))
    intensidad = fuzz.defuzz(intensidad_cafe, aggregated, 'centroid')
    tip_activation = fuzz.interp_membership(intensidad_cafe, aggregated,intensidad)
    print(cantidadCafe)
    print(intensidad)

'''    agua = np.zeros_like(nivel_agua)

    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 6))

    ax0.fill_between(nivel_agua, agua, cons1, facecolor='b', alpha=0.7)
    ax0.plot(nivel_agua, cons1, 'b', linewidth=0.5, linestyle='--', )

    ax0.fill_between(nivel_agua, agua, cons2, facecolor='r', alpha=0.7)
    ax0.plot(nivel_agua, cons1, 'r', linewidth=0.5, linestyle='--', )

    ax0.fill_between(nivel_agua, agua, cons3, facecolor='g', alpha=0.7)
    ax0.plot(nivel_agua, cons1, 'g', linewidth=0.5, linestyle='--', )

    ax0.fill_between(nivel_agua, agua, cons4, facecolor='y', alpha=0.7)
    ax0.plot(nivel_agua, cons1, 'y', linewidth=0.5, linestyle='--', )

    ax0.fill_between(nivel_agua, agua, cons5, facecolor='b', alpha=0.7)
    ax0.plot(nivel_agua, cons1, 'b', linewidth=0.5, linestyle='--', )

    ax0.fill_between(nivel_agua, agua, cons6, facecolor='r', alpha=0.7)
    ax0.plot(nivel_agua, cons1, 'r', linewidth=0.5, linestyle='--', )

    ax0.set_title('Output membership activity')

    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    print('a')
    plt.tight_layout()
    plt.show()
'''
