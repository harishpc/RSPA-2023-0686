import matplotlib.pyplot as plt

# Precision curve calculation
def calculate_precision_curve(y_true, y_pred):
  precision = []
  recall = []
  thresholds = sorted(y_pred, reverse=True)

  for threshold in thresholds:
    y_pred_binary = [1 if x >= threshold else 0 for x in y_pred]
    tp = sum([y_pred_binary[i] == y_true[i] and y_true[i] == 1 for i in range(len(y_pred_binary))])
    fp = sum([y_pred_binary[i] != y_true[i] and y_true[i] == 0 for i in range(len(y_pred_binary))])

    precision.append(tp / (tp + fp))
    recall.append(tp / sum(y_true))

  return precision, recall

# Load the test set data
# You can use the same test set data as above

# Calculate the precision curve
precision, recall = calculate_precision_curve(y_test, y_pred_test)

# Plot the precision curve
plt.plot(recall, precision, label="Precision curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision curve for ACTP framework result")
plt.legend()
plt.show()
