from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_hr_questions(experience_level, company_type):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Generate 10 common HR interview questions for a {experience_level} candidate applying to a {company_type} company. Include tell me about yourself, strengths/weaknesses, situational, career goals questions. Format as numbered list."}]
    )
    return response.choices[0].message.content

def get_hr_answer(question, candidate_background):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Generate a perfect HR interview answer for:\nQuestion: {question}\nCandidate Background: {candidate_background}\n\nProvide:\n1. Perfect Answer\n2. Key points to remember\n3. What NOT to say"}]
    )
    return response.choices[0].message.content
