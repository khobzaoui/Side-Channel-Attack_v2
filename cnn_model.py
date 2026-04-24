from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Input

class CNNModel:
    def __init__(self, shape):
        self.model = Sequential([
            Input(shape=shape),
            Conv1D(32, 3, activation='relu'),
            MaxPooling1D(2),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, Xtr, ytr, Xte, yte):
        return self.model.fit(Xtr, ytr, epochs=5, validation_data=(Xte, yte))
