import streamlit as st

st.set_page_config(page_title="AI Career Hub", page_icon="🚀", layout="wide")

st.title("🚀 AI-Powered Career & Resume Intelligence")
st.subheader("Welcome to your multi-page resume optimization toolkit!")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("### 📊 Page 1: ATS Scanner")
    st.write("Upload PDF resume, paste job description, and get instant score + missing skills.")

with col2:
    st.success("### 💡 Page 2: Skill Gap Analyzer")
    st.write("Explore top skills required for Data Science, AI, and Software roles.")

with col3:
    st.warning("### 📜 Page 3: History & Tracker")
    st.write("Track your previous resume match logs.")

st.markdown("---")
st.success("👈 Left side bar se navigation open karke kisi bhi page par jaao!")
