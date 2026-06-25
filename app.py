import streamlit as st
from PIL import Image
import re
from google_form import submit_to_google_form

# Page settings
st.set_page_config(
    page_title="LearnMate Chatbot",
    page_icon="🎓",
    layout="wide"
)

# Logo
logo = Image.open("logo.png")
st.image(logo, width=350)

# Title
st.markdown(
    "<h1 style='text-align:center;'>LearnMate Chatbot</h1>",
    unsafe_allow_html=True
)

st.write("Welcome! Please fill in your details.")

# Inputs
name   = st.text_input("Name")
phone  = st.text_input("Phone Number")
email  = st.text_input("Email ID")

status = st.selectbox(
    "Current Status",
    ["Select", "Student", "Working Professional", "Looking for Job"]
)

course = st.selectbox(
    "Course",
    ["Select", "UI/UX", "AIML", "AIDS", "Cloud",
     "Graphics Design", "Motion Graphics", "Full Stack",
     "AI with Python", "Digital Marketing"]
)

# Submit button
if st.button("Submit"):

    if name.strip() == "":
        st.error("Name cannot be empty")

    elif not phone.isdigit() or len(phone) != 10:
        st.error("Phone number must contain exactly 10 digits")

    elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        st.error("Enter a valid Email ID")

    elif status == "Select" or course == "Select":
        st.error("All fields are mandatory")

    else:
        # ✅ FIX: Save user data to session_state so other pages can use it
        st.session_state["user_name"]   = name
        st.session_state["user_phone"]  = phone
        st.session_state["user_email"]  = email
        st.session_state["user_status"] = status
        st.session_state["user_course"] = course

        # Submit to Google Form
        status_code = submit_to_google_form(name, phone, email, status, course)

        # ✅ FIX: Check properly — Google Forms returns 200 on success
        if status_code == 200:
            st.success("✅ Thank you for registering. Our administration team will contact you soon.")
            st.switch_page("pages/course_details.py")  # Go to course details page first
        else:
            st.warning("⚠️ Form submitted locally but Google Form upload failed. Continuing...")
            st.switch_page("pages/course_details.py")