import investpy
import streamlit as st

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')


ls = investpy.get_stocks(country='south africa')
sm = investpy.get_stock_financial_summary(stock='SHPJ',country='south africa')
st.write(ls)
st.write(sm)
