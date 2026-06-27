import streamlit as st
import re
from datetime import datetime
from google_form import submit_to_google_form

st.set_page_config(page_title="LearnMate", page_icon="🎓", layout="centered")

if "user_id" not in st.session_state:
    st.switch_page("main.py")
    st.stop()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: linear-gradient(160deg, #f0fff4 0%, #e8f5e9 40%, #fff8e1 100%); }
.block-container { max-width: 480px !important; padding-top: 1rem !important; }
div[data-testid="stTextInput"] input {
    border: 2px solid #f5a623 !important;
    border-radius: 8px !important;
    padding: 8px 10px !important;
}
div[data-testid="stSelectbox"] > div {
    border: 2px solid #f5a623 !important;
    border-radius: 8px !important;
}
div[data-testid="stButton"] > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
}
label { color: #555 !important; font-weight: 600 !important; font-size: 0.8em !important; }
</style>
""", unsafe_allow_html=True)

if "sidebar_open" not in st.session_state:
    st.session_state["sidebar_open"] = False

col1, col2 = st.columns([1, 10])
with col1:
    if st.button("❯" if not st.session_state["sidebar_open"] else "❮"):
        st.session_state["sidebar_open"] = not st.session_state["sidebar_open"]

if st.session_state["sidebar_open"]:
    st.markdown("""
    <div style='background:linear-gradient(160deg,#1b5e20,#2e7d32,#e65100);
    border-radius:16px; padding:1.5rem; margin-bottom:1rem; color:white;'>
        <h4 style='color:#a5d6a7; font-size:0.8em; letter-spacing:1px; margin-bottom:0.5rem;'>🎓 OUR COURSES</h4>
        <p style='font-size:0.82em; margin:2px 0;'>• AIDS</p>
        <p style='font-size:0.82em; margin:2px 0;'>• AIML</p>
        <p style='font-size:0.82em; margin:2px 0;'>• UI/UX Design</p>
        <p style='font-size:0.82em; margin:2px 0;'>• Graphics Design</p>
        <p style='font-size:0.82em; margin:2px 0;'>• Motion Graphics</p>
        <p style='font-size:0.82em; margin:2px 0;'>• Cloud Computing</p>
        <p style='font-size:0.82em; margin:2px 0;'>• Digital Marketing</p>
        <p style='font-size:0.82em; margin:2px 0;'>• AI with Python</p>
        <hr style='border-color:rgba(255,255,255,0.2); margin:0.75rem 0;'>
        <h4 style='color:#a5d6a7; font-size:0.8em; letter-spacing:1px; margin-bottom:0.5rem;'>📍 MAIN BRANCH</h4>
        <p style='font-size:0.82em;'>Second Floor, Aruna Avanthika Building,<br>280-3/4, B4, NSR Rd, Saibaba Colony,<br>Coimbatore, Tamil Nadu 641025</p>
        <hr style='border-color:rgba(255,255,255,0.2); margin:0.75rem 0;'>
        <h4 style='color:#a5d6a7; font-size:0.8em; letter-spacing:1px; margin-bottom:0.5rem;'>📞 CONTACT US</h4>
        <p style='font-size:0.82em;'>✉️ skilzlearn.gpc@gmail.com</p>
        <p style='font-size:0.82em;'>✉️ info@skilzlearn.com</p>
        <p style='font-size:0.82em;'>📱 +91 9787000027</p>
        <hr style='border-color:rgba(255,255,255,0.2); margin:0.75rem 0;'>
        <h4 style='color:#a5d6a7; font-size:0.8em; letter-spacing:1px; margin-bottom:0.5rem;'>🕐 OFFICE HOURS</h4>
        <p style='font-size:0.82em;'>Mon – Sat: 9:30 AM – 7:00 PM</p>
        <p style='font-size:0.82em;'>Closed on Sundays & Public Holidays</p>
    </div>
    """, unsafe_allow_html=True)

now = datetime.now()
st.markdown(f"""
<div style='background:linear-gradient(135deg,#f5a623,#e65100);
border-radius:16px; padding:1rem 1.25rem; margin-bottom:1rem; text-align:center; color:white;'>
    <h2 style='margin:0 0 0.25rem; font-size:1.1em; font-weight:700;'>👋 Welcome, {st.session_state.get("user_name", "Student")}!</h2>
    <p style='margin:0; font-size:0.78em; opacity:0.9;'>Please fill your details — our admissions team will contact you within 24 hours!</p>
</div>
<div style='background:linear-gradient(135deg,#2e7d32,#1b5e20);
color:white; border-radius:10px; padding:8px 14px;
font-size:0.82em; margin-bottom:1rem; font-weight:500;
display:flex; justify-content:space-between;'>
    <span>📅 {now.strftime("%A, %B %d %Y")}</span>
    <span>🕐 {now.strftime("%I:%M %p")}</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background:#f0fff4; border:2px solid #2e7d32; border-radius:14px;
padding:0.75rem 1rem; margin-bottom:0.5rem;'>
    <div style='color:#2e7d32; font-weight:700; font-size:0.85em;'>👤 Personal Details</div>
</div>
""", unsafe_allow_html=True)

name  = st.text_input("Full Name", placeholder="e.g. Rohit Sharma")
phone = st.text_input("Phone Number", placeholder="10-digit mobile number")
email = st.text_input("Email ID", placeholder="e.g. you@example.com")

st.markdown("""
<div style='background:#fff8f0; border:2px solid #f5a623; border-radius:14px;
padding:0.75rem 1rem; margin-top:0.5rem; margin-bottom:0.5rem;'>
    <div style='color:#e65100; font-weight:700; font-size:0.85em;'>🎓 Course Preference</div>
</div>
""", unsafe_allow_html=True)

status = st.selectbox("Current Status", ["-- Select --", "Student", "Working Professional", "Looking for Job"])
course = st.selectbox("Course Interested In", ["-- Select --", "AIDS", "AIML", "UI/UX Design", "Graphics Design", "Motion Graphics", "Cloud Computing", "Digital Marketing", "AI with Python"])

if st.button("🚀 Submit", use_container_width=True, type="primary"):
    if not name.strip():
        st.error("Name cannot be empty")
    elif not phone.strip().isdigit() or len(phone.strip()) != 10:
        st.error("Phone number must be 10 digits")
    elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email.strip()):
        st.error("Enter a valid Email ID")
    elif status == "-- Select --" or course == "-- Select --":
        st.error("All fields are mandatory")
    else:
        st.session_state["user_name_form"]  = name
        st.session_state["user_phone"]      = phone
        st.session_state["user_email_form"] = email
        st.session_state["user_status"]     = status
        st.session_state["user_course"]     = course
        submit_to_google_form(name, phone, email, status, course)
        st.success("✅ Registration completed! Our administration team will contact you soon.")
        st.switch_page("pages/course_details.py")