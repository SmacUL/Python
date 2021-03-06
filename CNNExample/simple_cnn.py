#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:24:53 2018
 
这个程序展示了一个简单的CNN模型

# 在运行这个程序之前，你需要先搞到mnist.npz的数据集
# 或者在可以翻墙的情况下，你也可以用下面的句子:
#     (train_images, train_labels), (test_images, test_labels) = \
#         mnist.load_data()
# 来代替程序中:
#     (train_images, train_labels), (test_images, test_labels) = \
#         load_mnist_data('./mnist.npz')

 
@author: smac-9
"""


from keras import layers
from keras import models

model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

from keras.datasets import mnist 
from keras.utils import to_categorical

import numpy as np

def load_mnist_data(path='./mnist.npz'):

    f = np.load(path)
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test)


(train_images, train_labels), (test_images, test_labels) = load_mnist_data('./mnist.npz')

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=64)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print("test_acc is ")
print(test_acc)

