import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Stock Candlestick Viewer",
    page_icon="📊",
    layout="wide"
)

st.title("📈 Stock Candlestick Viewer")
st.caption("Interactive NSE candlestick charts with RSI & MACD overlays - Three Panel Layout")

# Sidebar inputs
st.sidebar.header("Chart Settings")

default_ticker = "TATAMOTORS.NS"
ticker = st.sidebar.text_input("NSE Ticker (Yahoo format)", default_ticker)

timeframe = st.sidebar.selectbox(
    "Timeframe",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
    index=1
)

interval = st.sidebar.selectbox(
    "Interval",
    ["1d", "1h", "30m", "15m"],
    index=0
)

show_rsi = st.sidebar.checkbox("Show RSI", value=True)
show_macd = st.sidebar.checkbox("Show MACD", value=True)

st.sidebar.info(
    "Examples: RELIANCE.NS, HDFCBANK.NS, INFY.NS, TCS.NS"
)

@st.cache_data(show_spinner=True)
def load_data(ticker: str, period: str, interval: str) -> pd.DataFrame:
    df = yf.download(ticker, period=period, interval=interval, auto_adjust=True)
    df.dropna(inplace=True)
    return df

def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)
    gain_ema = pd.Series(gain, index=series.index).ewm(alpha=1/period, adjust=False).mean()
    loss_ema = pd.Series(loss, index=series.index).ewm(alpha=1/period, adjust=False).mean()
    rs = gain_ema / loss_ema
    rsi = 100 - (100 / (1 + rs))
    return rsi

def compute_macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    hist = macd - signal_line
    return macd, signal_line, hist

if not ticker:
    st.warning("Enter a valid NSE ticker symbol to view the chart.")
    st.stop()

with st.spinner("Fetching market data..."):
    df = load_data(ticker, timeframe, interval)

if df.empty:
    st.error("No data returned. Check ticker or timeframe.")
    st.stop()

# Compute indicators
close = df["Close"]
if show_rsi:
    df["RSI"] = compute_rsi(close)
if show_macd:
    macd, signal_line, hist = compute_macd(close)
    df["MACD"] = macd
    df["Signal"] = signal_line
    df["Hist"] = hist

# Create subplots: 3 rows, 1 column
# Row 1: Candlestick + Volume (shared x-axis, dual y-axis)
# Row 2: RSI
# Row 3: MACD
rows = 3
row_heights = [0.5, 0.25, 0.25]

fig = make_subplots(
    rows=rows,
    cols=1,
    shared_xaxes=True,
    row_heights=row_heights,
    vertical_spacing=0.08,
    subplot_titles=("Price & Volume", "RSI (14)", "MACD (12, 26, 9)"),
    specs=[
        [{"secondary_y": True}],  # Row 1: dual y-axis
        [{"secondary_y": False}],  # Row 2
        [{"secondary_y": False}]   # Row 3
    ]
)

# Row 1: Candlestick
fig.add_trace(
    go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Price",
        showlegend=True
    ),
    row=1,
    col=1,
    secondary_y=False
)

# Row 1: Volume (right y-axis)
fig.add_trace(
    go.Bar(
        x=df.index,
        y=df["Volume"],
        name="Volume",
        marker=dict(color="rgba(128, 128, 128, 0.3)"),
        showlegend=True
    ),
    row=1,
    col=1,
    secondary_y=True
)

# Row 2: RSI
if show_rsi and "RSI" in df.columns:
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            name="RSI",
            line=dict(color="blue", width=2),
            showlegend=True
        ),
        row=2,
        col=1
    )
    
    # RSI reference lines (30, 70)
    fig.add_hline(y=30, line_dash="dash", line_color="red", row=2, col=1, opacity=0.5)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1, opacity=0.5)

# Row 3: MACD
if show_macd and {"MACD", "Signal", "Hist"}.issubset(df.columns):
    # Histogram
    colors = ["green" if x >= 0 else "red" for x in df["Hist"]]
    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Hist"],
            name="Histogram",
            marker=dict(color=colors),
            showlegend=True
        ),
        row=3,
        col=1
    )
    
    # MACD line
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MACD"],
            name="MACD",
            line=dict(color="blue", width=2),
            showlegend=True
        ),
        row=3,
        col=1
    )
    
    # Signal line
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Signal"],
            name="Signal",
            line=dict(color="orange", width=2),
            showlegend=True
        ),
        row=3,
        col=1
    )

# Update layout
fig.update_layout(
    title=f"<b>{ticker} Technical Analysis</b> ({timeframe}, {interval})",
    xaxis_rangeslider_visible=False,
    template="plotly_white",
    height=900,
    hovermode="x unified",
    margin=dict(l=50, r=50, t=80, b=50),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="gray",
        borderwidth=1
    )
)

# Update y-axes labels
fig.update_yaxes(title_text="Price (₹)", row=1, col=1, secondary_y=False)
fig.update_yaxes(title_text="Volume", row=1, col=1, secondary_y=True)
fig.update_yaxes(title_text="RSI", row=2, col=1, range=[0, 100])
fig.update_yaxes(title_text="MACD", row=3, col=1)

# Update x-axes
fig.update_xaxes(title_text="Date", row=3, col=1)

st.plotly_chart(fig, use_container_width=True)

# Data info section
with st.expander("📊 Data Info"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Price", f"₹{df['Close'].iloc[-1]:.2f}")
    
    with col2:
        change = df['Close'].iloc[-1] - df['Close'].iloc[0]
        pct_change = (change / df['Close'].iloc[0]) * 100
        st.metric("Change", f"₹{change:.2f}", f"{pct_change:.2f}%")
    
    with col3:
        st.metric("52W High", f"₹{df['High'].max():.2f}")
    
    with col4:
        st.metric("52W Low", f"₹{df['Low'].min():.2f}")

st.markdown(
    """
---
**How to use**

1. Enter an NSE ticker in Yahoo format (e.g., `TATAMOTORS.NS`, `RELIANCE.NS`, `HDFCBANK.NS`).
2. Choose timeframe (1 month to 5 years) and interval (daily to 15-minute).
3. Toggle RSI and MACD indicators in the sidebar.
4. Hover over charts for detailed values. Use zoom and pan for deeper analysis.

**Indicator Meanings**
- **RSI (14)**: Relative Strength Index. Values above 70 = overbought, below 30 = oversold.
- **MACD**: Momentum indicator. Blue line (MACD) crossing orange line (Signal) = potential trend change.
"""
)
