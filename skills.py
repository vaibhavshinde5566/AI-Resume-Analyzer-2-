import spacy

#load english model
nlp = spacy.load('en_core_web_sm')

SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "nlp", "data analysis", "pandas", "numpy", "tensorflow", "pytorch",
    "excel", "power bi", "tableau", "communication", "leadership"
]

# job role mapping
JOB_ROLES = {
    "Data Scientist": ["python", "machine learning", "pandas", "numpy", "statistics"],
    "Data Analyst": ["excel", "sql", "power bi", "tableau", "data analysis"],
    "ML Engineer": ["python", "tensorflow", "pytorch", "deep learning"],
    "Backend Developer": ["java", "python", "sql", "apis"]
}

def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = set()
    
    for token in doc:
        if token in doc:
            if token.text in SKILLS_DB:
                found_skills.add(token.text)
                
    return list(found_skills)

def match_job_roles(skills):
    roles_scores = {}
    
    for role,role_skills in JOB_ROLES.items():
        match_count = len(set(skills) & set(role_skills))
        roles_scores[role] = match_count

    return sorted(roles_scores.items(), key=lambda x: x[1], reverse=True)