import pandas as pd

# Sample dataset
data = {
    "artist": ["A", "B", "A", "C", "B", "A", "C", "A", "B"],
    "venue": ["X", "Y", "X", "Z", "Y", "X", "Z", "Y", "X"],
    "date": ["2024-01-15", "2024-01-22", "2024-02-10", "2024-02-18",
             "2024-03-05", "2024-03-15", "2024-04-10", "2024-04-15", "2024-04-20"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'date' column to datetime and extract 'year-month'
df["date"] = pd.to_datetime(df["date"])
df["year_month"] = df["date"].dt.to_period("M")

# Count concerts per (artist, venue, year-month)
concert_counts = df.groupby(["year_month", "artist", "venue"]).size().reset_index(name="count")

# Pivot table to wide format
wide_table = concert_counts.pivot(index="year_month", columns=["artist", "venue"], values="count").fillna(0)

# Flatten column names
wide_table.columns = [f"{a}_{v}" for a, v in wide_table.columns]
wide_table.reset_index(inplace=True)

# Print result
print(wide_table)
