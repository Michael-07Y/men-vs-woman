# File Information
# Version: 0.50.01 (Pre-Beta)
# Creator: Michael Yurachek
# Last updated: 05 / 30 / 2024

import os
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
df = pd.read_csv('./assets/csv/gpaAverage.csv')

# Convert 'Year' column to integers
df['Year'] = df['Year'].astype(int)

# Extract data
yr = df['Year']
mHSgpa = df['Avg High School GPA (Male)']
fHSgpa = df['Avg High School GPA (Female)']

# Plotting
plt.figure(figsize=(10,6))

# Plot male high school GPA with blue color and solid line
plt.plot(yr, mHSgpa, color='blue', linestyle='-', linewidth=2, label='Male High School GPA')

# Plot female high school GPA with hotpink color and dashed line
plt.plot(yr, fHSgpa, color='hotpink', linestyle='--', linewidth=2, label='Female High School GPA')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Average High School GPA')
plt.title('Average High School GPA by Gender Over Years')

# Add legend
plt.legend()

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust x-axis ticks
plt.xticks(yr, rotation=45)  # Rotate x-axis labels for better readability

# Save plot image
strFile = "./assets/images/graphs/genderHighGPAGraph.png"
if os.path.isfile(strFile):
    os.remove(strFile)   # Remove the existing file if it exists
plt.savefig(strFile)

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

os.system('cls||clear')