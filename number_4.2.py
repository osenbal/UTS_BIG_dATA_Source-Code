import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("cleaned_german_credit.csv")

# Encode Variabel Kategorikal: Karena SelectKBest hanya dapat bekerja dengan data numerik, variabel kategorikal perlu diubah menjadi bentuk numerik. Ini biasanya dilakukan dengan teknik seperti label encoding atau one-hot encoding.
# Encode categorical variables
le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
data['Housing'] = le.fit_transform(data['Housing'])
data['Saving accounts'] = le.fit_transform(data['Saving accounts'])
data['Checking account'] = le.fit_transform(data['Checking account'])
data['Purpose'] = le.fit_transform(data['Purpose'])

# Pemilihan Variabel Independen dan Variabel Target: Variabel independen (fitur) dipisahkan dari variabel target. Variabel independen adalah fitur-fitur yang akan digunakan untuk memprediksi variabel target.
# Selecting features
X = data.drop(columns=['Unnamed: 0', 'Purpose']) # Exclude non-predictive columns
y = data['Purpose']

# Inisialisasi Objek SelectKBest: Objek SelectKBest diinisialisasi dengan fungsi skor yang ingin digunakan untuk memilih fitur terbaik. Dalam contoh ini, fungsi skor yang digunakan adalah uji chi-squared.
# Feature selection
best_features = SelectKBest(score_func=chi2, k='all')

# Fit Objek SelectKBest ke Data: Objek SelectKBest difitkan ke data untuk menghitung skor setiap fitur.
fit = best_features.fit(X, y)\
# Summarize scores
feature_scores = pd.DataFrame(fit.scores_, index=X.columns, columns=['Score'])
feature_scores = feature_scores.sort_values(by='Score', ascending=False)

print("Data:  ")
print(data)
print()

# Pemilihan Fitur: Fitur-fitur dengan skor tertinggi dipilih sebagai fitur terbaik berdasarkan nilai K yang ditentukan sebelumnya.
# Penyimpulan Hasil: Hasil pemilihan fitur, berupa skor setiap fitur, disajikan dalam bentuk yang dapat diinterpretasikan untuk memahami hubungan antara fitur-fitur dan variabel target.
print("Feature scores:")
# Print scores
print(feature_scores)
