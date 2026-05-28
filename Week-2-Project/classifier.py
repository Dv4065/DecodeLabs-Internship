# Project 2: Data Classification Using AI
# Intern Name  : Divyanjali Mandadi
# Batch        : 2026
# Organization : DecodeLabs

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

print("   Iris Flower Classification Model")
print("   Powered by KNN Algorithm")

iris = load_iris()
X = iris.data
y = iris.target
print(f"\n Dataset Loaded!")
print(f"   Total flowers : {len(X)}")
print(f"   Flower types  : {iris.target_names}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)
print(f"\n Data Split Done!")
print(f"   Training set  : {len(X_train)} flowers (80%)")
print(f"   Testing set   : {len(X_test)} flowers  (20%)")

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(f"\n Data Scaled and Balanced!")

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
print(f"\n KNN Model Trained! (K=5)")

predictions = model.predict(X_test)
print(f"\n Predictions Complete!")

print("\n" + "="*45)
print("       MODEL PERFORMANCE REPORT")
print("="*45)

print("\n Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\n Full Classification Report:")
print(classification_report(y_test, predictions,
      target_names=iris.target_names))

print("     Project 2 Complete!")
