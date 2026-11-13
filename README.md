# Digital Logic Gate Identifier from Natural Language Descriptions (Project P2)

An NLP-based classification system that maps plain-English descriptions of digital circuit behaviors to their corresponding standard logic gates (`AND`, `OR`, `NOT`, `NAND`, `NOR`, `XOR`, `XNOR`) and displays their truth tables.

---

## Project Overview & Course Outcomes
* **Problem Statement (P2):** Classify natural-language behavior descriptions (e.g., *"output high only when both inputs are high"*) into the correct digital logic gate.
* **CO Coverage:** **CO1, CO2** (Digital Logic Fundamentals & Combinational Gate Behavior)
* **Approach:** Supervised Multi-Class Text Classification using **TF-IDF Vectorization** (unigrams & bigrams) paired with **Logistic Regression**.

---

## Repository Structure

```text
logic-gate-identifier/
├── generate_data.py          # Generates synthetic NLP training dataset (1,050 samples)
├── app.py                    # Trains the model, prints evaluation metrics, and runs CLI demo
├── logic_gates_dataset.csv   # Generated dataset (7 classes x 150 variations)
├── gate_model.pkl            # Saved trained classifier
├── tfidf_vectorizer.pkl      # Saved TF-IDF vectorizer
└── README.md                 # Setup and report generation guide
```

Quick Setup & Execution
1. Clone the Repository
Bash
git clone [https://github.com/imanghosh2006-netizen/digital-logic-gate-identifier.git](https://github.com/imanghosh2006-netizen/digital-logic-gate-identifier.git)
cd digital-logic-gate-identifier
2. Set Up Virtual Environment & Install Dependencies
Linux / macOS:

Bash
python3 -m venv venv
source venv/bin/activate
pip install scikit-learn pandas joblib
Windows (PowerShell):

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install scikit-learn pandas joblib
3. Generate Dataset & Run the Application
Bash
python generate_data.py
python app.py
