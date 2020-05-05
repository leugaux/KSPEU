#Вывод результатов
import numpy as np
import matplotlib.pyplot as plt #График для последующего вывода изображений
def test_show(model, test_images, test_labels, start_pos, end_pos):
	predictions = model.predict(test_images[start_pos : end_pos])
	print( np.argmax(predictions, axis = 1) )
	print( test_labels[start_pos : end_pos] )
	for i in range(start_pos , end_pos):
		first_image = test_images[i]
		first_image = np.array(first_image, dtype = 'float')
		pixels = first_image.reshape((28, 28))
		plt.imshow(pixels, cmap = 'gray')
		plt.show()