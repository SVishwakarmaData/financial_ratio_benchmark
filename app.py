import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Financial Ratio Benchmarking Tool")

available_tickers = {
    "IDFC First Bank": "IDFCFIRSTB.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "Axis Bank": "AXISBANK.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "Kotak Mahindra Bank": "KOTAKBANK.NS",
}

selected = st.multiselect(
    "Choose banks to compare",
    options=list(available_tickers.keys()),
    default=["IDFC First Bank", "ICICI Bank", "Axis Bank"]
)

if len(selected) < 2:
    st.warning("Pick at least 2 banks to compare.")
else:
    tickers = [available_tickers[name] for name in selected]
    ratios_data = {}

    for t in tickers:
        stock = yf.Ticker(t)
        info = stock.info

        net_income = info.get('netIncomeToCommon')
        total_revenue = info.get('totalRevenue')
        roe = info.get('returnOnEquity')
        roa = info.get('returnOnAssets')
        debt_to_equity = info.get('debtToEquity')

        net_margin = (net_income / total_revenue) if net_income and total_revenue else None

        ratios_data[t] = {
            'ROE (%)': round(roe * 100, 2) if roe else None,
            'ROA (%)': round(roa * 100, 2) if roa else None,
            'Net Margin (%)': round(net_margin * 100, 2) if net_margin else None,
            'Debt/Equity': round(debt_to_equity, 2) if debt_to_equity else None,
        }

    df = pd.DataFrame(ratios_data).T
    st.subheader("Ratio Table")
    st.dataframe(df)

    st.subheader("Comparison Charts")
    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
    for ax, metric in zip(axes.flatten(), df.columns):
        df[metric].plot(kind='bar', ax=ax)
        ax.set_title(metric)
    plt.tight_layout()
    st.pyplot(fig)









