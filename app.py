import streamlit as st
import openai
import pandas as pd
import PyPDF2
import os

# --- CONFIG ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Ominra AI", layout="wide")
st.title("🧠 Ominra AI – Private Intelligence System")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload a document or CSV", type=["pdf", "txt", "csv"])

content = ""

uploaded_file = st.file_uploader("Upload a file", type=["pdf"])

if uploaded_file is not None:
  if uploaded_file.type == "application/pdf":
    st.success("PDF file uploaded successfully!")
else:
  st.error("Please upload a PDF file only.")

reader = PyPDF2.PdfReader(uploaded_file)
for page in reader.pages:
  content += page.extract_text()

elif uploaded_file.type == "text/plain":
  content = uploaded_file.read().decode("utf-8")

elif uploaded_file.type == "text/csv":
  df = pd.read_csv(uploaded_file)
  content = df.to_string()

st.success("File loaded successfully")

# --- QUESTION INPUT ---
question = st.text_input("Ask Ominra AI:")

if question and content:
with st.spinner("Ominra AI is thinking..."):
  response = openai.ChatCompletion.create(
model="gpt-4o-mini",
messages=[
{"role": "system", "content": "You are Ominra AI, a private business intelligence assistant."},
{"role": "user", "content": f"DATA:\n{content}\n\nQUESTION:\n{question}"}
]
)

st.subheader("📊 Ominra AI Response")
st.write(response.choices[0].message.content)
