# Stock Candlestick Viewer

Interactive Streamlit app for NSE stock analysis with three-panel technical analysis layout, integrated as a sub-app in **FinStatAnalysis**.

## Features

✅ **Candlestick Charts**: NSE ticker input (Yahoo format)  
✅ **Three-Panel Layout**: Price + Volume | RSI | MACD  
✅ **Flexible Timeframes**: 1 month to 5 years  
✅ **Intraday Support**: 15-min, 30-min, hourly intervals  
✅ **Interactive Plotly Charts**: Zoom, pan, hover tooltips  
✅ **Cached Data**: Fast load times via `@st.cache_data`  
✅ **Metrics Dashboard**: Current price, change %, high/low  

## Tech Stack

- **Streamlit**: UI framework
- **Plotly**: Interactive visualizations with subplots
- **yfinance**: Yahoo Finance API wrapper
- **pandas / numpy**: Data processing

## Installation

```bash
git clone https://github.com/<username>/FinStatAnalysis.git
cd FinStatAnalysis/stock-candlestick-viewer
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Run `streamlit run app.py`
2. Enter NSE ticker (e.g., `RELIANCE.NS`, `TATAMOTORS.NS`)
3. Select timeframe and interval
4. Toggle RSI/MACD indicators
5. Interact with the three-panel chart

## Example Tickers

- `RELIANCE.NS` (Reliance Industries)
- `HDFCBANK.NS` (HDFC Bank)
- `INFY.NS` (Infosys)
- `TCS.NS` (Tata Consultancy Services)
- `TATAMOTORS.NS` (Tata Motors)

## Notes

- Data fetched from Yahoo Finance (may have slight delays)
- For educational and analysis purposes only
- Indicators: RSI (14), MACD (12, 26, 9)

## Integration

Part of FinStatAnalysis ecosystem. Complements balance sheet analysis and sector rotation tools.
