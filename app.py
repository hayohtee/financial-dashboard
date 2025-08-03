import streamlit as st
from components import stock_card

st.header("Stock markets")
st.text("Overview of stock markets for big tech companies")

# Define the list of big tech companies
big_tech_companies = [
    "AAPL",  # Apple Inc.
    "GOOGL",  # Alphabet Inc. (Google)
    "AMZN",  # Amazon.com Inc.
    "MSFT",  # Microsoft Corporation
    "META",  # Meta Platforms, Inc. (Facebook)
    "NFLX",  # Netflix, Inc.
    "TSLA",  # Tesla, Inc.
    "NVDA",  # NVIDIA Corporation
]


# Display stock cards for each big tech company
for company in big_tech_companies:
    stock_card(company)