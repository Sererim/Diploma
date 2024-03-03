import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from keras import models
import numpy as np

model = models.load_model(filepath="Neural net\\model.h5")

print(model.summary())

data, info = tfds.load('food101', with_info=True, as_supervised=True, shuffle_files=True)

valid = data['validation']


for i, (image, label) in enumerate(valid.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    image = tf.image.resize(image, (224, 224))
    image = tf.cast(tf.expand_dims(image, axis=0), dtype=tf.float32) / 255.0
    plt.imshow(image[0])
    plt.title(str(label.numpy()) + ": " + str(np.argmax(model.predict(image))))
    plt.axis('off')

plt.show()
