import numpy as np

arr = np.array(['add', 'sub', 'gt', 'lt'])

width = 15

# Centered
centered = np.array([s.center(width, '_') for s in arr])
print("Centered:\n", centered)

# Left-justified
left_justified = np.array([s.ljust(width, '_') for s in arr])
print("\nLeft-Justified:\n", left_justified)

# Right-justified
right_justified = np.array([s.rjust(width, '_') for s in arr])
print("\nRight-Justified:\n", right_justified)