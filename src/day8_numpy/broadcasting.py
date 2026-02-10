import numpy as np

# For reproducibility (optional)
np.random.seed(42)

# 1. Create a 5x3 array of random scores between 50 and 100
scores = np.random.randint(50, 101, size=(5, 3))

# 2. Calculate the mean score for each subject (column-wise mean)
subject_means = scores.mean(axis=0)

# 3. Subtract the mean from the original scores using broadcasting
centered_scores = scores - subject_means

# 4. Print results
print("Original Scores:")
print(scores)

print("\nSubject-wise Means:")
print(subject_means)

print("\nCentered Scores (after broadcasting):")
print(centered_scores)
