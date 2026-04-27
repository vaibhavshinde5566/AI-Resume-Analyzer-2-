import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Job description
job_desc = st.text_area("Enter Job Description")

# Button
if st.button("Analyze Resume"):
    
    if uploaded_file is not None and job_desc:
        
        with st.spinner("Analyzing..."):
            
            files = {"file": uploaded_file.getvalue()}
            data = {"job_desc": job_desc}
            
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files={"file": (uploaded_file.name, uploaded_file, "application/pdf")},
                data=data
            )
            
            result = response.json()
            
            # Display results
            st.subheader("📊 Analysis Results")
            
            # Skills
            st.write("### Skills Detected")
            st.write(result["skills"])
            
            # Similarity
            st.write("### Similarity Score")
            st.write(result["similarity_score"])
            
            # ATS
            st.write("### ATS Score")
            st.write(result["ats"]["ats_score"])
            
            st.write("### Missing Skills")
            st.write(result["ats"]["missing_skills"])
            
            # Role
            st.write("### Suggested Role")
            st.write(result["best_role"])
            
            # AI Suggestions
            st.write("### AI Suggestions")
            st.write(result["ai_suggestions"])
    
    else:
        st.warning("Please upload resume and enter job description")