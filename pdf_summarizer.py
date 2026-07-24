from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_pdf(pdf_text, summary_type):
    prompts = {
        "Brief Summary": f"Summarize in 5-6 bullet points:\n{pdf_text[:3000]}",
        "Detailed Summary": f"Give detailed summary with key concepts:\n{pdf_text[:3000]}",
        "Key Points": f"Extract most important key points:\n{pdf_text[:3000]}",
        "Study Notes": f"Convert into easy study notes with headings:\n{pdf_text[:3000]}"
    }
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompts[summary_type]}]
    )
    return response.choices[0].message.content
