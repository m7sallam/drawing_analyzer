import streamlit as st
import os

st.set_page_config(page_title="Drawing Analyzer", page_icon="📐")
st.title("Drawing Analyzer AI")
st.write("Upload a 2D drawing to calculate the area.")

file = st.file_uploader("Upload Drawing", type=["pdf", "png", "jpg"])

if file:
    st.success("File uploaded! AI processing started...")
    # Logic from api.py will go here
