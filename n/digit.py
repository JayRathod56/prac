import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load MNIST data
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize and flatten input data
X_train = X_train.reshape(-1, 784) / 255.0
X_test = X_test.reshape(-1, 784) / 255.0

# One-hot encode output labels
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# Define neural network architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation="sigmoid", input_shape=(784,)),
    tf.keras.layers.Dense(10, activation="sigmoid")
])

# Compile the model with stochastic gradient descent optimizer
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=["accuracy"])

# Train the model
history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=64,
                    validation_data=(X_test, y_test))

# Evaluate performance on test set
accuracy = model.evaluate(X_test, y_test)[1]
print(f"Test accuracy = {accuracy}")

# Plot two sample images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(X_train[103].reshape(28, 28))
ax2.imshow(X_train[145].reshape(28, 28))
plt.show()

--------------------------------------------
# Alternate  code
import tensorflow as tf
import numpy as np

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Define the model architecture
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# Compile the model
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model on the test data
model.evaluate(x_test, y_test, verbose=2)

# Make predictions on a single image
image = x_test[0]
prediction = model.predict(np.array([image]))
predicted_number = np.argmax(prediction)

# Print the predicted number
print("The predicted number is:", predicted_number)

