#inference.py
#Прогнозирование на первых 5 тестовых изображениях
predictions = model.predict(test_images[9500:9505])
print( np.argmax(predictions, axis = 1) )
print( test_labels[9500:9505] )

for i in range(9500,9505):
  first_image = test_images[i]
  first_image = np.array(first_image, dtype = 'float')
  pixels = first_image.reshape((28, 28))
  plt.imshow(pixels, cmap = 'gray')
  plt.show()
