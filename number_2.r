library(ggplot2)
library(dplyr)
library(scales)
library(gridExtra)

# Load data from CSV
df <- read.csv('ojek_online_data.csv')

# a. Pengemudi dengan total penghasilan terbesar selama 10 hari
max_income_driver <- df %>%
  group_by(Nama.Pengemudi) %>%
  summarise(Total.Penghasilan = sum(Total.Penghasilan)) %>%
  slice(which.max(Total.Penghasilan))

max_income <- max_income_driver$Total.Penghasilan
max_income_driver <- max_income_driver$Nama.Pengemudi

cat(paste("Pengemudi dengan total penghasilan terbesar: ", max_income_driver, " (Total Penghasilan: ", max_income, ")\n\n"))

# b. Pengemudi dengan total penghasilan terkecil selama 10 hari
min_income_driver <- df %>%
  group_by(Nama.Pengemudi) %>%
  summarise(Total.Penghasilan = sum(Total.Penghasilan)) %>%
  slice(which.min(Total.Penghasilan))

min_income <- min_income_driver$Total.Penghasilan
min_income_driver <- min_income_driver$Nama.Pengemudi

cat(paste("Pengemudi dengan total penghasilan terkecil: ", min_income_driver, " (Total Penghasilan: ", min_income, ")\n\n"))

# c. Rata-rata penghasilan setiap pengemudi ojek online selama 10 hari
average_income_per_driver <- df %>%
  group_by(Nama.Pengemudi) %>%
  summarise(Average.Penghasilan = mean(Total.Penghasilan))

average_all_driver <- mean(df$Total.Penghasilan)

cat("Rata-rata penghasilan semua pengemudi:\n")
cat(average_all_driver)
cat("\n\n")
cat("Rata-rata penghasilan setiap pengemudi:\n")
print(average_income_per_driver)
cat("\n")

# d. Visualisasi data time series untuk melihat fluktuasi total penghasilan pengemudi ojek online
# Konversi kolom 'Tanggal' menjadi tipe data Date
df$Tanggal <- as.Date(df$Tanggal, format="%d %b %Y")

library(gridExtra)

# Visualisasi data time series
plot_time_series <- ggplot(df, aes(x=Tanggal, y=`Total.Penghasilan`)) +
  geom_line() +
  labs(title="Fluktuasi Total Penghasilan Pengemudi Ojek Online", x="Tanggal", y="Total Penghasilan") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  scale_x_date(date_labels = "%d %b %Y") +
  scale_y_continuous(labels = comma)

# Visualisasi group bar
df_grouped <- df %>%
  group_by(Nama.Pengemudi) %>%
  summarise(Jumlah.Penghasilan = sum(Jumlah.Penghasilan),
            Jumlah.Bonus = sum(Jumlah.Bonus),
            Total.Penghasilan = sum(`Total.Penghasilan`))


plot_group_bar <- ggplot(df_grouped, aes(x=Nama.Pengemudi)) +
  geom_bar(aes(fill="Total Penghasilan", y=`Total.Penghasilan`), stat="identity", position="dodge") +
  geom_bar(aes(fill="Jumlah Penghasilan", y=`Jumlah.Penghasilan`), stat="identity", position="dodge") +
  geom_bar(aes(fill="Jumlah Bonus", y=`Jumlah.Bonus`), stat="identity", position="dodge") +
  labs(title="Jumlah Penghasilan, Jumlah Bonus, dan Total Penghasilan Setiap Pengemudi Ojek Online", x="Pengemudi", y="Jumlah") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  scale_fill_manual(name="Variabel", values=c("Jumlah Penghasilan"="blue", "Jumlah Bonus"="green", "Total Penghasilan"="red")) +
  scale_y_continuous(labels = comma)

# Print kedua grafik dalam satu jendela
grid.arrange(plot_time_series, plot_group_bar, ncol=1)
