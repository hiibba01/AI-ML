import streamlit as st
import pandas as pd

st.title("Streamlit Widgets")

name = st.text_input("Enter your name:")

age=st.slider("Select your age:", 0, 100, 25) #range of slider is from 0 to 100 and default value is 25

st.write(f"Your age is {age}")

if name:
    st.write(f"Hello, {name}!")

#using selectbox

options = ["Option 1", "Option 2", "Option 3"]
choice = st.selectbox("Select an option:", options)
st.write(f"You selected: {choice}")


#dataframe

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}


df=pd.DataFrame(data)
st.write("Here is the dataframe:")
st.dataframe(df)

#creating an upload button to upload a file
uploaded_file = st.file_uploader("Choose a file", type="png")

#to upload a csv file
csv_file = st.file_uploader("Choose a CSV file", type="csv")

df.to_csv("sampledata.csv")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)