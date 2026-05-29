import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------
# USE ABSOLUTE CSV PATH
# ---------------------------------------
csv_path = r"D:\DualMind AI\evaluation_results.csv"

# ---------------------------------------
# CHECK FILE EXISTS
# ---------------------------------------
if not os.path.exists(csv_path):

    print("CSV FILE NOT FOUND")
    print("Expected path:", csv_path)

    exit()

# ---------------------------------------
# LOAD CSV
# ---------------------------------------
df = pd.read_csv(csv_path)

print("CSV loaded successfully.")

# ---------------------------------------
# CREATE OUTPUT FOLDER
# ---------------------------------------
charts_dir = r"D:\DualMind AI\reports\charts"

os.makedirs(charts_dir, exist_ok=True)

# ---------------------------------------
# LATENCY CHART
# ---------------------------------------
latency_data = df.groupby("model")["latency_sec"].mean()

plt.figure(figsize=(6, 4))

latency_data.plot(kind="bar")

plt.title("Average Latency Comparison")

plt.ylabel("Seconds")

plt.tight_layout()

plt.savefig(
    os.path.join(charts_dir, "latency_chart.png")
)

plt.close()

# ---------------------------------------
# SAFETY CHART
# ---------------------------------------
safety_counts = df.groupby(
    ["model", "safety"]
).size().unstack(fill_value=0)

plt.figure(figsize=(6, 4))

safety_counts.plot(kind="bar")

plt.title("Safety Comparison")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(charts_dir, "safety_chart.png")
)

plt.close()

# ---------------------------------------
# HALLUCINATION CHART
# ---------------------------------------
hallucination_counts = df.groupby(
    ["model", "hallucination"]
).size().unstack(fill_value=0)

plt.figure(figsize=(6, 4))

hallucination_counts.plot(kind="bar")

plt.title("Hallucination Comparison")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(charts_dir, "hallucination_chart.png")
)

plt.close()

print("\nCharts generated successfully.")
print("Saved inside:")
print(charts_dir)