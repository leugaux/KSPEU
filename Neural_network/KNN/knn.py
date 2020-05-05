#Импорт пакетов и зависимостей
import mnist #Набор данных MNIST
#Загрузка набора данных
train_images = mnist.train_images()#Изображения train-данных
train_labels = mnist.train_labels()#Метки train-данных
test_images = mnist.test_images()#Изображения test-данных
test_labels = mnist.test_labels()#Метки test-данных

import train
train_images, test_images = train.reshape_images(train_images, test_images)

import model
model = model.model_build(train_images, train_labels, test_images, test_labels)

import inference
inference.test_show(model, test_images, test_labels, 9500, 9505)