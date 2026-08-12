import streamlit as st

st.set_page_config(page_title="Skill Gap", page_icon="💡")
st.title("💡 Skill Gap & Role Requirements")

role = st.selectbox("Select Target Role:", ["Data Scientist", "AI Engineer", "Full-Stack Developer"])

if role == "Data Scientist":
    st.write("### Essential Skills:")
    st.markdown("- Python, SQL, Pandas, Scikit-Learn\n- Machine Learning, Statistics, Tableau/PowerBI")
elif role == "AI Engineer":
    st.write("### Essential Skills:")
    st.markdown("- PyTorch/TensorFlow, NLP, LLMs\n- Docker, FastAPI, Vector Databases")
else:
    st.write("### Essential Skills:")
    st.markdown("- React/Vue, Node.js/Flask, PostgreSQL\n- REST APIs, Git, Cloud Services")
