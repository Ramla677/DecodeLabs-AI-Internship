from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

# Features and labels
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create classification model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

# Display output
print("=" * 50)
print("🌸 IRIS FLOWER CLASSIFICATION SYSTEM 🌸")
print("=" * 50)

print(f"\n✅ Model Accuracy: {round(accuracy * 100, 2)}%")

print("\nSample Predictions:")
for i in range(5):
    print(f"Actual: {y_test[i]} | Predicted: {predictions[i]}")

print("\n🤖 AI Model Trained Successfully!")