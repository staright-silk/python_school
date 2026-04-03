import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt 

n = int(input("Enter number of datasets: "))

results = []
actual_labels = []
predicted_labels = []

for i in range(n):
    print(f"\nDataset {i+1}")
    
    name = input("Enter dataset name: ")
    total = int(input("Total number of samples: "))
    correct = int(input("Number of correctly predicted samples: "))
    
    
    actual = ["Dog"] * total
    predicted = ["Dog"] * correct + ["Not Dog"] * (total - correct)
    
    actual_labels.extend(actual)
    predicted_labels.extend(predicted)
    
    tp = correct
    fn = total - correct
    
    fp = sum([r["total"] for r in results]) - sum([r["correct"] for r in results]) if results else 0
    tn = sum([r["correct"] for r in results]) if results else 0

    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    recall = tp / (tp + fn) if (tp + fn) != 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    results.append({
        "name": name,
        "total": total,
        "correct": correct,
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

print("\nRESULTS")
for r in results:
    print(f"\nDataset: {r['name']}")
    print(f"tp: {r['tp']}, fp: {r['fp']}, fn: {r['fn']}, tn: {r['tn']}")
    print(f"Precision: {r['precision']}")
    print(f"Recall: {r['recall']}")
    print(f"F1 Score: {r['f1']}")

total_correct = sum(r["correct"] for r in results)
total_samples = sum(r["total"] for r in results)

accuracy = total_correct / total_samples if total_samples != 0 else 0
print("\nAccuracy:", accuracy)
cm = confusion_matrix(actual_labels, predicted_labels, labels=["Dog", "Not Dog"])

sns.heatmap(cm, annot=True, fmt='d', xticklabels=["Dog", "Not Dog"], yticklabels=["Dog", "Not Dog"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()