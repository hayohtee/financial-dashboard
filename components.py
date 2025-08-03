import streamlit as st
import yfinance as yf
import plotly.express as px

def stock_card(ticker_name: str):
    """Display stock information for a given ticker."""
    ticker = yf.Ticker(ticker_name)
    with st.container(border=True):
        st.subheader(ticker.info["longName"])
        st.write(f"Ticker: {ticker.ticker}")
        st.write(f"Current Price: ${ticker.history(period='1d')['Close'].iloc[-1]:.2f}")
        st.write(f"Market Cap: ${ticker.info['marketCap']:,}")
        st.write(f"Percentage Change (1Y): {ticker.history(period='1y')['Close'].pct_change().iloc[-1] * 100:.2f}%")
        df = ticker.history(period="1y")
        fig = px.line(df, x=df.index, y="Close", title=f"{ticker.ticker} Stock Price")
        st.plotly_chart(fig, use_container_width=True)