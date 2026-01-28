uploaded_file = st.file_uploader("Upload a file", type=["pdf"])

if uploaded_file is not None:
if uploaded_file.type == "application/pdf":
st.success("PDF file uploaded successfully!")
else:
st.error("Please upload a PDF file only.")
