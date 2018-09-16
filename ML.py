# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:10:56 2018

@author: Felipe
"""
# Hackaturing 2018

from pandas import DataFrame, read_csv

# Sequential Model
from keras.models import Sequential
from keras.layers import Dense, Activation

def learning ():
	#input de dados
	dados = read_csv("lookout_histories.csv")
	data = DataFrame(dados['history']) # Input to system
	output = DataFrame(dados['output']) # Comparison output to system
	output = (output - output.mean()) / (output.max() - output.min()) # Normalization


	model = Sequential()
	model.add(Dense(20, input_dim = data.shape[1], activation = 'relu'))
	model.add(Dense(1, activation = 'sigmoid'))

	print("Modelo pronto")

	model.compile(optimizer='rmsprop',
				loss = 'sparse_categorical_crossentropy',
				metrics=['accuracy'])
	# Train the model, iterating on the data in batches of 32 samples
	model.fit(data, output, epochs=3, batch_size=8)

	print("Modelo terminado")
	# evaluate the model
	scores = model.evaluate(data, output)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	return()

learning()
