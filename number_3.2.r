# Set seed for reproducibility
set.seed(0)

# Data for Normal Distribution
mean_normal <- 75
std_dev_normal <- 10
data_normal <- rnorm(1000, mean = mean_normal, sd = std_dev_normal)

# Data for Uniform Distribution
low_uniform <- 1
high_uniform <- 6
data_uniform <- sample(low_uniform:high_uniform, 1000, replace = TRUE)

# Data for Poisson Distribution
lambda_poisson <- 5
data_poisson <- rpois(1000, lambda = lambda_poisson)

# Plotting
par(mfrow = c(3, 1), mar = c(4, 4, 2, 1), oma = c(0, 0, 2, 0))

# Plot Normal Distribution
hist(data_normal, breaks = 30, col = 'skyblue', border = 'black',
     main = 'Distribusi Normal: Nilai Ujian Siswa', xlab = 'Nilai Ujian', ylab = 'Frekuensi')

# Plot Uniform Distribution
hist(data_uniform, breaks = seq(0.5, 6.5, by = 1), col = 'lightgreen', border = 'black',
     main = 'Distribusi Seragam: Pelemparan Dadu', xlab = 'Angka pada Dadu', ylab = 'Frekuensi', xaxt = 'n')
axis(1, at = 1:6)

# Plot Poisson Distribution
hist(data_poisson, breaks = 15, col = 'salmon', border = 'black',
     main = 'Distribusi Poisson: Jumlah Panggilan per Jam', xlab = 'Jumlah Panggilan', ylab = 'Frekuensi')

# Adjust layout
par(mfrow = c(1, 1), oma = c(0, 0, 0, 0))
