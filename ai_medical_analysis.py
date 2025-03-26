import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Simulate medical image data (100 images with 256 features each)
X = np.random.rand(100, 256)  
y = np.random.randint(0, 2, 100)  # Binary labels (0: healthy, 1: tumor)

# Train a simple AI model
model = RandomForestClassifier()
model.fit(X, y)

# Predict on new data (simulated image)
new_image = np.random.rand(1, 256)
prediction = model.predict(new_image)

# Display result
print("Tumor detected!" if prediction[0] == 1 else "No tumor detected.")