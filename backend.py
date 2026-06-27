from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

ALLOWED_TOPICS = [
    "aids", "ai & data science", "aiml", "ui/ux", "graphics design",
    "motion graphics", "cloud computing", "digital marketing", "ai with python",
    "python", "machine learning", "artificial intelligence", "data science",
    "deep learning", "neural network", "programming", "coding", "software",
    "developer", "database", "aws", "azure", "google cloud", "devops",
    "figma", "adobe", "photoshop", "illustrator", "after effects",
    "seo", "social media", "web", "frontend", "backend", "algorithm",
    "computer", "technology", "tech", "course", "salary", "career",
    "scope", "job", "placement", "skill", "learn", "training",
    "focus", "topics", "syllabus", "curriculum", "modules", "subjects",
    "what", "which", "how", "tell", "explain", "define", "describe"
]

def is_tech_question(question: str) -> bool:
    q = question.lower()
    return any(topic in q for topic in ALLOWED_TOPICS)

def get_ai_response(question: str, course: str = "") -> str:
    if not is_tech_question(question):
        return "Sorry, I don't know about that! 🙏 Please ask me technology or course-related questions only."

    system_prompt = f"""You are LearnMate AI, a helpful admission counselor chatbot for LearnMate educational institute.
The student is currently interested in the course: '{course}'.

LearnMate offers EXACTLY these 8 courses:
1. AIDS = AI & Data Science (NOT Acquired Immunodeficiency Syndrome — never mention the disease)
2. AIML = Artificial Intelligence & Machine Learning
3. UI/UX Design = User Interface and User Experience Design
4. Graphics Design = Visual communication, branding, typography
5. Motion Graphics = Animation, video editing, digital content
6. Cloud Computing = AWS, Azure, Google Cloud, DevOps
7. Digital Marketing = SEO, social media, paid ads, analytics
8. AI with Python = Python programming, automation, chatbots, computer vision

STRICT RULES:
- Answer ONLY about these 8 courses and related technology topics
- AIDS always means "AI & Data Science" course — NEVER mention any disease
- If asked about focus areas, syllabus, topics, or curriculum of a course — answer specifically about that course
- Keep answers friendly, concise, encouraging and relevant
- If truly unrelated to technology or these courses, say: "Sorry, I don't know about that! Please ask me technology or course-related questions only."
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}. Please try again!"