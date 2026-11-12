import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# data = np.array([[48], [50], [51], [49], [52], [47], [53], [50], [150], [-20]])

# model = IsolationForest(contamination=0.2, random_state=42)
# predictions = model.fit_predict(data)

# for x, y in zip(data.flatten(),predictions):
#     print(x,y,sep="\t:\t")

# df = pd.DataFrame({
#     "timestamp": pd.date_range("2026-01-01", periods=6, freq="h"),
#     "temp": [22.0, 22.5, np.nan, 23.0, 99.0, 22.8]
# })

# print(df)
# print("=" * 60)
# df["temp_clean"] = df["temp"].ffill()
# print(df)

df = pd.DataFrame({
    "timestamp": pd.date_range("2026-01-01", periods=3, freq="h", tz="UTC"),
    "value": [10, 12, 11]
})

print(df)

local_times = pd.to_datetime(["2026-01-01 15:30:00"]).tz_localize("Asia/Kolkata")
utc_times = local_times.tz_convert("UTC")

print(local_times)
print(utc_times)