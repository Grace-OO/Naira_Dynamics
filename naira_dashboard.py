
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib import style

st.set_page_config(page_title="🔁 Naira Dynamics: Oil, Inflation And Exchange", layout="centered")

st.title("🔁 Naira Dynamics: Oil, Inflation And Exchange")
st.write('This project analyzes the historical performance (between 2009 to 2024) of the Nigerian Naira (NGN) against six major global currencies, focusing on **exchange rate trends**, **volatility**, and the **influence of crude oil prices and inflation**.')
st.write("""
    This analysis is of value to professional in these spaces:
    * Financial Services & Banking – for FX risk assessment, investment strategy, and economic forecasting
    * Import/Export & Trade – to understand currency exposure and pricing strategy
    * Government & Policy Institutions – for macroeconomic planning and inflation control
    * Oil & Gas – to assess exchange rate risk independent of oil price trends
    * Investment & Asset Management – for currency market analysis and portfolio allocation
    """)

st.markdown("[Click here to explore the project code on GitHub.](https://github.com/Grace-OO/Call_Metrics/tree/main)")
# Load dataset (assumes the file is preloaded, not uploaded)
df = pd.read_csv("naira.csv", parse_dates=['date'])

# Sidebar filters
st.sidebar.header("Filter Data")
years = list(range(2009, 2025))
year_range = st.sidebar.slider("Select Year Range", 2009, 2024, (2009, 2024))
selected_currencies = st.sidebar.multiselect("Select Currencies", df['currency'].unique(), default=list(df['currency'].unique()))

# Filter data
df = df[df['year'].between(year_range[0], year_range[1]) & df['currency'].isin(selected_currencies)]

# Pivot exchange rate data
df_pivot = df.pivot(index='date', columns='currency', values='central_rate')
df_meta = df[['date', 'crude_oil_price', 'inflation_rate']].drop_duplicates().set_index('date')
df_merged = df_pivot.merge(df_meta, left_index=True, right_index=True)

# Sidebar selection

show_chart1 = st.sidebar.checkbox("NGN Exchange Rates Over Time", value=True)
show_chart2 = st.sidebar.checkbox("Volatility of Exchange Rates", value=True)
show_chart3 = st.sidebar.checkbox("Rolling Volatility of Exchange Rates)", value=True)
show_chart4 = st.sidebar.checkbox("Correlation Matrix: Currencies vs Oil/Inflation", value=True)


# Visualization 1: Exchange Rate Trends
if show_chart1:
    st.subheader("NGN Exchange Rates Over Time")
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in df_pivot.columns:
        ax.plot(df_pivot.index, df_pivot[col], label=col)
    ax.set_title('NGN vs Major Currencies')
    ax.set_ylabel('Exchange Rate')
    ax.set_xlabel('Date')
    ax.legend()
    ax.grid(True)
    ax.xaxis.set_major_locator(mdates.YearLocator())  # Show tick for each year
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Show only the year
    st.pyplot(fig)
    st.write("""
   Between 2009 and 2024, the Nigerian Naira experienced a long-term downward trend in value, marked by periods of relative stability. 
   The lowest valuation occurred in mid-year to the final quarter of 2024, followed by signs of recovery at the end of the year, indicating a potential shift in market dynamics or policy response.
    """)

# Visualization 2: Box Plot
if show_chart2:
    st.subheader("Volatility of Exchange Rates")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='currency', y='central_rate', ax=ax)
    ax.set_title("Box Plot of NGN Exchange Rates")
    st.pyplot(fig)
    st.write("""
    Between 2009 and 2024, Western currencies—particularly the USD, GBP, and EUR—exhibited higher volatility and a greater degree of Naira depreciation over time. 
    In contrast, Asian currencies such as the JPY and CNY, along with the South African Rand, demonstrated more stability, characterized by narrower interquartile ranges and fewer extreme fluctuations.
    """)

# Visualization 3: Rolling Volatility
if show_chart3:
    st.subheader("Rolling Volatility of Exchange Rates")
    rolling_vol = df_pivot.rolling(6).std()
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in rolling_vol.columns:
        ax.plot(rolling_vol.index, rolling_vol[col], label=col)
    ax.set_title("6-Month Rolling Std Dev")
    ax.legend()
    ax.set_ylabel("Std Dev")
    ax.xaxis.set_major_locator(mdates.YearLocator())  # Show tick for each year
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Show only the year
    plt.xticks(rotation=30)
    st.pyplot(fig)
    st.write("""
   From 2009 to 2024, the Naira saw major devaluations in 2015 followed by a more pronounced depreciation in 2016. This is followed by relative stability until 2020. 
   In 2023, volatility surged again, exceeding 2016 levels, with peaks in mid-2024. By year-end, the Naira showed signs of recovery.

    """)

# Visualization 4: Correlation Matrix
if show_chart4:
    st.subheader("Correlation Matrix: Currencies vs Oil/Inflation")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df_merged.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)
    st.write("""
    The correlation matrix reveals that crude oil prices have little to no correlation with the exchange rates of the analyzed currencies. 
    In contrast, the year-on-year inflation rate exhibits a strong positive correlation with these exchange rates, indicating inflation’s significant influence on currency valuation. 
    Additionally, the currencies generally tend to move together, demonstrating strong inter-correlations among themselves.
    """)
    
st.write("#### Summary")
st.write("""
   From 2009 to 2024, the Nigerian Naira faced ongoing depreciation, with major devaluation trends beginning in 2023 and culminating in the worst decline in 2024. 
   * Western currencies showed higher volatility compared to more stable Asian and African currencies. 
   * Inflation was strongly correlated with exchange rate changes, while crude oil prices had minimal impact. 
   * Currencies generally moved together, reflecting common economic influences.
    """)

with st.expander("📄 View Filtered Data"):
    st.dataframe(df)
