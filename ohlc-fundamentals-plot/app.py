import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(
    page_title="OHLC Fundamentals Plot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 OHLC Fundamentals Plot")
st.caption("Combine Technical OHLC Charts with Fundamental Balance Sheet Metrics")

# Sidebar inputs
st.sidebar.header("Settings")

default_ticker = "TATAMOTORS.NS"
ticker = st.sidebar.text_input("NSE Ticker (Yahoo format)", default_ticker)

timeframe = st.sidebar.selectbox(
    "Timeframe",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
    index=1
)

st.sidebar.info(
    "Examples: RELIANCE.NS, HDFCBANK.NS, INFY.NS, TCS.NS, TATAMOTORS.NS"
)

@st.cache_data(show_spinner=True)
def load_price_data(ticker: str, period: str) -> pd.DataFrame:
    """Load historical OHLC price data"""
    df = yf.download(ticker, period=period, auto_adjust=False)
    df.dropna(inplace=True)
    return df

@st.cache_data(show_spinner=True)
def load_fundamentals(ticker: str):
    """Load balance sheet fundamental data"""
    stock = yf.Ticker(ticker)
    
    # Get balance sheet
    balance_sheet = stock.balance_sheet
    
    # Get quarterly balance sheet for more recent data
    quarterly_bs = stock.quarterly_balance_sheet
    
    return balance_sheet, quarterly_bs, stock.info

def format_number(num):
    """Format large numbers for readability"""
    if pd.isna(num):
        return "N/A"
    if abs(num) >= 1e9:
        return f"₹{num/1e9:.2f}B"
    elif abs(num) >= 1e7:
        return f"₹{num/1e7:.2f}Cr"
    elif abs(num) >= 1e5:
        return f"₹{num/1e5:.2f}L"
    else:
        return f"₹{num:,.0f}"

if not ticker:
    st.warning("⚠️ Enter a valid NSE ticker symbol to view analysis.")
    st.stop()

# Load data
try:
    with st.spinner("🔄 Fetching price data..."):
        df = load_price_data(ticker, timeframe)
    
    with st.spinner("🔄 Loading fundamental data..."):
        balance_sheet, quarterly_bs, info = load_fundamentals(ticker)
        
    if df.empty:
        st.error("❌ No price data returned. Check ticker symbol or timeframe.")
        st.stop()
        
except Exception as e:
    st.error(f"❌ Error loading data: {str(e)}")
    st.stop()

# Display company info
st.subheader(f"🏢 {info.get('longName', ticker)}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Current Price",
        f"₹{df['Close'].iloc[-1]:.2f}"
    )

with col2:
    change = df['Close'].iloc[-1] - df['Close'].iloc[0]
    pct_change = (change / df['Close'].iloc[0]) * 100
    st.metric(
        "Change",
        f"₹{change:.2f}",
        f"{pct_change:.2f}%"
    )

with col3:
    st.metric(
        "High",
        f"₹{df['High'].max():.2f}"
    )

with col4:
    st.metric(
        "Low",
        f"₹{df['Low'].min():.2f}"
    )

st.divider()

# OHLC Candlestick Chart using mplfinance
st.subheader("🝯️ OHLC Candlestick Chart")

try:
    # Create mplfinance chart
    fig, axes = mpf.plot(
        df,
        type='candle',
        style='yahoo',
        title=f'{ticker} - {timeframe}',
        volume=True,
        ylabel='Price (₹)',
        ylabel_lower='Volume',
        figsize=(14, 8),
        returnfig=True
    )
    
    # Display the chart in Streamlit
    st.pyplot(fig)
    
    # Add download button for the chart
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    
    st.download_button(
        label="💾 Download Chart as PNG",
        data=buf,
        file_name=f"{ticker}_ohlc_chart.png",
        mime="image/png"
    )
    
except Exception as e:
    st.error(f"❌ Error creating OHLC chart: {str(e)}")

st.divider()

# Balance Sheet Fundamentals
st.subheader("💼 Balance Sheet Metrics")

if not balance_sheet.empty:
    try:
        # Get the most recent balance sheet data
        latest_bs = balance_sheet.iloc[:, 0]
        
        # Extract key metrics
        total_assets = latest_bs.get('Total Assets', np.nan)
        total_liabilities = latest_bs.get('Total Liabilities Net Minority Interest', np.nan)
        stockholders_equity = latest_bs.get('Stockholders Equity', np.nan)
        current_assets = latest_bs.get('Current Assets', np.nan)
        current_liabilities = latest_bs.get('Current Liabilities', np.nan)
        total_debt = latest_bs.get('Total Debt', np.nan)
        cash = latest_bs.get('Cash And Cash Equivalents', np.nan)
        inventory = latest_bs.get('Inventory', np.nan)
        
        # Calculate derived metrics
        working_capital = current_assets - current_liabilities if not pd.isna(current_assets) and not pd.isna(current_liabilities) else np.nan
        current_ratio = current_assets / current_liabilities if not pd.isna(current_assets) and not pd.isna(current_liabilities) and current_liabilities != 0 else np.nan
        quick_ratio = (current_assets - inventory) / current_liabilities if not pd.isna(current_assets) and not pd.isna(inventory) and not pd.isna(current_liabilities) and current_liabilities != 0 else np.nan
        debt_to_equity = total_debt / stockholders_equity if not pd.isna(total_debt) and not pd.isna(stockholders_equity) and stockholders_equity != 0 else np.nan
        
        # Display metrics in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 💵 Assets & Liabilities")
            metrics_data = {
                "Metric": [
                    "Total Assets",
                    "Total Liabilities",
                    "Stockholders Equity",
                    "Total Debt",
                    "Cash & Equivalents"
                ],
                "Value": [
                    format_number(total_assets),
                    format_number(total_liabilities),
                    format_number(stockholders_equity),
                    format_number(total_debt),
                    format_number(cash)
                ]
            }
            st.dataframe(pd.DataFrame(metrics_data), use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("### 📊 Working Capital")
            wc_data = {
                "Metric": [
                    "Current Assets",
                    "Current Liabilities",
                    "Working Capital",
                    "Inventory"
                ],
                "Value": [
                    format_number(current_assets),
                    format_number(current_liabilities),
                    format_number(working_capital),
                    format_number(inventory)
                ]
            }
            st.dataframe(pd.DataFrame(wc_data), use_container_width=True, hide_index=True)
        
        with col3:
            st.markdown("### 📈 Financial Ratios")
            ratios_data = {
                "Metric": [
                    "Current Ratio",
                    "Quick Ratio",
                    "Debt-to-Equity"
                ],
                "Value": [
                    f"{current_ratio:.2f}" if not pd.isna(current_ratio) else "N/A",
                    f"{quick_ratio:.2f}" if not pd.isna(quick_ratio) else "N/A",
                    f"{debt_to_equity:.2f}" if not pd.isna(debt_to_equity) else "N/A"
                ],
                "Status": [
                    "✅ Good" if not pd.isna(current_ratio) and current_ratio > 1.5 else "⚠️ Low" if not pd.isna(current_ratio) else "N/A",
                    "✅ Good" if not pd.isna(quick_ratio) and quick_ratio > 1.0 else "⚠️ Low" if not pd.isna(quick_ratio) else "N/A",
                    "✅ Conservative" if not pd.isna(debt_to_equity) and debt_to_equity < 1.0 else "⚠️ High" if not pd.isna(debt_to_equity) else "N/A"
                ]
            }
            st.dataframe(pd.DataFrame(ratios_data), use_container_width=True, hide_index=True)
        
        # Display full balance sheet in expander
        with st.expander("📝 View Full Balance Sheet"):
            st.dataframe(balance_sheet.head(20), use_container_width=True)
            
    except Exception as e:
        st.error(f"❌ Error processing balance sheet: {str(e)}")
else:
    st.warning("⚠️ No balance sheet data available for this ticker.")

st.divider()

# Analysis Tips
with st.expander("💡 How to Interpret This Data"):
    st.markdown("""
    ### Technical Analysis (OHLC Chart)
    - **Green Candles**: Closing price > Opening price (Bullish)
    - **Red Candles**: Closing price < Opening price (Bearish)
    - **Volume**: High volume confirms price movements
    - **Trends**: Look for consistent patterns over time
    
    ### Fundamental Analysis (Balance Sheet)
    - **Current Ratio > 2.0**: Healthy liquidity position
    - **Quick Ratio > 1.0**: Can meet short-term obligations without selling inventory
    - **Debt-to-Equity < 1.0**: Conservative leverage, lower financial risk
    - **Positive Working Capital**: Company can cover short-term liabilities
    
    ### Combined Analysis
    1. **Strong Fundamentals + Bullish Technicals**: Good investment opportunity
    2. **Weak Fundamentals + Bearish Technicals**: Avoid or short
    3. **Mixed Signals**: Requires deeper analysis
    """)

st.markdown(
    """
    ---
    **Disclaimer**: This tool is for educational purposes only. Not financial advice. 
    Always consult a qualified financial advisor before making investment decisions.
    
    Built with 🧡 by **Ankit** | Part of [FinStatAnalysis](https://github.com/Ank576/FinStatAnalysis)
    """
)
