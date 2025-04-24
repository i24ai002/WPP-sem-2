import numpy as np

while True:
    N = int(input("Enter the number of points (N >= 10): "))
    if N >= 10:
        break
    print("Please enter a number greater than or equal to 10.")

# Generate N random 2D Cartesian points
points = np.random.rand(N, 2)
print("Cartesian Points:\n", points)

# Extract x and y
x = points[:, 0]
y = points[:, 1]

# Convert to polar coordinates
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
polar = np.column_stack((r, theta))

print("Polar Coordinates:\n", polar)
