#Streamlit is an opensource app framework for machine learning and data scoience projects. It helps to create beautiful web apps in a short time with minimal effort. It is a great tool for data scientists and machine learning engineers to showcase their work and share it with others.

import streamlit as st
import pandas as pd
import numpy as np

#Title of application

st.title("HELLOOOO EVERYBODY!!!")

#display simple text
st.write("This is a simple text!")

#create a simple dataframe

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

#display the dataframe in the app
st.write("Here is the dataframe:")
st.write(df)

##create a linechart

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)