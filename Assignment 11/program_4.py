import pandas as pd

# Taking user input for John and Judy's schedule
john_schedule = []
judy_schedule = []

print("Enter '1' if John is visiting, '0' otherwise:")
for i in range(1, 11):
    john_schedule.append(int(input(f"Day {i} - John visiting? (1/0): ")))

print("\nEnter '1' if Judy is visiting, '0' otherwise:")
for i in range(1, 11):
    judy_schedule.append(int(input(f"Day {i} - Judy visiting? (1/0): ")))

# Create DataFrame
df = pd.DataFrame({
    "day": range(1, 11),
    "John": john_schedule,
    "Judy": judy_schedule
})

# Identify party days (when both John and Judy visit)
df["party"] = df["John"] & df["Judy"]

# Compute 'days_til_party'
df["days_til_party"] = (df.index.to_series()
                        .apply(lambda i: (df.loc[i:, "party"].idxmax() - i) if df.loc[i:, "party"].any() else None))

# Display the result
print("\nFinal Schedule with Days Until Next Party:")
print(df[["day", "John", "Judy", "days_til_party"]])
