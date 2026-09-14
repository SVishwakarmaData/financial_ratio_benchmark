# Financial Ratio Benchmarking Tool

Compares ROE, ROA, Net Margin, and Debt/Equity across 3 private
banks. Includes a static notebook version and an interactive
Streamlit app with a bank picker.

**Tech:** Python, yfinance, pandas, matplotlib, Streamlit

**Why ROA instead of Current Ratio:** Current Ratio isn't
meaningful for banks — their balance sheets don't work like a
regular company's. ROA is the correct substitute.

**Run the notebook:**
```
pip install yfinance pandas matplotlib
jupyter notebook financial_ratio_benchmark.ipynb
```

**Run the interactive app:**
```
pip install streamlit yfinance pandas matplotlib
streamlit run app.py
```

![chart](
