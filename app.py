import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load dataset
df = pd.read_csv("logic_gates_dataset.csv")

# 2. Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    df["description"], df["gate"], test_size=0.2, random_state=42
)

# 3. Convert text to numerical features using TF-IDF (unigrams + bigrams)
vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 4. Train classifier
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# 5. Evaluate model
y_pred = model.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"\n--- Model Evaluation ---")
print(f"Test Accuracy: {acc * 100:.2f}%\n")
print(classification_report(y_test, y_pred))

# Save model & vectorizer
joblib.dump(model, "gate_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

# Truth tables for display during live demo
TRUTH_TABLES = {
    "AND":  "A B | Y\n0 0 | 0\n0 1 | 0\n1 0 | 0\n1 1 | 1",
    "OR":   "A B | Y\n0 0 | 0\n0 1 | 1\n1 0 | 1\n1 1 | 1",
    "NOT":  "A | Y\n0 | 1\n1 | 0",
    "NAND": "A B | Y\n0 0 | 1\n0 1 | 1\n1 0 | 1\n1 1 | 0",
    "NOR":  "A B | Y\n0 0 | 1\n0 1 | 0\n1 0 | 0\n1 1 | 0",
    "XOR":  "A B | Y\n0 0 | 0\n0 1 | 1\n1 0 | 1\n1 1 | 0",
    "XNOR": "A B | Y\n0 0 | 1\n0 1 | 0\n1 0 | 0\n1 1 | 1",
}

# 6. Interactive Prediction Loop
print("\n--- Digital Logic Gate Identifier Ready ---")
print("Type a behavior description (or 'exit' to quit):\n")

while True:
    user_input = input("Description > ").strip()
    if user_input.lower() in ["exit", "quit"]:
        break
    if not user_input:
        continue

    vec = vectorizer.transform([user_input])
    prediction = model.predict(vec)[0]
    confidence = max(model.predict_proba(vec)[0]) * 100

    print(f"\nPredicted Gate : {prediction} (Confidence: {confidence:.1f}%)")
    print("Truth Table:")
    print(TRUTH_TABLES[prediction])
    print("-" * 35)