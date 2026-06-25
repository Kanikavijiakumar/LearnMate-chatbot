import streamlit as st

st.set_page_config(page_title="Course Details", page_icon="📚", layout="wide")

# ✅ Guard: if user lands here without submitting, send them back
if "user_course" not in st.session_state:
    st.error("Please fill the registration form first.")
    st.switch_page("app.py")
    st.stop()

# Pull data from session
course = st.session_state["user_course"]
name   = st.session_state["user_name"]

# -------------------------------------------------------------------
# Course details dictionary — add/edit any course info here easily
# -------------------------------------------------------------------
COURSE_INFO = {
    "UI/UX": {
        "description": "UI/UX Design focuses on creating intuitive and visually appealing digital products. It covers user research, wireframing, prototyping, and testing.",
        "impact": "Every app and website needs a great user experience. UI/UX designers are in high demand as businesses compete to retain users through better design.",
        "scope": "Work in tech companies, startups, agencies, or freelance. Roles include UI Designer, UX Researcher, Product Designer, and Interaction Designer.",
        "salary": "Freshers: ₹3–6 LPA | Mid-level: ₹8–15 LPA | Senior: ₹18–35 LPA",
        "emoji": "🎨"
    },
    "AIML": {
        "description": "Artificial Intelligence & Machine Learning teaches you to build systems that learn from data — from recommendation engines to predictive models.",
        "impact": "AI is transforming every industry — healthcare, finance, retail, and more. It's one of the fastest-growing fields globally.",
        "scope": "Roles include ML Engineer, Data Scientist, AI Researcher, NLP Engineer. Opportunities in top product companies and research labs.",
        "salary": "Freshers: ₹5–10 LPA | Mid-level: ₹15–25 LPA | Senior: ₹30–60 LPA",
        "emoji": "🤖"
    },
    "AIDS": {
        "description": "AI & Data Science combines statistics, programming, and machine learning to extract meaningful insights from large datasets.",
        "impact": "Data is the new oil. Companies rely on data scientists to make strategic decisions, forecast trends, and improve products.",
        "scope": "Roles include Data Analyst, Data Scientist, Business Intelligence Analyst, and Data Engineer across all industries.",
        "salary": "Freshers: ₹4–8 LPA | Mid-level: ₹12–22 LPA | Senior: ₹25–50 LPA",
        "emoji": "📊"
    },
    "Full Stack": {
        "description": "Full Stack Development covers both front-end (what users see) and back-end (server/database) development using modern frameworks.",
        "impact": "Every digital product needs developers. Full stack devs are versatile and can build complete applications independently.",
        "scope": "Work as Full Stack Developer, Software Engineer, or Technical Lead at startups, MNCs, or as a freelancer.",
        "salary": "Freshers: ₹4–8 LPA | Mid-level: ₹10–20 LPA | Senior: ₹22–45 LPA",
        "emoji": "💻"
    },
    "Cloud": {
        "description": "Cloud Computing teaches you to deploy, manage, and scale applications on platforms like AWS, Azure, and Google Cloud.",
        "impact": "90% of enterprises are moving to cloud. Cloud professionals are among the highest-paid in the tech industry.",
        "scope": "Roles include Cloud Engineer, DevOps Engineer, Cloud Architect, and Solutions Architect.",
        "salary": "Freshers: ₹5–9 LPA | Mid-level: ₹12–25 LPA | Senior: ₹28–55 LPA",
        "emoji": "☁️"
    },
    "Graphics Design": {
        "description": "Graphic Design covers visual communication using typography, color, layout, and illustration for branding, print, and digital media.",
        "impact": "Every brand needs a visual identity. Graphic designers shape how companies communicate with the world.",
        "scope": "Work in agencies, media companies, or freelance. Roles include Brand Designer, Visual Designer, and Art Director.",
        "salary": "Freshers: ₹2.5–5 LPA | Mid-level: ₹6–12 LPA | Senior: ₹15–25 LPA",
        "emoji": "🖼️"
    },
    "Motion Graphics": {
        "description": "Motion Graphics combines graphic design with animation to create engaging videos, ads, title sequences, and digital content.",
        "impact": "Video content dominates the internet. Motion designers are in huge demand for social media, OTT, and advertising.",
        "scope": "Work in film, advertising, YouTube, OTT platforms, or freelance. Roles include Motion Designer and Video Editor.",
        "salary": "Freshers: ₹3–6 LPA | Mid-level: ₹7–14 LPA | Senior: ₹16–28 LPA",
        "emoji": "🎬"
    },
    "AI with Python": {
        "description": "This course teaches Python programming specifically for AI applications — automation, chatbots, computer vision, and NLP projects.",
        "impact": "Python is the #1 language for AI. Knowing Python + AI opens doors to some of the most exciting jobs in tech today.",
        "scope": "Roles include Python Developer, AI Engineer, Automation Engineer, and Backend Developer.",
        "salary": "Freshers: ₹4–8 LPA | Mid-level: ₹12–22 LPA | Senior: ₹25–50 LPA",
        "emoji": "🐍"
    },
    "Digital Marketing": {
        "description": "Digital Marketing covers SEO, social media, paid ads, email marketing, and analytics to grow businesses online.",
        "impact": "Every business needs an online presence. Digital marketers drive growth, leads, and revenue in the digital age.",
        "scope": "Roles include SEO Analyst, Social Media Manager, Performance Marketer, and Growth Hacker.",
        "salary": "Freshers: ₹2.5–5 LPA | Mid-level: ₹6–12 LPA | Senior: ₹14–25 LPA",
        "emoji": "📣"
    }
}

# Get info for selected course
info = COURSE_INFO.get(course, None)

# -------------------------------------------------------------------
# Display the course details page
# -------------------------------------------------------------------
st.markdown(f"<h1 style='text-align:center;'>{info['emoji']} {course}</h1>", unsafe_allow_html=True)
st.markdown(f"### Hello {name}! Here's everything about your selected course 👇")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📖 What is this Course?")
    st.info(info["description"])

    st.markdown("### 🌍 Impact Nowadays")
    st.success(info["impact"])

with col2:
    st.markdown("### 🚀 Scope & Career")
    st.warning(info["scope"])

    st.markdown("### 💰 Salary Package")
    st.error(info["salary"])  # Red color makes salary stand out!

st.divider()

# ✅ The button to open AI Chatbot
st.markdown("### 💬 Want to know more? Chat with our AI!")
st.write("Click the button below to open the AI Chatbot and get your questions answered instantly.")

if st.button("🤖 Chat with AI", use_container_width=True):
    st.switch_page("pages/chatbot.py")