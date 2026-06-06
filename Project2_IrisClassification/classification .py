from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("=" * 60)
print("🌸 IRIS FLOWER CLASSIFICATION SYSTEM")
print("=" * 60)

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Loaded Successfully!")
print("Total Samples :", len(X))
print("Total Features:", len(iris.feature_names))

print("\nFeature Names:")
for feature in iris.feature_names:
    print("-", feature)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\n✅ Model Accuracy: {round(accuracy * 100, 2)}%")

print("\nFlower Types:")
for i, flower in enumerate(iris.target_names):
    print(f"{i} -> {flower}")

print("\nEnter Flower Measurements")

sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

user_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(user_data)

flower_name = iris.target_names[prediction[0]]

print("\n🌸 Prediction Result")
print("Predicted Flower:", flower_name)

print("\n🤖 Model Trained and Prediction Completed Successfully!")