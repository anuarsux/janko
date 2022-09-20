import streamlit as st

st.title("MY FIRST ML APP")
st.markdown("#Main Page")
st.sidebar.markdown("MainPage")
my_text = st.text("Janko, Bruno and Nils are:")
my_button = st.button("puchale aquí")
if my_button:
	st.title("My friends!")
