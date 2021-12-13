# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:49:48 2019

@author: Toñi Reina
@Revisor: fermincruz, Mariano González
ÚLTIMA MODIFICACIÓN: 24/01/2020
"""

import csv

from collections import namedtuple
from datetime import datetime, date


Video = namedtuple('Video', 'id_video,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes')

    