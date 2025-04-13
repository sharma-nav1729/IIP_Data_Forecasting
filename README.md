# IIP Data Forecasting Project

This repository contains time series analysis and forecasting models for the **Index of Industrial Production (IIP)** data across various sectors such as Mining, Manufacturing, Electricity, and General Index over 31 months.

The objective is to explore, analyze, and forecast the IIP using classical and advanced statistical methods.

---

## Project Structure

<pre>
```bash
IIP_Data_Forecasting/
│
├── data/                         
│   └── IIP_Data.csv                  # Raw IIP data
│
├── notebooks/                       
│   ├── 1_exploratory_analysis.ipynb        # Visualizations & trend analysis
│   ├── 2_exponential_smoothing.ipynb       # Holt-Winters method
│   ├── 3_SARIMA_modeling.ipynb             # Seasonal ARIMA modeling
│   ├── 4_prophet_modeling.ipynb            # Prophet (optional)
│   └── 5_comparison_of_models.ipynb        # Compare accuracy of methods
│
├── results/                        
│   ├── plots           # Forecast plots
│   └── tables
│
├── scripts/                        
│   ├── modeling
│   └── evaluation
│
├── README.md                         
└── requirements.txt                  # Project dependencies
```
</pre>                  # Project dependencies

---

## Objectives

- Visualize and understand patterns, trends, and seasonality in IIP data  
- Apply exponential smoothing methods (Holt-Winters)  
- Build and evaluate SARIMA models  
- (Optional) Use Prophet for forecasting  
- Compare performance using metrics like RMSE and MAPE  

---

## How to Use

1. **Clone the repository:**

```bash
git clone https://github.com/sharma-nav1729/IIP_Data_Forecasting.git
```
2. Run notebooks in Google Colab:



Upload .ipynb files

- Mount Google Drive if needed

- Execute each cell step-by-step


3. Save results to appropriate folders:



Forecast plots → plots/results/

Output data (optional) → data/



---

Installation

Install the required Python libraries using:

pip install -r requirements.txt

If you’re using Prophet (optional):

pip install prophet


---

Author

Navdeep Sharma
M.Sc. Statistics
Project Guide: Dr. Lakhan Singh. 
Institute: H.N.B. Garhwal University


---

License

This project is intended for academic and research use only.
