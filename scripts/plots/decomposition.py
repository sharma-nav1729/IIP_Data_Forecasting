import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.dates as mdates

# Full monthly IIP data from Apr 2022 to Oct 2024
data = {
    'Month': [
        '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09',
        '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03',
        '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09',
        '2023-10', '2023-11', '2023-12', '2024-01', '2024-02', '2024-03',
        '2024-04', '2024-05', '2024-06', '2024-07', '2024-08', '2024-09',
        '2024-10'
    ],
    'Mining': [
        8.4, 10.2, 7.5, 6.6, 3.9, 11.5, 13.1, 7.0, 5.2, 6.0, 8.1, 1.3,
        6.8, 6.6, 10.3, 3.8, -4.3, 5.5, 6.0, 4.5, 5.1, 4.7, 6.1, 3.9,
        5.7, 6.3, 6.5, 3.4, 1.2, 2.8, 4.6
    ],
    'Manufacturing': [
        3.5, 6.2, 5.7, 4.1, 3.8, 5.1, 10.6, 1.3, 4.6, 3.6, 4.9, 5.9,
        4.2, 5.0, 3.2, 4.4, 1.0, 3.8, 4.5, 3.7, 4.0, 3.9, 4.6, 4.3,
        5.1, 4.8, 4.7, 3.6, 2.9, 3.5, 4.2
    ],
    'Electricity': [
        6.1, 8.7, 7.2, 5.5, 6.3, 9.9, 20.4, 5.8, 1.2, 5.6, 7.6, 8.6,
        10.2, 13.7, 8.6, 7.9, -3.7, 6.0, 5.8, 4.9, 5.2, 6.4, 7.0, 6.8,
        7.9, 8.3, 8.6, 5.5, 3.2, 4.7, 6.0
    ],
    'General': [
        4.2, 6.0, 5.1, 3.8, 4.5, 6.4, 11.9, 2.5, 4.4, 4.2, 5.6, 5.5,
        5.2, 6.2, 4.7, 4.7, -0.1, 4.1, 4.3, 3.9, 4.1, 4.3, 4.8, 4.2,
        5.0, 5.1, 5.3, 3.7, 2.5, 3.9, 4.6
    ]
}

# Create DataFrame
df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
df = df.asfreq('MS')

# Define sectors and colors
sectors = {
    'Mining': 'tab:blue',
    'Manufacturing': 'tab:orange',
    'Electricity': 'tab:green',
    'General': 'tab:red'
}

# Setup figure
fig, axes = plt.subplots(len(sectors), 4, figsize=(22, 18))
fig.subplots_adjust(hspace=0.6, wspace=0.3)
fig.suptitle("Seasonal Decomposition of IIP Sectors (Apr 2022 – Oct 2024)",
             fontsize=22, fontweight='bold')

# Date formatter and ticks
date_fmt = mdates.DateFormatter('%Y-%m')
xtick_locator = mdates.MonthLocator(bymonth=[4, 10])  # Every April & October

# Generate seasonal decomposition plots
for row_idx, (sector, color) in enumerate(sectors.items()):
    result = seasonal_decompose(df[sector], model='additive', period=12)
    components = [result.observed, result.trend, result.seasonal, result.resid]
    titles = ['Observed', 'Trend', 'Seasonal', 'Residual']

    for col_idx, comp in enumerate(components):
        ax = axes[row_idx, col_idx]
        comp.plot(ax=ax, color=color)
        ax.set_title(f"{sector} - {titles[col_idx]}", fontsize=12)
        ax.set_xlabel('')
        ax.xaxis.set_major_formatter(date_fmt)
        ax.xaxis.set_major_locator(xtick_locator)
        for label in ax.get_xticklabels():
            label.set_rotation(45)

# Save plot
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("Seasonal_Decomposition_All_Sectors_Cleaned.png", dpi=300)
print("Decomposition plot saved as 'Seasonal_Decomposition_All_Sectors_Cleaned.png'")
