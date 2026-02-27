import streamlit as st

st.set_page_config(page_title="Drawing Analyzer", page_icon="📐")
st.title("Drawing Analyzer AI")
st.subheader("AI-Powered Area Calculator for 2D Drawings")

uploaded_file = st.file_uploader("Upload your drawing (PDF or Image)", type=['pdf', 'png', 'jpg', 'jpeg'])

if uploaded_file:
    st.info("File received! Processing for area calculation...")
