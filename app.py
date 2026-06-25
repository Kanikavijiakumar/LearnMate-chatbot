import streamlit as st
from PIL import Image
import re
import time
from google_form import submit_to_google_form

st.set_page_config(
    page_title="LearnMate - Admission Portal",
    page_icon="🎓",
    layout="centered"
)

# ── CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
/* Light green background */
.stApp, .main, section.main, .block-container {
    background-color: #e8f5e9 !important;
    background-image: linear-gradient(135deg, #e8f5e9 0%, #f1f8f1 50%, #e0f2e9 100%) !important;
}
body {
    background-color: #e8f5e9 !important;
}

/* Title */
.portal-title {
    font-size: 2.2em;
    font-weight: 800;
    color: #1a1a2e;
    margin-bottom: 4px;
}
.portal-sub {
    color: #f5a623;
    font-weight: 600;
    font-size: 1em;
    margin-bottom: 20px;
}

/* Stats cards */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 20px 0 28px 0;
}
.stat-box {
    border-radius: 14px;
    padding: 18px 10px;
    text-align: center;
    color: white;
    font-weight: 700;
}
.stat-box.green  { background: #2e7d32; }
.stat-box.orange { background: #e65100; }
.stat-box.teal   { background: #00695c; }
.stat-box.purple { background: #6a1b9a; }
.stat-num  { font-size: 1.8em; font-weight: 800; }
.stat-text { font-size: 0.75em; margin-top: 4px; opacity: 0.9; }

/* Welcome strip */
.welcome-strip {
    background: #fff8e1;
    border: 1.5px solid #ffe082;
    border-radius: 12px;
    padding: 14px 18px;
    font-size: 0.97em;
    color: #5d4037;
    margin-bottom: 20px;
}

/* Section titles */
.section-title {
    font-size: 1.05em;
    font-weight: 700;
    color: #1a1a2e;
    margin-bottom: 2px;
}
.section-sub {
    font-size: 0.82em;
    color: #888;
    margin-bottom: 16px;
}

/* Inputs */
.stTextInput > div > div > input {
    border-radius: 8px !important;
    border: 1.5px solid #c8e6c9 !important;
    padding: 11px 14px !important;
    background: white !important;
    font-size: 0.97em !important;
}
.stTextInput > div > div > input:focus {
    border: 1.5px solid #2e7d32 !important;
    box-shadow: 0 0 0 3px rgba(46,125,50,0.1) !important;
}
.stSelectbox > div > div {
    border-radius: 8px !important;
    border: 1.5px solid #c8e6c9 !important;
    background: white !important;
}

/* Submit button - centered */
div.stButton {
    display: flex !important;
    justify-content: center !important;
}
div.stButton > button {
    background: linear-gradient(135deg, #2e7d32, #1b5e20) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 80px !important;
    font-size: 1.1em !important;
    font-weight: 700 !important;
    width: auto !important;
    white-space: nowrap !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 16px rgba(46,125,50,0.3) !important;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #1b5e20, #2e7d32) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(46,125,50,0.4) !important;
}

/* Footer */
.footer-note {
    text-align: center;
    color: #aaa;
    font-size: 0.82em;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ── Logo ─────────────────────────────────────────────────────
logo = Image.open("logo.png")
st.image(logo, width=220)

# ── Title ─────────────────────────────────────────────────────
st.markdown("""
<div class="portal-title">Admission Portal</div>
<div class="portal-sub">🌟 Building Bridges to Success — Start Your Journey Today!</div>
""", unsafe_allow_html=True)

# ── Stats Cards ───────────────────────────────────────────────
st.markdown("""
<div class="stats-grid">
    <div class="stat-box green">
        <div class="stat-num">9+</div>
        <div class="stat-text">Courses<br>Available</div>
    </div>
    <div class="stat-box orange">
        <div class="stat-num">500+</div>
        <div class="stat-text">Students<br>Enrolled</div>
    </div>
    <div class="stat-box teal">
        <div class="stat-num">95%</div>
        <div class="stat-text">Placement<br>Rate</div>
    </div>
    <div class="stat-box purple">
        <div class="stat-num">24h</div>
        <div class="stat-text">Response<br>Time</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Welcome Strip ─────────────────────────────────────────────
st.markdown("""
<div class="welcome-strip">
    👋 Welcome! Please fill in your details below —
    our admissions team will contact you within 24 hours!
</div>
""", unsafe_allow_html=True)

# ── Personal Details ──────────────────────────────────────────
st.markdown('<div class="section-title">👤 Personal Details</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">All fields are mandatory. Your data is safe with us 🔒</div>', unsafe_allow_html=True)

name  = st.text_input("Full Name", placeholder="Enter your full name")
phone = st.text_input("Phone Number", placeholder="10-digit mobile number")
email = st.text_input("Email ID", placeholder="example@email.com")

# ── Course Preference ─────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">🎓 Course Preference</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Tell us what you want to learn and where you are now</div>', unsafe_allow_html=True)

status = st.selectbox("Current Status", [
    "Select", "Student", "Working Professional", "Looking for Job"
])
course = st.selectbox("Course Interested In", [
    "Select", "UI/UX", "AIML", "AIDS", "Cloud",
    "Graphics Design", "Motion Graphics", "Full Stack",
    "AI with Python", "Digital Marketing"
])

# ── Submit Button ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
submitted = st.button("🚀 Submit")

if submitted:
    if name.strip() == "":
        st.error("❌ Name cannot be empty")
    elif not phone.isdigit() or len(phone) != 10:
        st.error("❌ Phone number must be exactly 10 digits")
    elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        st.error("❌ Enter a valid Email ID")
    elif status == "Select" or course == "Select":
        st.error("❌ All fields are mandatory")
    else:
        st.session_state["user_name"]   = name
        st.session_state["user_phone"]  = phone
        st.session_state["user_email"]  = email
        st.session_state["user_status"] = status
        st.session_state["user_course"] = course

        st.markdown("**⏳ Submitting your details...**")
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.015)
            bar.progress(i + 1)

        submit_to_google_form(name, phone, email, status, course)

        st.success("✅ Thank you {}! Our team will contact you soon 🎉".format(name))
        time.sleep(1.5)
        st.switch_page("pages/course_details.py")

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class="footer-note">
    © 2026 LearnMate | Powered by SkilzLearn 🎓
</div>
""", unsafe_allow_html=True)