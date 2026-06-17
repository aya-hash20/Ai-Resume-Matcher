import re
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s+#.]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_similarity(cv_text, job_text):
    documents = [clean_text(cv_text), clean_text(job_text)]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)


st.title("AI Resume Matcher")
st.write("Compare your CV with an internship offer.")

cv_text = st.text_area("Paste your CV text here", height=250)
job_text = st.text_area("Paste the internship offer here", height=250)

if st.button("Analyze"):
    if cv_text and job_text:
        score = calculate_similarity(cv_text, job_text)

        st.subheader("Compatibility Score")
        st.metric("Match", f"{score}%")

        if score < 40:
            st.warning("Your CV needs more relevant keywords for this offer.")
        elif score < 70:
            st.info("Your CV is partially aligned. You can improve it.")
        else:
            st.success("Your CV is well aligned with this offer.")
    else:
        st.error("Please paste both your CV and the internship offer.")
