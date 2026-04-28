"""This file will:

Convert text → vectors
Calculate similarity between:
Resume
Job Description"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_desc):

    def preprocess(text):
        return text.lower().replace("\n", " ")

    resume_text = preprocess(resume_text)[:2000]
    job_desc = preprocess(job_desc)

    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1,2),
        max_features=5000
    )

    vectors = vectorizer.fit_transform([resume_text, job_desc])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return float(similarity[0][0])