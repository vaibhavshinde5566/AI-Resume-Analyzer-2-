"""from Utils.skills import extract_skills, match_job_roles
# cheak skilss file
text = "I have experience in Python, machine learning, pandas and numpy"

skills = extract_skills(text)
print("Skills:", skills)

roles = match_job_roles(skills)
print("Roles:", roles)"""

#==========================Check similasrity file=========================================
"""
from Utils.parser import extract_text_from_pdf
from Utils.similarity import calculate_similarity

resume_text = extract_text_from_pdf("resume.pdf")

job_desc = """
#Python machine learning data scientist pandas numpy
"""
print("------JOB DESC------")

print("------RESUME SAMPLE------")
print(resume_text[:300])  # first 300 chars

score = calculate_similarity(resume_text, job_desc)
print("Similarity Score:", score)

score = calculate_similarity(resume_text, job_desc)

print("Similarity Score:", score)
"""

#============================= cheack ats file=============
"""
from Utils.parser import extract_text_from_pdf
from Utils.ats import calculate_ats_score, suggest_job_role

resume_text = extract_text_from_pdf("resume.pdf")

#job_desc =
#Looking for a Data Scientist with Python, machine learning,
#pandas, numpy, and data analysis skills.


ats_result = calculate_ats_score(resume_text, job_desc)
print(ats_result)

role, scores = suggest_job_role(resume_text)
print("Best Role:", role)
print("All Role Scores:", scores)
"""
#===============================cheack ai_suggestions.py
from Utils.parser import extract_text_from_pdf
from Utils.ats import calculate_ats_score
from Utils.generate_suggestions import generate_ai_suggestions_llm

resume_text = extract_text_from_pdf("resume.pdf")

job_desc = """
Looking for Python, machine learning, pandas, numpy, and data analysis skills.
"""

ats = calculate_ats_score(resume_text, job_desc)

output = generate_ai_suggestions_llm(
    resume_text,
    job_desc,
    ats["missing_skills"]
)

print(output)