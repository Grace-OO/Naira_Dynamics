# 🔁 Naira Dynamics: Oil, Inflation And Exchange
This project analyzes the historical performance (between 2009 to 2024) of the Nigerian Naira (NGN) against six major global currencies, focusing on exchange rate trends, volatility, and the influence of crude oil prices and inflation.

## 📌 Project Objective

> To explore how NGN exchange rates have changed over time and identify the impact of crude oil prices and inflation on the Naira’s performance against six foreign currencies.

---
##### [View streamlit data story here](https://nairadynamics.streamlit.app/)

## 📁 Dataset Description

| Column Name        | Description                                  |
|--------------------|----------------------------------------------|
| `date`             | Monthly timestamp                            |
| `currency`         | Foreign currency code (e.g., USD, GBP, EUR)  |
| `central_rate`     | Central Bank exchange rate (NGN per unit)    |
| `crude_oil_price`  | Monthly average global oil price (USD/barrel)|
| `inflation_rate`   | Nigerian monthly inflation rate (%)          |

### Dataset Source
* [Inflation rate data ](https://www.cbn.gov.ng/rates/inflrates.html)
* [Crude oil price data](https://www.cbn.gov.ng/rates/crudeoil.html)
* [NGN Exchange rate data](https://www.cbn.gov.ng/rates/ExchRateByCurrency.html)
---

## 🔍 Research Questions

### 🧠 **Main Question**

> **How have the exchange rates between the Nigerian Naira and six major currencies evolved over 2009 to 2024, and what roles do oil prices and inflation play in shaping these trends and volatilities?**

---

## 📌 Subquestions
* What are the long-term trends in NGN exchange rates?
* Which currencies are most volatile vs the Naira?
* How are exchange rates correlated with oil prices and inflation?
* Do some currencies behave similarly vs NGN?

---

## 📊 Visualizations 

- Line plots of NGN vs each currency over time
- Rolling averages ( 6-month)
- Heatmap of correlation coefficients
- Box plots to compare overall volatility

---
## 📊 Key Insights
From 2009 to 2024, the Nigerian Naira faced ongoing depreciation, with major devaluation trends beginning in 2023 and culminating in the worst decline in 2024.
* Western currencies showed higher volatility compared to more stable Asian and African currencies.
* Inflation was strongly correlated with exchange rate changes, while crude oil prices had minimal impact.
* Currencies generally moved together, reflecting common economic influences.

---
## 🛠 Tech Stack
* Python (pandas, matplotlib, seaborn)
* Jupyter Notebook
* Streamlit for dashboard

