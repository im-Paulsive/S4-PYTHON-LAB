import matplotlib.pyplot as plt
import numpy as np

#  Convert dictionary to lists
programs = ["java", "python", "c", "Rust", "R"]
popularity = [93, 99, 87, 92, 94]

#  Convert lists to NumPy arrays
programs_np = np.array(programs)
popularity_np = np.array(popularity)

#  Sort by popularity (ascending order)
sorted_indices = np.argsort(popularity_np)  # Sort in ascending order

# Apply sorting to both arrays
programs_sorted = programs_np[sorted_indices]
popularity_sorted = popularity_np[sorted_indices]

# Define colors
colors = ['green', 'red', 'orange', 'yellow', 'blue']

# Step 4: Create bar chart
plt.bar(programs_sorted, popularity_sorted, color=colors)

# Labels and formatting
plt.ylabel("Popularity")
plt.xlabel("Programming Language")
plt.xticks(rotation=45)
plt.title("Popularity of Programming Languages (Ascending Order)")


# Show plot
plt.show()
