import streamlit as st

st.set_page_config(page_title="LearnMate - Course Details", page_icon="📚", layout="centered")

if "user_course" not in st.session_state:
    st.switch_page("main.py")
    st.stop()

course = st.session_state["user_course"]
name   = st.session_state.get("user_name_form", "Student")

COURSE_INFO = {
    "AIDS":             {"emoji": "📊", "full": "AI & Data Science",    "about": "Combines statistics, programming & ML to extract meaningful insights from large datasets. Master Python, Pandas & visualization tools.", "scope": "Data Analyst, Data Scientist, BI Analyst, Data Engineer across all industries.", "salary": "₹4–50 LPA"},
    "AIML":             {"emoji": "🤖", "full": "AI & Machine Learning","about": "Build systems that learn from data — recommendation engines, predictive models, deep learning & neural networks.", "scope": "ML Engineer, AI Researcher, NLP Engineer, Data Scientist at top product companies.", "salary": "₹5–60 LPA"},
    "UI/UX Design":     {"emoji": "🎨", "full": "UI/UX Design",         "about": "Create intuitive and visually appealing digital products. Covers user research, wireframing, prototyping & Figma.", "scope": "UI Designer, UX Researcher, Product Designer at startups & MNCs.", "salary": "₹3–35 LPA"},
    "Graphics Design":  {"emoji": "🖼️", "full": "Graphics Design",      "about": "Visual communication using typography, color, layout & illustration for branding, print and digital media.", "scope": "Brand Designer, Visual Designer, Art Director at agencies or freelance.", "salary": "₹2.5–25 LPA"},
    "Motion Graphics":  {"emoji": "🎬", "full": "Motion Graphics",      "about": "Combines graphic design with animation to create engaging videos, ads & digital content.", "scope": "Motion Designer, Video Editor at film, advertising, YouTube & OTT platforms.", "salary": "₹3–28 LPA"},
    "Cloud Computing":  {"emoji": "☁️", "full": "Cloud Computing",      "about": "Deploy, manage & scale applications on AWS, Azure & Google Cloud. Learn DevOps, containers & CI/CD.", "scope": "Cloud Engineer, DevOps Engineer, Cloud Architect, Solutions Architect.", "salary": "₹5–55 LPA"},
    "Digital Marketing":{"emoji": "📣", "full": "Digital Marketing",    "about": "SEO, social media, paid ads, email marketing & analytics to grow businesses online.", "scope": "SEO Analyst, Social Media Manager, Performance Marketer, Growth Hacker.", "salary": "₹2.5–25 LPA"},
    "AI with Python":   {"emoji": "🐍", "full": "AI with Python",       "about": "Python programming for AI applications — automation, chatbots, computer vision & NLP projects.", "scope": "Python Developer, AI Engineer, Automation Engineer, Backend Developer.", "salary": "₹4–50 LPA"},
}

info = COURSE_INFO.get(course, {})

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: linear-gradient(160deg, #f0fff4 0%, #e8f5e9 40%, #fff8e1 100%); }
.block-container { max-width: 480px !important; padding-top: 1rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style='background:linear-gradient(135deg,#1b5e20,#2e7d32);
border-radius:16px; padding:1.25rem; margin-bottom:1rem; text-align:center; color:white;'>
    <div style='font-size:2.5em;'>{info.get('emoji','🎓')}</div>
    <h2 style='margin:0.5rem 0 0.25rem; font-size:1.2em;'>{info.get('full', course)}</h2>
    <p style='margin:0; font-size:0.82em; opacity:0.85;'>Hello {name}! Here's everything about your selected course 👇</p>
</div>
<div style='background:#f0fff4; border:2px solid #2e7d32; border-radius:14px; padding:1rem; margin-bottom:0.85rem;'>
    <div style='color:#2e7d32; font-weight:700; font-size:0.85em; margin-bottom:6px;'>📖 About</div>
    <div style='color:#333; font-size:0.85em; line-height:1.6;'>{info.get('about','')}</div>
</div>
<div style='background:#fff8f0; border:2px solid #f5a623; border-radius:14px; padding:1rem; margin-bottom:0.85rem;'>
    <div style='color:#e65100; font-weight:700; font-size:0.85em; margin-bottom:6px;'>🚀 Career Scope</div>
    <div style='color:#333; font-size:0.85em; line-height:1.6;'>{info.get('scope','')}</div>
</div>
<div style='background:linear-gradient(135deg,#f5a623,#e65100);
border-radius:14px; padding:1rem; margin-bottom:1rem; color:white;
display:flex; justify-content:space-between; align-items:center;'>
    <span style='font-weight:700; font-size:0.85em;'>💰 Salary Range</span>
    <span style='font-weight:700; font-size:1em;'>{info.get('salary','')}</span>
</div>
""", unsafe_allow_html=True)

if st.button("🤖 Chat with AI →", use_container_width=True, type="primary"):
    st.switch_page("pages/chatbot.py")