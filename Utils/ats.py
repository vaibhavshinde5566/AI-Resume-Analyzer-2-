from Utils.skills import extract_skills, JOB_ROLES

def calculate_ats_score(resume_text, job_desc):
    
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)
    
    # convert to sets
    resume_set = set(resume_skills)
    job_set = set(job_skills)
    
    # matched skills
    matched = resume_set & job_set
    
    # missing skills (gap)
    missing = job_set - resume_set
    
    # ATS score calculation
    if len(job_set) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_set)) * 100
    
    return {
        "ats_score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }


def suggest_job_role(resume_text):
    
    resume_skills = extract_skills(resume_text)
    role_scores = {}
    
    for role, skills in JOB_ROLES.items():
        match = len(set(resume_skills) & set(skills))
        role_scores[role] = match
    
    best_role = max(role_scores, key=role_scores.get)
    
    return best_role, role_scores