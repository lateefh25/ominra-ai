import streamlit as st

st.set_page_config(
    page_title="Ominra AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ OMINRA AI")
st.subheader("Cyber Intelligence Assistant for Ominra Cyber Tech")

st.write("""
Welcome to **Ominra AI**.

This AI will evolve into:
- SOC analyst assistant  
- Incident reasoning engine  
- Cyber risk & intelligence advisor  
- Internal AI brain of Ominra Cyber Tech
""")

st.divider()

user_input = st.text_area("Ask Ominra AI:", placeholder="Example: Explain what a SOC analyst does")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.success("Ominra AI received your query.")
        st.write("⚙️ Response engine will be connected next.")
