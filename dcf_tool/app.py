import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="DCF Valuation Tool", layout="wide")

st.title("💰 DCF Valuation Tool")
st.write("Educational Streamlit app to experiment with Discounted Cash Flow (DCF) valuation assumptions.")

# Sidebar inputs
st.sidebar.header("📈 Input Assumptions")

ticker = st.sidebar.text_input("📊 Ticker (optional)", value="RELIANCE.NS", help="Stock ticker symbol for reference")
years = st.sidebar.slider("📅 Projection years", 5, 15, 10, help="Number of years to project cash flows")
revenue_start = st.sidebar.number_input("💵 Starting revenue (₹ Cr)", value=1000.0, min_value=0.0, help="Current or Year 0 revenue")
growth_rate = st.sidebar.slider("📈 Annual revenue growth (%)", 0.0, 30.0, 10.0, help="Expected annual revenue growth rate")
ebit_margin = st.sidebar.slider("📊 EBIT margin (%)", 0.0, 50.0, 20.0, help="Operating profit margin")
tax_rate = st.sidebar.slider("📋 Tax rate (%)", 0.0, 40.0, 25.0, help="Corporate tax rate")
discount_rate = st.sidebar.slider("📉 Discount rate / WACC (%)", 5.0, 20.0, 12.0, help="Weighted Average Cost of Capital")
terminal_growth = st.sidebar.slider("🔚 Terminal growth (%)", 0.0, 6.0, 3.0, help="Perpetual growth rate beyond projection period")
shares_out = st.sidebar.number_input("📊 Shares outstanding (Cr)", value=100.0, min_value=0.01, help="Number of shares outstanding")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip**: Adjust the sliders to see how different assumptions affect the valuation.")

# DCF calculation
years_range = np.arange(1, years + 1)
revenues = revenue_start * (1 + growth_rate / 100) ** years_range
ebit = revenues * ebit_margin / 100
nopat = ebit * (1 - tax_rate / 100)
free_cash_flow = nopat  # Simplified: Assuming FCF = NOPAT

discount_factors = (1 + discount_rate / 100) ** years_range
discounted_fcf = free_cash_flow / discount_factors

# Terminal value calculation
terminal_value = free_cash_flow[-1] * (1 + terminal_growth / 100) / (
    (discount_rate / 100) - (terminal_growth / 100)
)
terminal_pv = terminal_value / ((1 + discount_rate / 100) ** years)

enterprise_value = discounted_fcf.sum() + terminal_pv
intrinsic_value_per_share = enterprise_value / shares_out

# Display results
st.subheader("📊 DCF Valuation Summary")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🏢 Enterprise Value (₹ Cr)", f"{enterprise_value:,.2f}")
with col2:
    st.metric("💵 Intrinsic Value per Share (₹)", f"{intrinsic_value_per_share:,.2f}")
with col3:
    st.metric("📊 Terminal Value (₹ Cr)", f"{terminal_value:,.2f}")

st.markdown("---")

# Projected cash flows table
st.subheader("📈 Projected Free Cash Flows (₹ Cr)")

df = pd.DataFrame(
    {
        "Year": years_range,
        "Revenue": revenues,
        "EBIT": ebit,
        "NOPAT": nopat,
        "Free Cash Flow": free_cash_flow,
        "Discount Factor": discount_factors,
        "Discounted FCF": discounted_fcf,
    }
)

st.dataframe(
    df.style.format(
        {
            "Revenue": "{:,.2f}",
            "EBIT": "{:,.2f}",
            "NOPAT": "{:,.2f}",
            "Free Cash Flow": "{:,.2f}",
            "Discount Factor": "{:.3f}",
            "Discounted FCF": "{:,.2f}",
        }
    ),
    use_container_width=True,
)

st.markdown("---")

# Breakdown
st.subheader("🧩 Valuation Breakdown")

col1, col2 = st.columns(2)
with col1:
    st.write("**PV of Projected FCFs:**")
    st.write(f"₹ {discounted_fcf.sum():,.2f} Cr")
with col2:
    st.write("**PV of Terminal Value:**")
    st.write(f"₹ {terminal_pv:,.2f} Cr")

st.write(f"**Total Enterprise Value:** ₹ {enterprise_value:,.2f} Cr")
st.write(f"**Shares Outstanding:** {shares_out:,.2f} Cr")
st.write(f"**Intrinsic Value per Share:** ₹ {intrinsic_value_per_share:,.2f}")

st.markdown("---")

# Educational notes
with st.expander("📚 Learn More About DCF"):
    st.markdown("""
    ### What is DCF Valuation?
    
    **Discounted Cash Flow (DCF)** is a valuation method used to estimate the value of an investment based on its expected future cash flows.
    
    ### Key Steps:
    1. **Project Free Cash Flows**: Estimate future cash flows based on revenue, margins, and expenses.
    2. **Determine Discount Rate**: Use the company's Weighted Average Cost of Capital (WACC).
    3. **Calculate Terminal Value**: Estimate the value beyond the projection period.
    4. **Discount to Present Value**: Apply the discount rate to bring future cash flows to today's value.
    5. **Sum and Divide**: Add all discounted cash flows and divide by shares outstanding.
    
    ### Limitations:
    - Highly sensitive to assumptions (growth rate, discount rate, terminal value)
    - Requires accurate financial forecasting
    - May not capture market sentiment or qualitative factors
    """)

st.caption(
    "⚠️ This tool is for **educational** purposes only and does not constitute financial advice."
)
