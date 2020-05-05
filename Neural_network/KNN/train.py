#Нормализация изображений. Преобразуем значения пикселей (от 0 до 255)
#в диапазон от -0.5 до 0.5 для более легкой тренировки нейросети
def reshape_images(train_images, test_images):
	train_images = (train_images/255)-0.5
	test_images = (test_images/255)-0.5
	#преобразование в вектор. Преобразуем  каждое изображение размером 
	#28 на 28 пикселей в вектор размером 784 (28х28=784)
	train_images = train_images.reshape((-1,784))
	test_images = test_images.reshape((-1,784))
	#Печать информации о массивах
	print(train_images.shape)#60000 строк и 784 столбца
	print(test_images.shape)#10000 строк и 784 столбца
	return train_images, test_images