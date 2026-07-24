from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_resume(resume_text, job_description):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"""Analyze this resume against the job description and provide:
1. ATS Score (0-100)
2. Matching Skills
3. Missing Skills
4. Resume Improvements
5. Overall Feedback

Resume: {resume_text}
Job Description: {job_description}"""}]
    )
    return response.choices[0].message.content
