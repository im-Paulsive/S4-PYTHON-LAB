# Class intervals and frequencies
classes = [(0,10), (10,20), (20,30), (30,40), (40,50), (50,60), (60,70), (70,80)]
frequencies = [5, 10, 20, 40, 30, 20, 10, 5]

# Step 1: Calculate midpoints of each class
midpoints = [(start + end) / 2 for start, end in classes]

# Step 2: Calculate total frequency and mean
N = sum(frequencies)
fx = [f * x for f, x in zip(frequencies, midpoints)]
mean = sum(fx) / N

# Step 3: Calculate variance and standard deviation
fx2 = [f * (x - mean)**2 for f, x in zip(frequencies, midpoints)]
variance = sum(fx2) / N
std_dev = variance ** 0.5

# Step 4: Calculate mean deviation
f_abs_dev = [f * abs(x - mean) for f, x in zip(frequencies, midpoints)]
mean_dev = sum(f_abs_dev) / N

# Step 5: Range = highest - lowest class midpoint
range_val = max(midpoints) - min(midpoints)

# Output
print(f"Mean: {mean:.2f}")
print(f"Mean Deviation: {mean_dev:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Range: {range_val}")
