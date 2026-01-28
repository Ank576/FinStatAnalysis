# DCF Valuation Tool

Streamlit-based **DCF (Discounted Cash Flow) valuation** tool inside the FinStatAnalysis repo.

## Overview

- Educational DCF analysis app built with Streamlit
- Calculate intrinsic stock value using fundamental assumptions
- Part of the FinStatAnalysis toolkit for financial statement and market analysis
- For learning and experimentation only (not investment advice)

## Features

- **Interactive DCF Calculator**: Input financial assumptions to compute enterprise value and intrinsic value per share
- **Customizable Parameters**: 
  - Revenue growth rates
  - EBIT margins
  - Tax rates
  - Discount rate (WACC)
  - Terminal growth rate
  - Shares outstanding
- **Visual Cash Flow Projections**: See projected revenues, EBIT, NOPAT, and free cash flows
- **Educational Focus**: Learn DCF methodology through hands-on experimentation

## Installation

```bash
git clone https://github.com/Ank576/FinStatAnalysis.git
cd FinStatAnalysis/dcf_tool
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## DCF Methodology

This tool implements a simplified DCF model:

1. **Project Free Cash Flows (FCF)**: Based on revenue growth, margins, and tax assumptions
2. **Discount FCFs**: Apply discount rate (WACC) to get present value
3. **Calculate Terminal Value**: Using perpetuity growth method
4. **Sum to Enterprise Value**: PV of FCFs + PV of Terminal Value
5. **Intrinsic Value per Share**: Enterprise Value / Shares Outstanding

## Disclaimer

This app is for **educational purposes only** and does not constitute financial advice. DCF valuation involves many assumptions and simplifications. Always conduct thorough research before making investment decisions.
