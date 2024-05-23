import pandas as pd
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("cleaned_german_credit.csv")

# 3. Eksplorasi Data: Saving Account dan Sex
saving_account_sex = data[['Saving accounts', 'Sex']]
saving_account_sex_grouped = saving_account_sex.groupby('Sex')['Saving accounts'].value_counts(normalize=True)
print("Distribusi Tabungan Berdasarkan Jenis Kelamin:")
print(saving_account_sex_grouped)

# Plot
plt.figure(figsize=(10, 6))
saving_account_sex_grouped.unstack().plot(kind='bar')
plt.title('Distribusi Tabungan Berdasarkan Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Proporsi')
plt.xticks(rotation=0)
plt.legend(title='Tabungan')
plt.show()
