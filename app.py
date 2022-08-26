import streamlit as st

st.title("AI Art Tool")
st.write("Text to Image generator")

promp = st.text_input("Input promp:")
st.write(promp)
