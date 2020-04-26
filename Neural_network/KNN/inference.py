for i in range(9500,9505):
  first_image = test_images[i]
  first_image = np.array(first_image, dtype = 'float')
  pixels = first_image.reshape((28, 28))
  plt.imshow(pixels, cmap = 'gray')
  plt.show()