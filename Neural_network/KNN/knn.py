#Импорт пакетов и зависимостей
import numpy as np
import mnist #Набор данных MNIST
import matplotlib.pyplot as plt #График
from keras.models import Sequential #Архитектура нейросети
from keras.layers import Dense #Слой в нейросети
from keras.utils import to_categorical

import train.py
