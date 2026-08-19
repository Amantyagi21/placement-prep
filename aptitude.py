from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_aptitude_questions(topic, num_questions=5):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"Generate {num_questions} aptitude questions on {topic}. Format each as:\nQ. Question\nA) option\nB) option\nC) option\nD) option\nAnswer: X\nExplanation: explanation\n\nMake them similar to TCS, Infosys placement tests."}]
    )
    return response.choices[0].message.content
