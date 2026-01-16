# Stock Candlestick Viewer 📈

> Interactive Streamlit app for NSE stock analysis with three-panel technical analysis layout. Part of the **FinStatAnalysis** ecosystem.

---

## Overview

Stock Candlestick Viewer is a powerful, lightweight tool for analyzing Indian stock market data with professional-grade technical indicators. Built with Streamlit and Plotly, it provides real-time candlestick charts, RSI, MACD, and volume analysis for informed investment decisions.

**Perfect for:**
- Day traders and swing traders
- Financial analysts and portfolio managers
- Students learning technical analysis
- Fintech developers integrating market data

---

## ✨ Features

✅ **Interactive Candlestick Charts**: Real-time NSE candlestick visualizations  
✅ **Three-Panel Layout**: Price & Volume | RSI | MACD technical indicators  
✅ **Flexible Timeframes**: 1 month, 3 months, 6 months, 1 year, 2 years, 5 years  
✅ **Intraday Support**: Daily, hourly, 30-minute, and 15-minute intervals  
✅ **Interactive Controls**: Zoom, pan, hover tooltips for detailed analysis  
✅ **Fast Data Loading**: Cached data via `@st.cache_data` for optimal performance  
✅ **Metrics Dashboard**: Current price, change %, 52-week high/low  
✅ **Customizable Indicators**: Toggle RSI and MACD on/off

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Streamlit |
| **Visualization** | Plotly (with subplots) |
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
cd FinStatAnalysis/stock-candlestick-viewer

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
   - Examples section below shows popular tickers
   - Press Enter to fetch data

3. **Select Timeframe**
   - Choose from: 1mo, 3mo, 6mo, 1y, 2y, 5y
   - Default: 3 months (good for most analysis)

4. **Choose Interval**
   - **1d**: Daily candlesticks (traditional analysis)
   - **1h**: Hourly candlesticks (intraday trading)
   - **30m**: 30-minute intervals (swing trading)
   - **15m**: 15-minute intervals (scalping)

5. **Toggle Indicators**
   - Check "Show RSI" for Relative Strength Index
   - Check "Show MACD" for Moving Average Convergence Divergence
   - Uncheck to focus on price action only

6. **Analyze the Three-Panel Layout**
   - **Panel 1**: Candlestick chart + Volume bars
   - **Panel 2**: RSI (0-100 scale)
   - **Panel 3**: MACD histogram + Signal line

7. **Interact with Charts**
   - **Hover**: See exact values at each point
   - **Zoom**: Double-click to zoom, double-click again to reset
   - **Pan**: Click and drag to move across the chart
   - **Export**: Click camera icon to save as PNG

---

## 📊 Example Tickers

| Symbol | Company | Sector |
|--------|---------|--------|
| `RELIANCE.NS` | Reliance Industries | Energy & Petrochemicals |
| `HDFCBANK.NS` | HDFC Bank | Banking & Finance |
| `INFY.NS` | Infosys | IT Services |
| `TCS.NS` | Tata Consultancy Services | IT Services |
| `TATAMOTORS.NS` | Tata Motors | Automotive |
| `WIPRO.NS` | Wipro | IT Services |
| `ITC.NS` | ITC Limited | Diversified |
| `MARUTI.NS` | Maruti Suzuki | Automotive |
| `POWERGRID.NS` | Power Grid Corporation | Power & Utilities |
| `SUNPHARMA.NS` | Sun Pharmaceutical | Pharmaceuticals |

---

## 📚 Technical Indicators Explained

### RSI (Relative Strength Index)
- **Range**: 0 to 100
- **Interpretation**:
  - Above 70 = Overbought (potential sell signal)
  - Below 30 = Oversold (potential buy signal)
  - 50 = Neutral zone
- **Period**: 14 days (default)
- **Use**: Identify momentum extremes and reversal points

### MACD (Moving Average Convergence Divergence)
- **Components**:
  - Blue line = MACD (12-day EMA - 26-day EMA)
  - Orange line = Signal line (9-day EMA of MACD)
  - Green/Red bars = Histogram (MACD - Signal)
- **Signals**:
  - MACD crosses above Signal = Bullish signal
  - MACD crosses below Signal = Bearish signal
  - Positive histogram = Bullish momentum
  - Negative histogram = Bearish momentum
- **Use**: Identify trend direction and momentum strength

### Volume Analysis
- **Gray bars**: Trading volume at each candle
- **High volume**: Confirms price breakouts
- **Low volume**: Reversal may be weak

---

## 💡 Tips for Better Analysis

1. **Use Multiple Timeframes**: Compare daily and intraday for confirmation
2. **RSI + MACD Combo**: Use together for stronger signals (not in isolation)
3. **Volume Confirmation**: Always check volume when prices break support/resistance
4. **Avoid News Events**: Stock prices often gap on news; wait for stabilization
5. **Risk Management**: Never risk more than 2% of portfolio on a single trade
6. **Backtesting**: Test your strategy on historical data before live trading

---

## 📝 Notes

- **Data Delay**: Yahoo Finance data may be delayed by 15-20 minutes during market hours
- **Market Hours**: NSE operates Monday-Friday, 9:15 AM - 3:30 PM IST
- **Holidays**: Stock exchanges closed on Indian national holidays
- **Accuracy**: Use this tool for analysis only; verify with official sources

---

## 🔗 Integration

Part of the **FinStatAnalysis** ecosystem. Complements:
- Balance sheet analysis tools
- Sector rotation screeners
- Financial ratio calculators
- LLM-powered financial insights

---

## ⚖️ Disclaimer

**EDUCATIONAL PURPOSE ONLY**

This application is designed solely for educational and informational purposes. By using this tool, you acknowledge that:

1. **No Investment Advice**: This is NOT financial or investment advice. Always consult a qualified financial advisor before making investment decisions.
2. **No Guarantee**: Past performance does not guarantee future results. Market conditions change rapidly.
3. **Risk Acknowledgment**: Stock market investing carries significant risk of loss. Only invest money you can afford to lose.
4. **Data Accuracy**: While we strive for accuracy, we do not guarantee the completeness or accuracy of data from Yahoo Finance.
5. **User Responsibility**: You are solely responsible for your investment decisions and any losses incurred.
6. **No Liability**: The creators are not liable for any financial losses or damages resulting from using this application.

**Use this tool to learn and practice technical analysis, not for real money trading without proper knowledge and risk management.**

---

## 👨‍💻 About the Creator

Built with ❤️ by **Ankit** (@Ank576)

- **Focus**: Fintech, Financial Literacy & Stock Market Analysis
- **Location**: Jhansi, Uttar Pradesh, India 🇮🇳
- **GitHub**: [github.com/Ank576](https://github.com/Ank576)
- **Projects**: FinStatAnalysis, LLM-powered apps, Agricultural Finance

This tool is part of my mission to democratize financial knowledge and make stock market analysis accessible to everyone in India.

---

## 📞 Support & Feedback

- **Issues**: Report bugs on [GitHub Issues](https://github.com/Ank576/FinStatAnalysis/issues)
- **Discussions**: Share ideas in [GitHub Discussions](https://github.com/Ank576/FinStatAnalysis/discussions)
- **Contributions**: Pull requests welcome! See CONTRIBUTING.md

---

## 📄 License

MIT License - See LICENSE file for details

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Status**: Active & Maintained ✅
