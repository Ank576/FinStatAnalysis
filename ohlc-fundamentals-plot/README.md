# OHLC Fundamentals Plot 📊

> Streamlit app combining technical OHLC candlestick charts with fundamental balance sheet metrics for comprehensive NSE stock analysis.

---

## Overview

OHLC Fundamentals Plot bridges the gap between technical and fundamental analysis by providing mplfinance candlestick visualizations alongside key balance sheet metrics. This tool helps traders and investors make informed decisions by viewing both price action and company fundamentals in one place.

**Unique Combination:**
- Technical Analysis: OHLC candlestick charts
- Fundamental Analysis: Balance sheet metrics table
- Real-time NSE stock data via yfinance

---

## ✨ Features

✅ **mplfinance Candlestick Charts**: Clean, professional OHLC visualizations  
✅ **Balance Sheet Metrics**: Assets, Liabilities, Equity, Working Capital  
✅ **NSE Stock Support**: Yahoo Finance format (e.g., RELIANCE.NS)  
✅ **Multiple Timeframes**: 1 month to 5 years  
✅ **Publication-Ready**: High-quality charts for reports and presentations  
✅ **Fundamental Ratios**: Quick Ratio, Current Ratio, Debt-to-Equity  
✅ **Clean UI**: Simple, focused interface for analysis  
✅ **Export Options**: Save charts for documentation

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Streamlit |
| **Charting** | mplfinance |
| **Data Source** | Yahoo Finance (yfinance) |
| **Data Processing** | pandas, numpy |
| **Python** | 3.8+ |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda

### Quick Start

```bash
# Clone the FinStatAnalysis repository
git clone https://github.com/Ank576/FinStatAnalysis.git
cd FinStatAnalysis/ohlc-fundamentals-plot

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🚀 Usage Guide

### Step-by-Step Instructions

1. **Start the Application**
   ```bash
   streamlit run app.py
   ```

2. **Enter NSE Ticker Symbol**
   - Use Yahoo Finance format (e.g., `RELIANCE.NS`, `TATAMOTORS.NS`)
   - Press Enter to load data

3. **Select Timeframe**
   - Choose from: 1mo, 3mo, 6mo, 1y, 2y, 5y
   - Default: 3 months

4. **Analyze the Charts**
   - **Top Section**: OHLC candlestick chart with volume
   - **Bottom Section**: Balance sheet metrics table

5. **Review Fundamentals**
   - Total Assets, Total Liabilities, Stockholders Equity
   - Current Assets, Current Liabilities, Working Capital
   - Quick Ratio, Current Ratio, Debt-to-Equity Ratio

6. **Export Charts**
   - Right-click on charts to save as PNG
   - Use for reports, presentations, or analysis documentation

---

## 📊 Balance Sheet Metrics Explained

### Assets & Liabilities
- **Total Assets**: Everything the company owns
- **Total Liabilities**: Everything the company owes
- **Stockholders Equity**: Net worth (Assets - Liabilities)

### Working Capital
- **Current Assets**: Assets convertible to cash within 1 year
- **Current Liabilities**: Debts due within 1 year
- **Working Capital**: Current Assets - Current Liabilities
- **Interpretation**: Positive = healthy liquidity

### Financial Ratios
- **Quick Ratio**: (Current Assets - Inventory) / Current Liabilities
  - Above 1.0 = good short-term liquidity
- **Current Ratio**: Current Assets / Current Liabilities
  - Above 2.0 = healthy liquidity position
- **Debt-to-Equity**: Total Debt / Stockholders Equity
  - Below 1.0 = conservative leverage

---

## 📈 Example Tickers

| Symbol | Company | Sector |
|--------|---------|--------|
| `RELIANCE.NS` | Reliance Industries | Energy & Petrochemicals |
| `HDFCBANK.NS` | HDFC Bank | Banking & Finance |
| `INFY.NS` | Infosys | IT Services |
| `TCS.NS` | Tata Consultancy Services | IT Services |
| `TATAMOTORS.NS` | Tata Motors | Automotive |
| `ITC.NS` | ITC Limited | Diversified |
| `WIPRO.NS` | Wipro | IT Services |
| `MARUTI.NS` | Maruti Suzuki | Automotive |

---

## 💡 Analysis Tips

1. **Combine Technical & Fundamental**: Look for stocks with strong balance sheets AND bullish price action
2. **Check Working Capital**: Positive working capital indicates ability to meet short-term obligations
3. **Debt Levels**: High debt-to-equity may be risky during market downturns
4. **Price vs Value**: Use fundamentals to identify undervalued stocks with good technicals
5. **Sector Comparison**: Compare balance sheets of companies in the same sector
6. **Trend Analysis**: Track how fundamentals change over multiple quarters

---

## 📝 Notes

- **Data Source**: Yahoo Finance (may have 15-20 minute delays during market hours)
- **Frequency**: Fundamental data is typically quarterly
- **Accuracy**: Always verify with official company filings
- **Market Hours**: NSE operates Monday-Friday, 9:15 AM - 3:30 PM IST

---

## 🔗 Integration

Part of the **FinStatAnalysis** ecosystem. Complements:
- Stock Candlestick Viewer (technical analysis)
- Balance Sheet analysis guides
- Financial ratios documentation
- Investment decision frameworks

---

## ⚖️ Disclaimer

**EDUCATIONAL PURPOSE ONLY**

This application is designed solely for educational and informational purposes. By using this tool, you acknowledge that:

1. **No Investment Advice**: This is NOT financial or investment advice. Always consult a qualified financial advisor.
2. **No Guarantee**: Past performance and current fundamentals do not guarantee future results.
3. **Risk Acknowledgment**: Stock market investing carries significant risk of loss.
4. **Data Accuracy**: We do not guarantee the completeness or accuracy of data from Yahoo Finance.
5. **User Responsibility**: You are solely responsible for your investment decisions and any losses incurred.
6. **No Liability**: The creators are not liable for any financial losses resulting from using this application.

**Use this tool to learn and practice financial analysis, not for real money trading without proper knowledge.**

---

## 👨‍💻 About the Creator

Built with 🧡 by **Ankit** (@Ank576)

- **Focus**: Fintech, Financial Literacy & Stock Market Analysis
- **Location**: Jhansi, Uttar Pradesh, India 🇮🇳
- **GitHub**: [github.com/Ank576](https://github.com/Ank576)
- **Projects**: FinStatAnalysis, LLM-powered apps, Agricultural Finance

This tool is part of my mission to democratize financial knowledge and make stock market analysis accessible to everyone in India.

---

## 📞 Support & Feedback

- **Issues**: Report bugs on [GitHub Issues](https://github.com/Ank576/FinStatAnalysis/issues)
- **Discussions**: Share ideas in [GitHub Discussions](https://github.com/Ank576/FinStatAnalysis/discussions)
- **Contributions**: Pull requests welcome!

---

## 📄 License

MIT License - See LICENSE file for details

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Status**: Active & Maintained ✅
