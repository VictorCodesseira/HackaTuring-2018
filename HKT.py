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

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:10:56 2018

@author: Felipe
"""
# Hackaturing 2018

# Sequential Model
from keras.models import Sequential
from keras.layers import Dense, Activation

# import clean dataset
#data = # alguma coisa lendo um vetor de entradas
def learning (dados):

	#input de dados
	label = dados[0]
	data = dados[1]
	output = dados [2]
	x = len(data)
	y = len(output)

	model = Sequential([
	    Dense(x, input_shape=(784,)),
	    Activation('relu'),
	    Dense(10),
	    Activation('softmax'),
	    Dense(y),
	    Activation('sigmoid'),
	    ])

	# For a multi-class classification problem
	model.compile(optimizer='rmsprop',
	              loss='categorical_crossentropy',
	              metrics=['accuracy'])


	print("Modelo pronto")

	# Train the model, iterating on the data in batches of 32 samples
	model.fit(data, output, epochs=3, batch_size=32)

	print("Modelo terminado")
	# evaluate the model
	scores = model.evaluate(data, output)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	return()