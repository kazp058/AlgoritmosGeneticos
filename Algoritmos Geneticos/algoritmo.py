import math
import pygame
import random as rnd
import Configuracion as cfg
import funciones as fn

#Bienvenido a este reto de Robotron
#Aqui escribiras tu algoritmo genetico
#Puedes crear mas archivos si deseas modularizar tu codigo

#Para ver la solucion ingresa a https://github.com/kazp058/AlgoritmosGeneticos
#Recuerda subir tu solucion a https://www.facebook.com/groups/914984065598051/
#Veamos quien hace el mejor algoritmo

def crearPoblacion():
    '''
    Esta función crea la población de "jugadores" que van a probar resolver el problema
    Para crear la población siga estos pasos:
    1. Indique cuántos jugadores tendrá su población
    2. Cree un grupo de sprites y asígnelo a la variable poblacion
    3. Cree todos los jugadores. Para cada jugador debe definir una lista de movimientos
       aleatorios. La lista deberá tener cfg.maxMovimientos elementos y cada elemento será
       un entero entre 1 y 4 (1:arriba, 2:abajo, 3:izquierda, 4:derecha) generado de manera
       aleatoria.

    :return: un grupo de sprites (pygame.sprite.Group()) con los jugadores
    '''
    cfg.generaciones = 1
    poblacion = pygame.sprite.Group()

    ######
    ###### Escriba su código aquí
    ######

    #la variable cfg.cuantos indica el tamaño de la primera generación
    poblacion.add(fn.crearIndividuo([])) #esta línea solo muestra como añadir un individuo a la población. ¡Eliminar!

    return poblacion


def calcularSalud(individuo):
    '''
    Esta función calcula la salud de un individuo de la poblacion. El valor de salud debe
    ser almacenado en la variable individuo.salud
    :param individuo: un integrante de la población
    :return: nada
    '''
    individuo.salud = 0

    ######
    ###### Escriba su código aquí
    ######


def seleccionNatural(poblacion):
    '''
    Esta función selecciona a uno o más padres para formar la siguiente generación de jugadores.
    :param poblacion: la generación actual de jugadores (pygame.sprite.Group())
    :return: lista con uno o más padres para la siguiente generación
    '''

    listaPadres = []

    ######
    ###### Escriba su código aquí
    ######

    #Retorna la nueva población
    return listaPadres


def reproducir(padres, cuantos):
    '''
    Esta función crea la siguiente generación de jugadores basado en la lista de padres que recibe.
    La nueva generación debe incorporar lo que la generación de sus padres ha aprendido.
    :param padres: lista con uno o más padres para la siguiente generación
    :param cuantos: el tamaño de la siguiente generación
    :return: un grupo de sprites (pygame.sprite.Group()) con la nueva generación de jugadores
    '''
    nuevaPoblacion = pygame.sprite.Group()

    ######
    ###### Escriba su código aquí
    ######

    #Incrementa el número de la generación
    cfg.generaciones += 1

    #Retorna la nueva población
    return nuevaPoblacion


def mutarHijos(poblacion):
    '''
    Esta función cambia, basado en una probabilidad dada, algunas movimientos de la lista
    de movimientos para cada integrante de la población.
    :param poblacion: la generación actual
    :return: nada
    '''
    for individuo in poblacion:
        mutarMovimientos(individuo, cfg.probMutacion)

    ######
    ###### Modifique esta función si desea utilizar alguna otra política de mutación de la población.
    ###### Por ejemplo, si no desea mutar a todos los hijos, reemplace el for con las instrucciones apropiadas
    ######


def mutarMovimientos(individuo, probabilidad):
    '''
    Esta función muta los movimientos del individuo en base a una probabilidad.
    :param individuo: el individuo a mutar
    :param probabilidad: probabilidad de mutación
    :return: nada
    '''

    #individuo.movimientos es la lista con los movimientos del individuo

    ######
    ###### Escriba su código aquí
    ######