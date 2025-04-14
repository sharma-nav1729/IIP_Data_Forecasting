import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Prompt user for custom output path
user_path = input("Enter the full output path to save the figure (or press Enter to use default): ").strip()

# Set default path if nothing entered
if not user_path:
    user_path = os.path.join(os.getcwd(), "Figure_1_IIP_Time_Series.png")

# Create date range from April 2022 to October 2024 (31 months)
dates = pd.date_range(start="2022-04", periods=31, freq="M")

# IIP sector-wise data
data = {
    "Mining": [
        116.6, 120.4, 113.7, 101.1, 99.6, 100.0, 112.6, 122.7, 132.6, 136.1, 129.2,
        154.2, 122.6, 128.1, 122.3, 111.9, 111.9, 111.5, 127.4, 131.3, 139.5, 144.3,
        139.7, 156.2, 130.9, 136.5, 134.9, 116.1, 107.1, 111.7, 128.5
    ],
    "Manufacturing": [
        131.6, 134.6, 136.8, 135.0, 131.3, 134.6, 128.5, 137.5, 144.9, 145.5, 137.6,
        147.5, 138.8, 143.1, 141.6, 142.1, 144.4, 141.5, 142.1, 139.3, 151.6, 150.8,
        144.4, 156.2, 144.6, 150.4, 146.6, 148.8, 146.1, 147.2, 148.4
    ],
    "Electricity": [
        194.5, 199.9, 196.9, 188.9, 191.3, 187.4, 169.3, 166.7, 179.4, 186.6, 174.0,
        188.0, 192.3, 201.6, 205.2, 204.0, 220.5, 205.9, 203.8, 176.3, 181.6, 197.1,
        187.2, 204.2, 212.0, 229.3, 222.8, 220.2, 212.3, 206.9, 207.8
    ],
    "General": [
        134.5, 137.8, 138.3, 134.4, 131.5, 133.8, 129.5, 137.7, 145.9, 147.4, 139.3,
        151.7, 140.7, 145.6, 143.9, 142.7, 145.8, 142.3, 144.9, 141.1, 152.3, 153.6,
        147.1, 160.0, 148.0, 154.7, 151.0, 149.8, 145.8, 146.9, 150.3
    ]
}

# Create DataFrame
df = pd.DataFrame(data, index=dates)

# Set color palette
sector_colors = {
    'Mining': '#1f77b4',
    'Manufacturing': '#ff7f0e',
    'Electricity': '#2ca02c',
    'General': '#d62728'
}

# Apply seaborn styling
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Plotting
fig, ax = plt.subplots()
for sector in df.columns:
    ax.plot(df.index, df[sector], label=sector, color=sector_colors[sector], linewidth=2)

plt.title("IIP Trends Over Time (Apr 2022 - Oct 2024)", fontsize=14)
plt.xlabel("Month")
plt.ylabel("IIP Index")
plt.xticks(rotation=45)
plt.legend(title="Sector", loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(user_path), exist_ok=True)

# Save plot
plt.savefig(user_path, dpi=300)
print(f"Plot successfully saved at: {user_path}")
