import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load data from CSV
data = pd.read_csv("german_credit_data.csv")

# Display the first few rows of the dataset
print("Data German Credit:")
print(data.head())

# Calculate class probabilities
class_counts = data['Purpose'].value_counts()
class_probabilities = class_counts / len(data)

print("\nProbabilitas Kelas:")
print(class_probabilities)

# Separate features and target variable
X = data.drop(columns=['Purpose'])
y = data['Purpose']

# Function to calculate probabilities of categorical features for each class
def calculate_categorical_probabilities(feature, target):
    probabilities = {}
    for class_value in target.unique():
        class_data = feature[target == class_value]
        probabilities[class_value] = class_data.value_counts() / len(class_data)
    return probabilities

# Calculate probabilities of categorical features for each class
categorical_probabilities = {}
categorical_features = ['Sex', 'Housing', 'Saving accounts', 'Checking account']
for feature in categorical_features:
    categorical_probabilities[feature] = calculate_categorical_probabilities(X[feature], y)

# Print the calculated probabilities
for feature, probabilities in categorical_probabilities.items():
    print(f"\nProbabilitas Fitur '{feature}' pada Setiap Kelas:")
    for class_value, prob in probabilities.items():
        print(f"Kelas '{class_value}':")
        print(prob)

# Function to calculate mean and standard deviation of numerical features for each class
def calculate_numerical_parameters(feature, target):
    parameters = {}
    for class_value in target.unique():
        class_data = feature[target == class_value]
        parameters[class_value] = {
            'mean': np.mean(class_data),
            'std': np.std(class_data)
        }
    return parameters

# Calculate mean and standard deviation of numerical features for each class
numerical_parameters = {}
numerical_features = ['Age', 'Job', 'Credit amount', 'Duration']
for feature in numerical_features:
    numerical_parameters[feature] = calculate_numerical_parameters(X[feature], y)

def calculate_class_probabilities(instance):
    probabilities = {}
    for class_value in class_probabilities.index:
        probabilities[class_value] = class_probabilities[class_value]
        for feature in instance.index:
            if feature in categorical_features:
                if instance[feature] in categorical_probabilities[feature][class_value]:
                    probabilities[class_value] *= categorical_probabilities[feature][class_value][instance[feature]]
                else:
                    probabilities[class_value] *= 0.01  # Smoothing for unseen features
            elif feature in numerical_features:
                mean = numerical_parameters[feature][class_value]['mean']
                std = numerical_parameters[feature][class_value]['std']
                if std == 0:  # Handling std deviation zero
                    probabilities[class_value] *= 0
                else:
                    probabilities[class_value] *= (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((instance[feature] - mean) ** 2) / (2 * std ** 2))
    return probabilities

# Function to predict class for a given instance and return probabilities
def predict_with_probabilities(instance):
    probabilities = calculate_class_probabilities(instance)
    predicted_class = max(probabilities, key=probabilities.get)
    return predicted_class, probabilities

# Test data
test_data = pd.DataFrame({
    'Age': [22, 40, 50],
    'Sex': ['M', 'F', 'M'],
    'Job': [2, 3, 3],
    'Housing': ['Rent', 'Own', 'Own'],
    'Saving accounts': ['Little', 'Quite rich', 'Rich'],
    'Checking account': ['Little', 'Moderate', 'Rich'],
    'Credit amount': [15000, 7500, 1000],
    'Duration': [70, 35, 10]
})

# Predict classes for test data with probabilities
test_data['Predicted Purpose'], test_data['Probabilities'] = zip(*test_data.apply(predict_with_probabilities, axis=1))

print("\nHasil Prediksi:")
print(test_data[['Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration', 'Predicted Purpose', 'Probabilities']])
test_data.to_csv("hasil_prediksi_nomor_6.2_6.3.csv", index=False)
