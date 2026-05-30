# Project 2    : Data Classification Using AI
# Intern Name  : Divyanjali Mandadi
# Batch        : 2026
# Organization : DecodeLabs
# Algorithm    : K-Nearest Neighbors (KNN)
# Dataset      : Iris Benchmark

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

print("=" * 50)
print("   Iris Flower Classification Model")
print("   DecodeLabs | Batch 2026")
print("   Algorithm: K-Nearest Neighbors")
print("=" * 50)

iris = load_iris()
X = iris.data
y = iris.target

print("\n DATASET OVERVIEW:")
print(f"   Total Samples   : {len(X)}")
print(f"   Total Features  : {X.shape[1]}")
print(f"   Flower Classes  : {list(iris.target_names)}")
print(f"   Feature Names   : {list(iris.feature_names)}")

df = pd.DataFrame(X, columns=iris.feature_names)
df['flower_type'] = [iris.target_names[i] for i in y]
print(f"\n First 5 rows of dataset:")
print(df.head())

print(f"\n Dataset Statistics:")
print(df.describe().round(2))

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print(f"\n DATA SPLIT:")
print(f"   Training Set : {len(X_train)} flowers (80%)")
print(f"   Testing Set  : {len(X_test)} flowers  (20%)")

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(f"\n FEATURE SCALING:")
print(f"   StandardScaler Applied!")
print(f"   Mean = 0, Variance = 1 (Balanced)")

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print(f"\n MODEL TRAINING:")
print(f"   Algorithm : K-Nearest Neighbors")
print(f"   K Value   : 5 neighbors")
print(f"   Status    : Trained Successfully! ")

predictions = model.predict(X_test)

print(f"\n PREDICTIONS:")
for i in range(len(predictions)):
    actual    = iris.target_names[y_test[i]]
    predicted = iris.target_names[predictions[i]]
    status = "✅" if actual == predicted else "❌"
    print(f"   Flower {i+1:2d}: "
          f"Actual={actual:12s} | "
          f"Predicted={predicted:12s} {status}")

print("\n" + "=" * 50)
print("          MODEL PERFORMANCE REPORT")
print("=" * 50)

cm = confusion_matrix(y_test, predictions)
print("\n CONFUSION MATRIX:")
print(f"   (Rows = Actual | Columns = Predicted)\n")
print(f"                Setosa  Versicolor  Virginica")
print(f"   Setosa     :  {cm[0][0]:4d}    {cm[0][1]:4d}        {cm[0][2]:4d}")
print(f"   Versicolor :  {cm[1][0]:4d}    {cm[1][1]:4d}        {cm[1][2]:4d}")
print(f"   Virginica  :  {cm[2][0]:4d}    {cm[2][1]:4d}        {cm[2][2]:4d}")

print("\n CLASSIFICATION REPORT (with F1 Score):")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

accuracy = (predictions == y_test).sum() / len(y_test) * 100
print(f"  Overall Accuracy : {accuracy:.1f}%")

if accuracy >= 95:
    print("   Grade: EXCELLENT ")
elif accuracy >= 85:
    print("   Grade: GOOD ")
else:
    print("   Grade: NEEDS IMPROVEMENT ")
