# ==============================================================================
# CENTRAL LIMIT THEOREM (CLT) IN A NUTSHELL
# ==============================================================================
# 1. The Input: Start with ANY population shape (skewed, uniform, chaotic).
# 2. The Action: Take repeated random samples of size n (where n >= 30) 
#               and calculate the mean (average) of each sample.
# 3. The Result: The distribution of these sample means will ALWAYS form 
#               a Normal Distribution (Bell Curve).
# ==============================================================================
'''
In plain English, the Central Limit Theorem states: 
If you take enough random samples from any weird, lopsided, non-normal population, 
the distribution of their averages will always form a neat, symmetrical Bell Curve (Normal Distribution).
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# 1. Create a heavily skewed non-normal population (Exponential Distribution)
population = np.random.exponential(scale=2.0, size=10000)

# 2. Simulate taking 1,000 random samples (each of size n = 30)
sample_size = 30
num_samples = 1000
sample_means = []

for _ in range(num_samples):
    # Draw a random sample of size 30 from our skewed population
    sample = np.random.choice(population, size=sample_size)
    # Calculate and store the average of this sample
    sample_means.append(np.mean(sample))

# 3. Store the sample means in a Pandas DataFrame
df_means = pd.DataFrame({'Sample_Mean': sample_means})
# print(df_means)

# 4. Plotting the before and after comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot A: The chaotic original population
axes[0].hist(population, bins=50, color='skyblue', edgecolor='black', density=True)
axes[0].set_title("1. Original Population (Exponential / Skewed)")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Density")

# Plot B: The sample means forming a Bell Curve
axes[1].hist(df_means['Sample_Mean'], bins=30, color='salmon', edgecolor='black', density=True)
axes[1].set_title(f"2. Distribution of Sample Means (n = {sample_size})\n(The Bell Curve Appears!)")
axes[1].set_xlabel("Sample Mean")
axes[1].set_ylabel("Density")

plt.tight_layout()
plt.show()

# Quick look at the DataFrame
print("First 5 rows of our Sample Means DataFrame:")
print(df_means.head())
