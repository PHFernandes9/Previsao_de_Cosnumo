# ------------------Bibliotecas ------------------------------------#


import numpy as np
import pandas as pd
import calendar
from datetime import datetime
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

Curva_tipica = [
    #  CT-08 (Industrial)

         0.44828, 0.44448, 0.42443, 0.40285, 0.41609, 0.44226, 0.50296, 0.84177,
         1.41840, 1.61855, 1.72690, 1.62080, 1.61110, 1.60163, 1.64404, 1.75534,
         1.64330, 1.40273, 1.17373, 0.83101, 0.62876, 0.48362, 0.47292, 0.44404 ]


# Consum
Multiplicador = [1,1,1,1,1,0.8,0.7]

