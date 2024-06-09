import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Read data from CSV files
file1_path = 'coordinates_FL_rightline2.csv'
file2_path = 'right_line2_dlio.csv'

data1 = pd.read_csv(file1_path)
data2 = pd.read_csv(file2_path)

# Assuming both CSV files have columns 'x' and 'y'
x1 = data1['x']
y1 = data1['y']

x2 = data2['x']
y2 = data2['y']

# Create the line plot
plt.figure(figsize=(5, 3))
# plt.scatter(x1, y1, label='FAST_LIO2 odometry', marker='o')
# plt.scatter(x2, y2, label='DLIO odometry', marker='x')
plt.plot(x1, y1, label='FAST_LIO2 odometry')
plt.plot(x2, y2, label='DLIO odometry')


plt.title('Odometry by FAST_LIO2 and DLIO')
plt.xlabel('X-axis (meters)')
plt.ylabel('Y-axis (meters)')
# plt.title('Odometry by FAST_LIO2 and DLIO')
# plt.xlabel('X-axis(meter)')
# plt.ylabel('Y-axis(meter)')
plt.legend()

plt.grid(True)
plt.axis('equal')

tick_spacing = 1.0  # Set the tick spacing in meters
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(base=tick_spacing))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=tick_spacing))

plt.show()
