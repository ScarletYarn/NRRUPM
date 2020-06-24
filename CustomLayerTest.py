from tensorflow import keras
import tensorflow as tf
import numpy as np

class Linear(keras.layers.Layer):
    def __init__(self, units=32):
        super(Linear, self).__init__()
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="random_normal",
            trainable=True,
        )
        self.b = self.add_weight(
            shape=(self.units,), initializer="random_normal", trainable=True
        )

    def call(self, inputs):
        print(inputs)
        return tf.matmul(inputs, self.w) + self.b


x = tf.Variable([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=tf.float32)
# At instantiation, we don't know on what inputs this is going to get called
linear_layer = Linear(32)

# The layer's weights are created dynamically the first time the layer is called
y = linear_layer(x)

# print(y)
