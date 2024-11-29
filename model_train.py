import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

# Example: 100 students, 6 timesteps (years), 6 feature (marks per year)

X = np.random.randint(40, 100, size=(100, 6,6))  # Input
y = np.random.randint(40,100,size=(100,6))     # Output (future marks)

#split train and test data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential([
    LSTM(64, activation='relu', input_shape=(6, 6)),  # 6 years, 6 subjects
    Dense(6)  # six output (future marks)
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test), verbose=1)

# Evaluate the model
loss, mae = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}, Test MAE: {mae:.4f}")
