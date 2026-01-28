import streamlit as st

st.set_page_config(page_title="Ominra AI")

st.title("Ominra AI")
st.write("Upload a PDF file")

uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully")
    st.write(uploaded_file.name)
