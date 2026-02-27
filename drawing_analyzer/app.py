import streamlit as st
import api
st.title("Drawing Analyzer AI")
st.write("Welcome to the AI Area Calculator.")
uploaded_file = st.file_uploader("Choose a 2D Drawing (PDF/Image)", type=['pdf', 'png', 'jpg'])
if uploaded_file is not None:
st.success("File uploaded! Processing...")
