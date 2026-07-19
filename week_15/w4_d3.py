import pandas as pd

# Step 1
data = {
    "speed": [95, 120, None, 110],
    "altitude": [1000, 1500, 800, 1250],
    "longitude": [121, 414, 666, 564]
}

df = pd.DataFrame(data)
# print(df)

# Step 2
# print(df.describe())

# Step 3
mean_of_speed = df["speed"].mean()
median_of_alt = df["altitude"].median()
max_of_long = df["longitude"].max()
min_of_long = df["longitude"].min()
count = df["speed"].count()

print(df["altitude"].std())




