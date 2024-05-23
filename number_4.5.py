import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder

# Membaca data
data = pd.read_csv("cleaned_german_credit.csv")

# Encode variabel kategorikal
le = LabelEncoder()
categorical_columns = ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose']
for column in categorical_columns:
    data[column] = le.fit_transform(data[column])

# Pisahkan fitur dan target
X = data.drop(columns=['Unnamed: 0', 'Purpose'])  # Exclude non-predictive columns
y = data['Purpose']

# Inisialisasi StratifiedKFold dengan K=10
k = 10
skf = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)

# Iterasi dan pembagian data
for fold, (train_index, test_index) in enumerate(skf.split(X, y)):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    print(f"Fold {fold + 1}")
    print(f"Data Latih: {len(X_train)} sampel")
    print(f"Data Uji: {len(X_test)} sampel")
    print("-" * 30)
    # Jika ingin menampilkan data latih dan uji
    print("Data Latih:")
    print(X_train.head())
    print(y_train.head())
    print("Data Uji:")
    print(X_test.head())
    print(y_test.head())
    print("=" * 50)

# Note: X dan y di sini adalah placeholder. Sesuaikan dengan nama kolom dalam DataFrame df.
