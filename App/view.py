"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Catalogo")
    print("2- Cargar información")
    print("3- Caracterizar las reproducciones")
    print("4-  Encontrar música para festejar")
    print("5-  Encontrar música para estudiar")
    print("6-  Encontrar los generos segun el tempo")
    print("6-  Indicar el género musical más escuchado en el tiempo")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.init()    
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont)
        print('Eventos cargados: ' + str(controller.eventsSize(cont)))
    elif int(inputs[0]) == 3:
        conten = input('ingrese la caracteristica de contenido\n')
        mini= input('ingrese el valor minimo\n')
        maxi = input('ingrese el valor maximo\n')
        controller.reproductchar(cont, conten, float(mini), float(maxi))
        sys.exit(0)
    elif int(inputs[0]) == 4:
        min1= input('ingrese el Valor mínimo de la característica Energy\n')
        max1= input('ingrese el Valor máximo de la característica Energy\n')
        min2= input('ingrese el Valor mínimo de la característica Danceability\n')
        max2= input('ingrese el Valor máximo de la característica Danceability\n')
        controller.musicfest(cont, float(min1), float(max1), float(min2), float(max2))
    elif int(inputs[0]) == 5:
        tipo = input("Ingrese la lista de generos que desea buscar, separado por comas ',': ")
        tipo=list(tipo.split(", "))
        ans = controller.generosMusicales(cont, tipo)
        print("Total de reproducciones:" +str(ans[0]))
        for a in range(0, (lt.size(ans[1]))):
            b=lt.getElement(ans[1], a)
            print("---------{0}---------".format(b[0]))
            print("{0} reproducciones: {1} con {2} artistas diferentes".format(b[0], b[1], b[2]))

    else:
        sys.exit(0)
sys.exit(0)
