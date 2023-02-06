import streamlit as st
from plotly import graph_objs as go
import pandas as pd
import pickle


st.title('AAPL Stock Forecasting Using Streamlit')
st.subheader('Import Data')

data = st.file_uploader('Upload here',type='csv')

if data is not None:
    
    df = pd.read_csv(data)
    st.text('Displaying the first five and last five records')  
    st.write(df.head(),df.tail())
    df.set_index('Date',inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index,y=df.Close,name='stock_close'))
    fig.layout.update(title_text='Line graph of Close price',xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

    loaded_model = pickle.load(open('C:/Users/Dell/Assignments/model_trained.sav','rb'))
    st.subheader('To see the Forecast for next 30 days')

    if st.button('Click here'):
        
        fct = loaded_model.get_forecast(steps=30)
        ci_95 = pd.DataFrame(fct.conf_int())
        st.subheader('With 95 percent confidence interval')
        st.write(ci_95)
        
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ci_95.index,y=ci_95['lower Close'],name='Forecast_lower_limit'))
        fig3.add_trace(go.Scatter(x=ci_95.index,y=ci_95['upper Close'],name='Forecast_upper_limit'))
        fig3.layout.update(title_text='Forecast of Closing price for next 30 days with 95 percent confidence interval',xaxis_rangeslider_visible=True)
        st.plotly_chart(fig3)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df.index,y=df.Close,name='original_data'))
        fig2.add_trace(go.Scatter(x=ci_95.index,y=ci_95['lower Close'],name='Forecast_lower_limit'))
        fig2.add_trace(go.Scatter(x=ci_95.index,y=ci_95['upper Close'],name='Forecast_upper_limit'))
        fig2.layout.update(title_text='Displaying forecast along with the original data',xaxis_rangeslider_visible=True)
        st.plotly_chart(fig2)
        



