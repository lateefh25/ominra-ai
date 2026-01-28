import streamlit as st

st.set_page_config(page_title="Ominra AI", layout="centered")

st.title("🔐 Ominra AI – Cyber Intelligence Platform")
st.write("Upload a PDF report to begin analysis")

uploaded_file = st.file_uploader(
    "Upload SOC / Security PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        st.success("✅ PDF uploaded successfully")
        st.write("Filename:", uploaded_file.name)
    else:
        st.error("❌ Please upload a PDF file only")
