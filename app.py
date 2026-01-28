import streamlit as st

st.title("Ominra AI")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    st.write("File received")

    if uploaded_file.type == "application/pdf":
        st.success("PDF uploaded successfully")
