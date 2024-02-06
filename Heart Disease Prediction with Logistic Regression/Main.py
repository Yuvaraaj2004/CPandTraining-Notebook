import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn import __version__ as sklearn_version

# Load the dataset
#Fill your code here

# Extracting features and target
#Fill your code here

# Feature scaling
#Fill your code here

# Implement Logistic Regression
#Fill your code here

# Validation approaches
#Validation set approach
#Fill your code here

# K-fold cross validation(use cv=5, scoring='accuracy')
#Fill your code here

#Stratified K-fold cross validation(n_splits=5, shuffle=True, random_state=42)
#Fill your code here

#LOO strategy
#Fill your code here

# c. Plot Confusion Matrix
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig("ConfusionMatrix.png")

# d. Report performance metrics with two decimal points
#Fill your code here

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
