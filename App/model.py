"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalogo():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    catalogo = {'events': None,
                'artistas': None,
                'pistas': None
                }

    catalogo['events'] = lt.newList('SINGLE_LINKED', compareIds)
    catalogo['eventos_id'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)

    catalogo['artistas'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['pistas'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['instrumentalness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['liveness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['speechiness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['danceability'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['valence'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['loudness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['tempo'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['acousticness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalogo['energy'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds) 
    catalogo['mode'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds) 
    catalogo['key'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)   

    return catalogo

# Funciones para agregar informacion al catalogo
def addEvent(catalogo, evento):
    lt.addLast(catalogo['events'], evento)
    om.put(catalogo["eventos_id"], evento["id"], evento)
    om.put(catalogo['artistas'], (evento["artist_id"]), evento["id"])
    om.put(catalogo['pistas'], (evento["track_id"]), evento["id"])

    mapa=catalogo['instrumentalness']
    llave=float(evento["instrumentalness"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['liveness']
    llave=float(evento["liveness"])
    addcontent(catalogo, mapa, llave, evento)
    
    mapa=catalogo['speechiness']
    llave=float(evento["speechiness"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['danceability']
    llave=float(evento["danceability"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['valence']
    llave=float(evento["valence"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['loudness']
    llave=float(evento["loudness"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['tempo']
    llave=float(evento["tempo"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['acousticness']
    llave=float(evento["acousticness"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['energy']
    llave=float(evento["energy"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['mode']
    llave=float(evento["mode"])
    addcontent(catalogo, mapa, llave, evento)

    mapa=catalogo['key']
    llave=float(evento["key"])
    addcontent(catalogo, mapa, llave, evento)

    return catalogo

# Funciones para creacion de datos

def addcontent (catalogo, mapa, llave, evento):
    entry = om.get(mapa, llave)
    if entry is None:
        lista=lt.newList()
        lt.addLast(lista, evento["id"])
        om.put(mapa, llave, lista)
    else:
        datentry = me.getValue(entry)
        lt.addLast(datentry, evento["id"])
# Funciones de consulta
def eventsSize(catalogo):
    print("artistas cargados : "+str(om.size(catalogo['artistas'])))
    print("pistas de audio cargadas : "+str(om.size(catalogo['pistas'])))
    sice=lt.size(catalogo['events'])
    return sice


def reproductchar(catalogo,conten, mini, maxi):

    lst=om.values(catalogo[conten], mini, maxi)
    artistas=lt.newList()
    totcres = 0
    for lstdate in lt.iterator(lst):
        totcres += lt.size(lstdate)
        for even in lt.iterator(lstdate):
            evens=om.get(catalogo["eventos_id"], even)
            artis=me.getValue(evens)["artist_id"]
            if lt.isPresent(artistas, artis)==False:
                lt.addLast(artistas, artis)
    print(totcres)
    print("total artistas")
    print(lt.size(artistas))
    print(lt.size(catalogo['events']))



def musicfest(catalogo, min1, max1, min2, max2):
    lst=om.values(catalogo["energy"], 0.5, 0.75)
    lst2=om.values(catalogo["danceability"], 0.75, 1.0)
    pistas1=lt.newList()
    for lstdate in lt.iterator(lst):
        for even in lt.iterator(lstdate):
            evens=om.get(catalogo["eventos_id"], even)
            artis=me.getValue(evens)["track_id"]
            if lt.isPresent(pistas1, artis)==False:
                lt.addLast(pistas1, artis)
    pistas2=lt.newList()
    for lstdate1 in lt.iterator(lst2):
        for even1 in lt.iterator(lstdate1):
            evens1=om.get(catalogo["eventos_id"], even1)
            artis1=me.getValue(evens1)["track_id"]
            if lt.isPresent(pistas1, artis1):
                lt.addLast(pistas2, artis1)
    print(lt.firstElement(pistas2))
    print("total PISTAS")
    print(lt.size(pistas2))


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
