# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:49:48 2019

@author: Toñi Reina
@Revisor: fermincruz, Mariano González
ÚLTIMA MODIFICACIÓN: 13/12/2021 Belén Ramos
"""

import csv
from collections import namedtuple
from datetime import datetime, date
from collections import Counter
import statistics


Video = namedtuple(
    "Video", "id_video,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes"
)

#################
# EJERCICIO 1
#################


def lee_trending_videos(fichero):
    """
    Lee un fichero de entrada en formato CSV y devuelve una lista de tuplas
    de tipo Video conteniendo todos los datos almacenados en el fichero.
    Use: datetime.strptime(cadena_fecha,'%d/%m/%Y').date() para convertir una cadena a fecha
    Recuerde que puede usar el parámetro delimiter en el reader
    Entrada:
        @param fichero: ruta del fichero csv que contiene los datos en codificación utf-8
        @type fichero: str

    Salida:
        @return: lista de tuplas con la información del fichero
        @rtype: [Video(str,date,str,str,str,int,int,int)]
    """
    videos = []
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for (id_video,fecha_trending,
            titulo,canal,categoria,visitas,likes,dislikes,) in lector:
            tupla = Video(id_video,datetime.strptime(fecha_trending, "%d/%m/%Y").date(), titulo,canal,categoria, int(visitas),int(likes),int(dislikes))
            videos.append(tupla)
    return videos


#################
# EJERCICIO 2
#################


def media_visitas(videos, fecha):
    """
    Devuelve la media de visitas de una fecha dada. Si para esa fecha
    no hay registros la función devuelve cero.
    Entrada:
        @param videos: lista de tuplas con la información de vídeos trending
        @type videos: [Video(str,date,str,str,str,int,int,int)]
        @param fecha: fecha de visita
        @type fecha: date

    Salida:
        @return: media de visitas de esa fecha
        @rtype: float
    """
    pass


#################
# EJERCICIO 3
#################


def video_mayor_ratio_likes_dislikes(videos, categoria=None):
    """
        Devuelve la tupla de tipo Video de la categoría dada como parámetro que ha tenido un mayor ratio
        likes/dislikes. Si la categoría toma el valor None, se devolverá la tupla de tipo Video con mayor
        ratio likes/dislikes de todas. El ratio likes/dislikes se calcula como el cociente entre el número
        de likes y el número de dislikes. Tenga en cuenta que puede haber vídeos que no hayan recibido dislikes
        que no deben ser tenidos en cuenta en el cálculo del máximo.
    .
        Entrada:
            @param videos: lista de tuplas con la información de vídeos trending
            @type videos: [Video(str,date,str,str,str,int,int,int)]
            @param categoria: nombre de la categoría del vídeo
            @type categoria: str

        Salida:
            @return: vídeo con mejor ratio likes/dislikes de la categoría dada o de todas.
            @rtype: Video(str,date,str,str,str,int,int,int)
    """
    pass


#################
# EJERCICIO 4
#################


def canales_top(videos, n=3):
    '''
    Devuelve una lista de tuplas (canal, num_videos_trending) con los n canales que tienen
    más vídeos trending. Cada tupla contiene el nombre del canal y el número de vídeos 
    trending de ese canal, teniendo en cuenta que si un vídeo es trending durante d días, 
    contará d veces para el canal. La lista estará ordenada de mayor a menor número de vídeos trending. 
    Entrada:
        @param videos: lista de tuplas con la información de vídeos trending
        @type videos: [Video(str,date,str,str,str,int,int,int)]
        @param n: número de vídeos que se incluiran en el ranking
        @type n: int

    Salida:
        @return: listas de tuplas (canal, num_videos_trending)
        @rtype: [(str, int)]
    '''
    pass

#################
# EJERCICIO 5
#################


def video_mas_likeability_por_categoria(videos, k=20):
    '''
    Devuelve un diccionario que asocia las categorías(claves), con el vídeo de mayor índice 
    likeability de esa categoría. El índice likeability se calcula según la fórmula 
    que se indica en el enunciado.    
    Entrada:
        @param videos: lista de tuplas con la información de vídeos trending
        @type videos: [Video(str,date,str,str,str,int,int,int)]
        @param k: constante usada para el cálculo del índice likeability
        @type k: int

    Salida:
        @return: diccionario de categorías (claves) y vídeos con más likeability de esa categoría
        @rtype: {str:Video(str,date,str,str,str,int,int,int)}
    '''
    pass

#################
# EJERCICIO 6
#################

def incrementos_visitas(videos, canal):
    '''
    Recibe una lista de tuplas de tipo Video y un canal. Devuelve una lista con el incremento (o 
    decremento) del total de visitas diarias de los vídeos trending de un día con respecto al día 
    anterior para el rango de fechas en que hay mediciones. Note que puede haber días para el que 
    se hayan tomado mediciones en los que no aparezca ningún video de un canal concreto, ya que los
    videos de ese canal no han sido tendencia ese día. Sin embargo, esos días habrá que tenerlos 
    en cuenta en el cálculo de los incrementos. Por ejemplo, el canal Mr. Tops no tiene ningún 
    vídeo trending el día 10/01/2017, y el día 11/01/2017 ha obtenido 200487 visitas en videos 
    que son tendencia. En este caso, en la lista resultado debe aparecer un incremento de 200487, 
    aunque no se haya registrado ningún dato de ese canal el día 10/01/2017. 
    Entrada:
        @param videos: lista de tuplas con la información de vídeos trending
        @type videos: [Video(str,date,str,str,str,int,int,int)]
        @param canal: nombre del canal a analizar
        @type canal: str

    Salida:
        @return: lista con incrementos/decrementos de visitas
        @rtype: [int]
    '''
    pass 