import investpy
import streamlit as st

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')
st.write(df)

sm = investpy.get_stock_financial_summary(stock='CFRJ',country='South Africa')
st.write(sm)
