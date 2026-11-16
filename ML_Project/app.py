import streamlit as streamlit
st.title("My first streamlit app")
name=st.text_input("Enter your name")
if name:
    st.write("Hello", Name)
