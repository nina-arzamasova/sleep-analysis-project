import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- create synthetic dataset ---
np.random.seed(42)

days = pd.date_range(start="2024-01-01", periods=120)

sleep_hours = np.random.normal(7, 1, 120).round(1)
focus_score = (sleep_hours * 10 + np.random.normal(0, 5, 120)).round(1)
reaction_time = (300 - sleep_hours * 15 + np.random.normal(0, 10, 120)).round(1)

df = pd.DataFrame({
    "date": days,
    "sleep_hours": sleep_hours,
    "focus_score": focus_score,
    "reaction_time": reaction_time
})

# --- basic info ---
print(df.head())

# --- correlation ---
corr = df[["sleep_hours", "focus_score", "reaction_time"]].corr()
print("\nCorrelation matrix:\n", corr)

# --- plot 1: sleep vs focus ---
plt.figure()
plt.scatter(df["sleep_hours"], df["focus_score"])
plt.title("Sleep vs Focus")
plt.xlabel("Sleep (hours)")
plt.ylabel("Focus score")
plt.show()

# --- plot 2: sleep vs reaction time ---
plt.figure()
plt.scatter(df["sleep_hours"], df["reaction_time"])
plt.title("Sleep vs Reaction Time")
plt.xlabel("Sleep (hours)")
plt.ylabel("Reaction time (ms)")
plt.show()

# --- plot 3: sleep over time ---
plt.figure()
plt.plot(df["date"], df["sleep_hours"])
plt.title("Sleep over time")
plt.xticks(rotation=45)
plt.show()
