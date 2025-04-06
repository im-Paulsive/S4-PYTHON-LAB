import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    "a": [4, 2, 4, 2, 2],
    "b": [8, 3, 7, 6, 4],
    "c": [5, 4, 4, 4, 3],
    "d": [7, 2, 7, 8, 3],
    "e": [6, 6, 8, 6, 2]
}

# Create DataFrame
index_labels = [2, 4, 6, 8, 10]
df = pd.DataFrame(data,index=index_labels)
print(df)
# Plot Bar Chart
df.plot(kind='bar',colormap='viridis')

# Customize Chart
plt.title("Bar Plot of Sample Data")
plt.xlabel("Index Values")
plt.ylabel("Values")
plt.legend(title="Columns")
plt.xticks(rotation=0)

# Show Plot
plt.show()
