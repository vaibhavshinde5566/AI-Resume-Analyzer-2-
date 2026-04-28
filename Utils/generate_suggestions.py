from Utils.skills import extract_skills

def generate_suggestions(resume_text, job_desc, missing_skills):
    
    suggestions = []

    # Suggest adding missing skills
    if missing_skills:
        suggestions.append(
            f"Consider adding these skills to your resume: {', '.join(missing_skills)}"
        )

    # Suggest improving summary
    if "objective" not in resume_text.lower() and "summary" not in resume_text.lower():
        suggestions.append(
            "Add a strong professional summary or objective at the top of your resume."
        )

    # Suggest action verbs
    if "developed" not in resume_text.lower():
        suggestions.append(
            "Use action verbs like 'developed', 'implemented', 'designed' to describe your work."
        )

    # Suggest project section
    if "project" not in resume_text.lower():
        suggestions.append(
            "Include a projects section highlighting your practical work."
        )

    # Suggest metrics
    if "%" not in resume_text:
        suggestions.append(
            "Add measurable achievements (e.g., improved accuracy by 20%)."
        )

    return suggestions


#======================================= AI suggestons ========

import os
from groq import Groq

client = Groq(api_key="your groq api key")


def generate_ai_suggestions_llm(resume_text, job_desc, missing_skills):

    prompt = f"""
    You are an expert ATS resume reviewer.

    Analyze the resume and job description.

    Resume:
    {resume_text[:2000]}

    Job Description:
    {job_desc}

    Missing Skills:
    {', '.join(missing_skills)}

    Give:
    1. Key improvements
    2. Missing keywords to add
    3. Better phrasing suggestions
    4. ATS optimization tips

    Keep it concise and practical.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # best Groq model
        messages=[
            {"role": "system", "content": "You are a professional resume reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        timeout=10
    )

    return response.choices[0].message.content