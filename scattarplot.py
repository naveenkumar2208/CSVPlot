import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
file1_path = 'coordinates_FL_leftline1.csv'
file2_path = 'left_line_dlio.csv'

data1 = pd.read_csv(file1_path)
data2 = pd.read_csv(file2_path)

# Assuming both CSV files have columns 'x' and 'y'
x1 = data1['x']
y1 = data1['y']

x2 = data2['x']
y2 = data2['y']

# Create the line plot
plt.figure(figsize=(10, 6))

plt.scatter(x1, y1, label='Data from File 1', marker='o')
plt.scatter(x2, y2, label='Data from File 2', marker='x')

plt.title('Line Plot of Data from Two CSV Files')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.grid(True)
# plt.axis('equal')
plt.show()
