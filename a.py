import streamlit as st

st.title("MY FIRST ML APP")
st.markdown("#Main Page")
st.sidebar.markdown("MainPage")
my_text = st.text("A ramdom version 2 of text")
my_button = st.button("puchale aquí")
if my_button:
	st.title("The model is running")
