# DANJACOB project
# Copyright Jacob and Dan 2019
# AI sample code
# purpose of this code is to train a simple AND gate logic using keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

def ai_func():
    # init the randomizer to something
    np.random.seed(10)

    # train a simple AND gate
    # split into input (X) and output (Y) variables
    X = np.array([[1,0],[0,0],[0,1],[1,1]])
    Y = np.array([0,0,0,1])

    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=2, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fit the model
    print ("Now training the network to learn the AND function:")
    model.fit(X, Y, epochs=150, batch_size=2)

    # evaluate the model
    print ("General accuracy of the model:")
    scores = model.evaluate(X, Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    # calculate predictions
    predictions = model.predict(X)
    # round predictions
    # rounded = [round(x[0]) for x in predictions]
    print ("Inputs into the neural net after training to be an AND:\n"+ str(X))
    print("Neural net predictions:\n"+ str(predictions))