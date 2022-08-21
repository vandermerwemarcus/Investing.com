import investpy
import streamlit as st

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')


sm = investpy.get_stock_dividends(stock='SHP',country='South Africa')
st.write(df)
st.write(sm)
