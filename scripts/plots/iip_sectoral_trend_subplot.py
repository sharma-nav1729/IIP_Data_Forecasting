import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# ---------------------- USER-DEFINED OUTPUT PATH ----------------------
user_path = input("Enter the full path to save the plot (e.g., /storage/emulated/0/Dissertation): ")
output_file = os.path.join(user_path, "Figure3_IIP_Subplots.png")

# ---------------------- DEFINE IIP DATA ----------------------
months = pd.date_range(start="2022-04", periods=31, freq='M')

data = {
    "Month": months,
    "Mining": [
        116.6, 120.4, 113.7, 101.1, 99.6, 100.0, 112.6, 122.7, 132.6, 136.1, 129.2, 154.2,
        122.6, 128.1, 122.3, 111.9, 111.9, 111.5, 127.4, 131.3, 139.5, 144.3, 139.7, 156.2,
        130.9, 136.5, 134.9, 116.1, 107.1, 111.7, 128.5
    ],
    "Manufacturing": [
        131.6, 134.6, 136.8, 135.0, 131.3, 134.6, 128.5, 137.5, 144.9, 145.5, 137.6, 147.5,
        138.8, 143.1, 141.6, 142.1, 144.4, 141.5, 142.1, 139.3, 151.6, 150.8, 144.4, 156.2,
        144.6, 150.4, 146.6, 148.8, 146.1, 147.2, 148.4
    ],
    "Electricity": [
        194.5, 199.9, 196.9, 188.9, 191.3, 187.4, 169.3, 166.7, 179.4, 186.6, 174.0, 188.0,
        192.3, 201.6, 205.2, 204.0, 220.5, 205.9, 203.8, 176.3, 181.6, 197.1, 187.2, 204.2,
        212.0, 229.3, 222.8, 220.2, 212.3, 206.9, 207.8
    ],
    "General": [
        134.5, 137.8, 138.3, 134.4, 131.5, 133.8, 129.5, 137.7, 145.9, 147.4, 139.3, 151.7,
        140.7, 145.6, 143.9, 142.7, 145.8, 142.3, 144.9, 141.1, 152.3, 153.6, 147.1, 160.0,
        148.0, 154.7, 151.0, 149.8, 145.8, 146.9, 150.3
    ]
}

df = pd.DataFrame(data)

# ---------------------- PLOT CONFIGURATION ----------------------
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (14, 10)

fig, axes = plt.subplots(4, 1, sharex=True)
sectors = ['Mining', 'Manufacturing', 'Electricity', 'General']
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

for i, sector in enumerate(sectors):
    sns.lineplot(ax=axes[i], x='Month', y=sector, data=df, color=colors[i])
    axes[i].set_title(f"{sector} Sector")
    axes[i].set_ylabel("IIP Value")
    axes[i].grid(True)

axes[-1].set_xlabel("Month")
plt.suptitle("Monthly IIP by Sector (Apr 2022 – Oct 2024)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ---------------------- SAVE FIGURE ----------------------
try:
    plt.savefig(output_file, dpi=300)
    print(f"Plot saved successfully at: {output_file}")
except Exception as e:
    print(f"Failed to save plot: {e}")
