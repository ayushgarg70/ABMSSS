from keras.layers import Dense,Input,Flatten
import numpy as np
from keras.models import Model
from keras import initializers
from keras import optimizers


class Qvalue:
    def __init__(self,n_inputs):
        self.n_inputs = n_inputs
        self.model=self.create_model()

    def create_model(self):

        input_shape=(self.n_inputs,1)
        n_hidden1=50
        n_hidden2=30
        n_hidden3=20
        n_hidden4=10
        n_outputs=1

        inputs= Input(shape=input_shape)
        x=Flatten()(inputs)
        # kernel_initializer = initializers.Zeros()
        x=Dense(n_hidden1,activation='sigmoid',use_bias=True,kernel_initializer='random_uniform')(x)
        x=Dense(n_hidden2,activation='sigmoid',use_bias=True,kernel_initializer='random_uniform')(x)
        x=Dense(n_hidden3,activation='sigmoid',use_bias=True,kernel_initializer='random_uniform')(x)
        x = Dense(n_hidden4, activation='sigmoid',use_bias=True, kernel_initializer='random_uniform')(x)
        output=Dense(n_outputs)(x)

        model = Model(inputs=inputs, outputs=output)
        sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.1, nesterov=True)
        model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])
        return model

    def train(self,action,price,opposite_bids,target):

        X=np.concatenate(([action],[price],opposite_bids)).T
        X = np.reshape(X, (1, self.n_inputs, 1))
        self.model.train_on_batch(X,[target])

    def get_Qvalue(self,action,price,opposite_bids):

        input = np.concatenate(([action],[price], opposite_bids)).T
        input=np.reshape(input,(1,self.n_inputs,1))

        Qval=self.model.predict(input)

        return Qval

