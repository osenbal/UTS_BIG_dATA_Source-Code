import pandas as pd
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("cleaned_german_credit.csv")

# 4. Eksplorasi Data: Sex, Duration, dan Purpose
sex_duration_purpose = data[['Sex', 'Duration', 'Purpose']]
sex_duration_purpose_grouped = sex_duration_purpose.groupby(['Sex', 'Purpose'])['Duration'].describe()
print("\nStatistik Durasi Kredit Berdasarkan Jenis Kelamin dan Tujuan Kredit:")
print(sex_duration_purpose_grouped)

# Plot
plt.figure(figsize=(12, 8))
sex_duration_purpose_grouped['mean'].unstack().plot(kind='bar')
plt.title('Rata-rata Durasi Kredit Berdasarkan Jenis Kelamin dan Tujuan Kredit')
plt.xlabel('Tujuan Kredit')
plt.ylabel('Rata-rata Durasi Kredit')
plt.xticks(rotation=45)
plt.legend(title='Jenis Kelamin')
plt.show()