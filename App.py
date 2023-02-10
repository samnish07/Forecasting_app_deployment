import streamlit as st
from plotly import graph_objs as go
import pandas as pd
import pickle
import os


st.title('AAPL Stock Forecasting Using Streamlit')
st.subheader('AAPL Dataset')

df = pd.read_csv('C:/Users/Dell/Assignments/AAPL.csv')
st.write(df)
df.set_index('Date',inplace=True)
    
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index,y=df.Close,name='stock_close'))
fig.layout.update(title_text='Line graph of Close price',xaxis_rangeslider_visible=True)
st.plotly_chart(fig)

loaded_model = pickle.load(open('C:/Users/Dell/Assignments/model_trained.sav','rb'))
st.sidebar.header('Forecast Stock prices')
days = st.sidebar.slider('Days for Prediction',0,200)
if days > 1:
    fct = pd.DataFrame(loaded_model.forecast(days))
    st.write(fct)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=fct.index,y=fct.predicted_mean,name='Forecast'))
    fig2.layout.update(title_text='Forecast of Closing price for the next given number of days',xaxis_rangeslider_visible=True)
    st.plotly_chart(fig2)

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df.index,y=df.Close,name='original_data'))
    fig3.add_trace(go.Scatter(x=fct.index,y=fct.predicted_mean,name='Forecast'))
    fig3.layout.update(title_text='Displaying forecast along with the original data',xaxis_rangeslider_visible=True)
    st.plotly_chart(fig3)
        



