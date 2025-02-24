import matplotlib.pyplot as plt
from collections import Counter

# Read the file and count character occurrences
with open("chara.txt", 'r') as f:
    text = f.read()

# Filter out spaces and count character frequencies
char_list = [char for char in text if char != " "]
char_freq = Counter(char_list)

# Expanding the dataset for histogram
expanded_data = []
for char, freq in char_freq.items():
    expanded_data.extend([char] * freq)  # Add the character 'freq' times

# Plot histogram
plt.hist(expanded_data, bins=len(char_freq), color='red', edgecolor='black', alpha=0.7)

# Labels and title
plt.title("Occurrence of Each Character")
plt.xlabel("Character")
plt.ylabel("Occurrence")

# Show plot
plt.show()
