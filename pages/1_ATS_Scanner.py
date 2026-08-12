import streamlit as st
import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="ATS Scanner", page_icon="📊")

st.title("📊 ATS Resume & JD Matcher")

EXTRA_STOP_WORDS = {'looking', 'skilled', 'engineer', 'role', 'seeking', 'work', 'job', 'description', 'required'}

def extract_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description (JD) here...", height=150)

if st.button("Scan Resume"):
    if uploaded_file is not None and job_description:
        resume_text = extract_pdf_text(uploaded_file)
        
        c_resume = clean_text(resume_text)
        c_jd = clean_text(job_description)
        
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf = vectorizer.fit_transform([c_resume, c_jd])
        match_score = round(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100, 2)
        
        words_resume = set(c_resume.split())
        words_jd = set(c_jd.split())
        feature_names = set(vectorizer.get_feature_names_out())
        
        raw_missing = (words_jd - words_resume).intersection(feature_names)
        clean_missing = [w for w in raw_missing if w not in EXTRA_STOP_WORDS and len(w) > 2]
        
        st.markdown("---")
        st.subheader("🎯 ATS Compatibility Score")
        st.progress(int(match_score))
        st.write(f"### **{match_score}% Match**")
        
        if match_score >= 75:
            st.success("🌟 **Excellent Match!** Your resume matches most of the key requirements.")
        elif match_score >= 40:
            st.warning("⚠️ **Moderate Match.** Adding missing keywords will boost your score.")
        else:
            st.error("🚨 **Low Match.** Consider updating your skills section with relevant keywords from the JD.")
        
        st.markdown("---")
        if clean_missing:
            st.subheader("💡 Key Skills missing in your resume:")
            skills_html = "".join([f'<span style="background-color:#f0f2f6; color:#31333F; padding:6px 12px; margin:4px; border-radius:15px; display:inline-block; font-weight:bold;">{s.upper()}</span>' for s in clean_missing[:12]])
            st.markdown(skills_html, unsafe_allow_html=True)
        else:
            st.success("🎉 Outstanding! No major technical skill gaps found.")
    else:
        st.error("Please upload a PDF resume and paste a Job Description!")
