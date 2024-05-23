import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score, f1_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv("german_credit_data.csv")

# Ganti nilai NA dengan nilai yang paling sering muncul untuk kolom Saving accounts dan Checking account
data['Saving accounts'].fillna(data['Saving accounts'].mode()[0], inplace=True)
data['Checking account'].fillna(data['Checking account'].mode()[0], inplace=True)

# Encoding categorical features
label_encoders = {}
for column in ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column].astype(str))
    label_encoders[column] = le

# Tampilkan beberapa baris pertama untuk memastikan encoding telah dilakukan dengan benar
print(data.head())

# Definisikan fitur dan target
X = data.drop(columns=['Purpose'])  # Fitur adalah semua kolom kecuali 'Purpose'
y = data['Purpose']  # Target adalah kolom 'Purpose'

# 5.3. Lakukan implementasi C45 secara komputasi dengan dataset german credit. Jika
# ukuran pohonya terlalu besar dapat menerapkan teknik pruning untuk memangkas
# pohon menjadi lebih sederhana.

# Bagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bangun pohon keputusan
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)  # Set max_depth untuk pruning
clf.fit(X_train, y_train)

# Visualisasikan pohon keputusan
tree_rules = export_text(clf, feature_names=list(X.columns))
print(tree_rules)

# 5.4. Berapa nilai akurasi, presisi dan recall dari implementasi C45 German Credit.
# Prediksi pada set pengujian
y_pred = clf.predict(X_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Precision, Recall, Accuracy, dan F1 Score dengan zero_division
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

print()
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1:.2f}")

# Classification Report
# class_report = classification_report(y_test, y_pred, target_names=label_encoders['Purpose'].classes_)
# print("Classification Report:")
# print(class_report)

# Plot the decision tree
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=label_encoders['Purpose'].classes_, filled=True)
plt.show()
