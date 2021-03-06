#model.py
#Построим модель. 3 слоя.
#2 слоя 64 нейронами и функцией ReLu
#1 слой с 10 нейронами и функцией Softmax
from keras.models import Sequential #Архитектура нейросети
from keras.layers import Dense #Слой в нейросети
from keras.utils import to_categorical
def model_build(train_images, train_labels, test_images, test_labels):
	model = Sequential()
	model.add( Dense(64, activation='relu', input_dim=784) )
	model.add( Dense(64, activation='relu') )
	model.add( Dense(10, activation='softmax') )

	#Компилирование модели
	model.compile(
	    optimizer = 'adam',
	    loss = 'categorical_crossentropy',
	    metrics = ['accuracy']
	)
	#Тренировка модели
	model.fit(
	    train_images,
	    to_categorical(train_labels),
	    epochs = 5,
	    batch_size = 32
	)
	#Оценивание модели
	model.evaluate(
	    test_images,
	    to_categorical(test_labels)
	)
	return model