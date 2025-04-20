import pandas as pd

# Given Series
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to Upper and Lower case
s_upper = s.str.upper()  # Convert to uppercase
s_lower = s.str.lower()  # Convert to lowercase

# Find Length of Strings (handling None values)
s_length = s.str.len()

# Display results
print("Original Series:\n", s)
print("\nUppercase:\n", s_upper)
print("\nLowercase:\n", s_lower)
print("\nString Length:\n", s_length)
# string serial 0 is one space ahead of all serials to indicate there are mixed datatypes because of None