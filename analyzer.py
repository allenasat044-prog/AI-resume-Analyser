import re

SKILLS = [
    "python", "java", "c++", "c", "javascript", "html", "css",
    "react", "node", "sql", "mongodb", "machine learning",
    "data analysis", "excel", "git", "linux"
]

def analyze_resume(text):
    text_lower = text.lower()

    score = 0
    feedback = []
    found_skills = []

    # ---- Skills ----
    for skill in SKILLS:
        if skill in text_lower:
            found_skills.append(skill)

    if len(found_skills) >= 5:
        score += 25
    elif len(found_skills) >= 2:
        score += 15
    else:
        feedback.append("Add more relevant technical skills")

    # ---- Sections ----
    if "experience" in text_lower:
        score += 20
    else:
        feedback.append("Add an Experience section")

    if "project" in text_lower:
        score += 20
    else:
        feedback.append("Add a Projects section")

    if "education" in text_lower:
        score += 10
    else:
        feedback.append("Add an Education section")

    # ---- Length ----
    word_count = len(text.split())
    if 300 <= word_count <= 800:
        score += 15
    else:
        feedback.append("Keep resume length between 300-800 words")

    # ---- Action Words ----
    action_words = ["developed", "built", "created", "designed", "implemented"]
    if any(word in text_lower for word in action_words):
        score += 10
    else:
        feedback.append("Use strong action words like 'developed', 'built'")

    # ---- Email ----
    if re.search(r'\S+@\S+', text):
        score += 5
    else:
        feedback.append("Add a professional email address")

    # ---- Final Output ----
    result = f"""
AI Resume Analysis (Offline)

Score: {score}/100

Skills Found:
{', '.join(found_skills) if found_skills else 'None'}

Suggestions:
"""

    if feedback:
        for f in feedback:
            result += f"- {f}\n"
    else:
        result += "Excellent resume! Minor improvements only."

    return result