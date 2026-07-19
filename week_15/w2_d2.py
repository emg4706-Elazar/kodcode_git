import pandas as pd
from pandas.core.interchange.column import PandasColumn

# Step 2
speeds = [412, 95, 250, 510]
names = ["Elazar", "yosef", "David", "Yaakov"]
series = pd.Series(speeds, index=names)
# print(series["Elazar"])

# Step 3
dicti = data = {
    "id": [1, 2, 3, 4],
    "speed": [95, 120, 75, 110],
    "heading": [30, 90, 180, 270]
}

df = pd.DataFrame(dicti)
df = df.set_index("id")
# print(df.loc[1])


# Step 4
df["speed_kmh"] = df["speed"] * 1.609
# print(df)










