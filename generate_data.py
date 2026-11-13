import pandas as pd
import random

# Core templates for each logic gate
templates = {
    "AND": [
        "output is high only when both inputs are high",
        "produces 1 if and only if all inputs are 1",
        "output is true when both A and B are true",
        "gives a low output if any input is low",
        "all inputs must be active for the output to turn on",
        "logical multiplication of two binary inputs",
        "high output requires both switches to be closed",
        "output stays 0 unless both inputs are 1"
    ],
    "OR": [
        "output is high if at least one input is high",
        "produces 1 when either A or B or both are 1",
        "output is low only when all inputs are low",
        "gives a true result if any single input is true",
        "logical addition of two binary signals",
        "output turns on when at least one switch is closed",
        "produces 0 only if both inputs are 0",
        "high output whenever one or more inputs are active"
    ],
    "NOT": [
        "inverts the input signal",
        "output is the exact opposite of the input",
        "produces 1 when input is 0 and 0 when input is 1",
        "complements a single binary input",
        "reverses the logic state of the input",
        "inverter gate that flips high to low",
        "single input gate whose output negates the input",
        "gives low when input is high"
    ],
    "NAND": [
        "output is low only when both inputs are high",
        "produces 0 if and only if all inputs are 1",
        "inverted AND gate behavior",
        "output is high whenever at least one input is low",
        "gives 1 unless both A and B are 1",
        "negation of logical conjunction",
        "output drops to 0 only when all switches are closed",
        "high output if any input is 0"
    ],
    "NOR": [
        "output is high only when both inputs are low",
        "produces 1 if and only if all inputs are 0",
        "inverted OR gate behavior",
        "output is low whenever any input is high",
        "gives 0 if either A or B is 1",
        "negation of logical disjunction",
        "output turns on only when all switches are open",
        "low output if at least one input is 1"
    ],
    "XOR": [
        "output is high when inputs are different",
        "produces 1 only if the two inputs do not match",
        "output is low when both inputs are the same",
        "gives true if an odd number of inputs are true",
        "exclusive OR behavior where 1 and 1 gives 0",
        "high output if A and B have opposite logic levels",
        "detects inequality between two binary bits",
        "produces 0 when inputs are both 0 or both 1"
    ],
    "XNOR": [
        "output is high when both inputs are the same",
        "produces 1 only if the two inputs match",
        "output is low when inputs are different",
        "equivalence gate that outputs 1 for identical bits",
        "inverted XOR behavior where 1 and 1 gives 1",
        "high output if both A and B are 0 or both are 1",
        "detects equality between two binary inputs",
        "gives 0 when inputs have opposite states"
    ]
}

# Generate variations by adding slight phrasing prefixes/suffixes
prefixes = ["", "A circuit where ", "The gate where ", "In this logic, ", "System where "]
suffixes = ["", ".", " in the circuit", " for binary inputs", " at the output"]

data = []
for gate, phrases in templates.items():
    for _ in range(150):  # 150 samples per gate = 1050 total rows
        base = random.choice(phrases)
        sentence = f"{random.choice(prefixes)}{base}{random.choice(suffixes)}".strip()
        data.append({"description": sentence, "gate": gate})

df = pd.DataFrame(data)
df.to_csv("logic_gates_dataset.csv", index=False)
print(f"Dataset generated successfully with {len(df)} rows!")