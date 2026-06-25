from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(question: str, course: str = "") -> str:
    """
    Send a question to Groq AI and get a response.
    Includes course context so the bot gives relevant answers.
    """

    # ✅ FIX: System prompt gives the AI context about who it is
    system_prompt = f"""You are LearnMate, a helpful admission counselor chatbot 
for an educational institute. The student is interested in the '{course}' course.
Give clear, friendly, and encouraging answers. Focus on:
- Course details, syllabus, and career scope
- Salary packages and job opportunities  
- Comparison with other courses if asked
- Admission process and eligibility
Keep answers concise and easy to understand for students."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": question}
        ]
    )

    return response.choices[0].message.content