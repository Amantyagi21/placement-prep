from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_questions(job_role, num_questions=5):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"Generate {num_questions} interview questions for {job_role} role. Mix of technical and behavioral. Format as numbered list."}]
    )
    return response.choices[0].message.content

def evaluate_answer(question, answer, job_role):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"Evaluate this interview answer:\nJob Role: {job_role}\nQuestion: {question}\nAnswer: {answer}\n\nProvide:\n1. Score (out of 10)\n2. What was good\n3. What was missing\n4. Better answer suggestion"}]
    )
    return response.choices[0].message.content
