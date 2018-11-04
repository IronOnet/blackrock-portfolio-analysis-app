"""
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from keras.optimizers import SGD, Adam
import numpy as np

batch_size = 7
epochs = 5

x_train, y_train = data input
y_vals = y_train

y_train = keras.utils.to_categorical(y_train, len(y_train))

# neural net
model = Sequential()
model.add(Dense(64, activation ='relu', input_dim = 1))
model.add(Dense(len(y_train), activation = 'softmax'))

model.compile(loss='categorical_crossentropy', optimizer=SGD(lr = 0.01), metrics = ['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer = Adam(), metrics = ['accuracy'])

model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs)

def predict(num):
	print(model.predict([num]))
	return y_vals[np.argmax(np.round(model.predict([num]), 3))]

print(predict(20))
"""

