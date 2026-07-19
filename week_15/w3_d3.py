import pandas as pd

# Step 1
data = {
    "id": [1, 2, 2, 3],
    "speed": ["95", "120", "120", "80"],
    "heading": [30, 90, 90, 180],
    "date": ["2026-07-15", "2026-07-16", "2026-07-16", "2026-07-17"],
    "notes": ["ok", "check", "check", "ok"]
}

df = pd.DataFrame(data)
# print(df)
# print()

# Step 2
del df["notes"]

df = df.drop_duplicates()
# print(df)

# Step 3
# print(df.dtypes)
df["speed"] = pd.to_numeric(df["speed"]).mean()
# print()
# print(df.dtypes)

# Step 4
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
# print(df)

monthly_average = df.groupby(df.index.date)["speed"].mean()

print(monthly_average)







