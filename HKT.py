# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:10:56 2018

@author: Felipe
"""
# Hackaturing 2018

from pandas import DataFrame

# Sequential Model
from keras.models import Sequential
from keras.layers import Dense, Activation

def learning (dados):
	#input de dados
	label = dados['id']
	data = dados['history']
	output = dados['output']
	x = len(data)
	y = len(output)
	data = Dense(data)
	output = Dense(output)

	model = Sequential([
	    Dense(1, input_shape=(x,)),
	    Activation('relu'),
	    Dense(10),
	    Activation('sigmoid'),
	    Dense(y),
	    Activation('softmax'),
	    ])

	print("Modelo pronto")

	# Train the model, iterating on the data in batches of 32 samples
	model.fit(data, output, epochs=3, batch_size=8)

	print("Modelo terminado")
	# evaluate the model
	scores = model.evaluate(data, output)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	return()
