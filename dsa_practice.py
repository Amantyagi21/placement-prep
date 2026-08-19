from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_dsa_question(topic, difficulty):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"Generate a DSA problem on {topic} with {difficulty} difficulty.\n\nFormat:\nProblem Title:\nProblem Statement:\nExample Input:\nExample Output:\nHint:\nSolution Approach:"}]
    )
    return response.choices[0].message.content

def check_solution(problem, user_solution):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"Review this DSA solution:\nProblem: {problem}\nSolution: {user_solution}\n\nProvide:\n1. Is solution correct?\n2. Time Complexity\n3. Space Complexity\n4. What is good\n5. What can be improved\n6. Optimal solution"}]
    )
    return response.choices[0].message.content
