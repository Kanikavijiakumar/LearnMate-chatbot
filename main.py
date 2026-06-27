import streamlit as st
from supabase import create_client
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

st.set_page_config(page_title="LearnMate Login", page_icon="🎓", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: linear-gradient(160deg, #f0fff4 0%, #e8f5e9 40%, #fff8e1 100%); }
.block-container { max-width: 420px !important; padding-top: 2rem !important; }
div[data-testid="stTextInput"] input {
    border: 2px solid #f5a623 !important;
    border-radius: 10px !important;
    padding: 10px 12px !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #2e7d32 !important;
    box-shadow: 0 0 0 3px rgba(46,125,50,0.15) !important;
}
div[data-testid="stButton"] > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 10px !important;
}
label { color: #2e7d32 !important; font-weight: 600 !important; font-size: 0.85em !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-bottom:1.5rem; padding-top:0.5rem;'>
    <span style='font-size:2.2em; font-weight:900; color:#2e7d32;'>Learn</span><span style='font-size:2.2em; font-weight:900; color:#f5a623;'>Mate</span>
    <div style='color:#777; font-size:0.82em; margin-top:2px;'>Building Bridges to Success..</div>
</div>
""", unsafe_allow_html=True)

if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

col1, col2 = st.columns(2)
with col1:
    if st.button("Sign In", use_container_width=True,
                 type="primary" if st.session_state["auth_mode"] == "login" else "secondary"):
        st.session_state["auth_mode"] = "login"
        st.rerun()
with col2:
    if st.button("Create Account", use_container_width=True,
                 type="primary" if st.session_state["auth_mode"] == "signup" else "secondary"):
        st.session_state["auth_mode"] = "signup"
        st.rerun()

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

if st.session_state["auth_mode"] == "login":
    st.markdown("<h3 style='color:#2e7d32; margin:0.5rem 0 0.1rem;'>Welcome back 👋</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; font-size:0.82em; margin-bottom:1rem;'>Sign in to your account to continue</p>", unsafe_allow_html=True)

    login_email = st.text_input("Email address", placeholder="you@example.com", key="login_email")
    login_pass  = st.text_input("Password", type="password", placeholder="Enter your password", key="login_pass")

    st.markdown("<div style='text-align:right; margin-top:-10px; margin-bottom:14px;'><a href='#' style='color:#f5a623; font-size:0.8em; font-weight:600; text-decoration:none;'>Forgot password?</a></div>", unsafe_allow_html=True)

    if st.button("Sign In →", use_container_width=True, type="primary", key="login_btn"):
        if not login_email.strip() or not login_pass.strip():
            st.error("Please fill all fields!")
        else:
            try:
                result = supabase.table("users").select("*").eq("email", login_email).execute()
                if result.data:
                    user = result.data[0]
                    if bcrypt.checkpw(login_pass.encode(), user["password"].encode()):
                        st.session_state["user_id"]    = user["id"]
                        st.session_state["user_email"] = user["email"]
                        st.session_state["user_name"]  = user.get("name", login_email)
                        st.success("✅ Login successful!")
                        st.switch_page("pages/home.py")
                    else:
                        st.error("❌ Wrong password!")
                else:
                    st.error("❌ Email not found! Please create an account.")
            except Exception as e:
                st.error(f"Error: {e}")

    st.markdown("<div style='text-align:center; margin-top:1rem; font-size:0.8em; color:#888;'>New here? Click <b>Create Account</b> above!</div>", unsafe_allow_html=True)

else:
    st.markdown("<h3 style='color:#2e7d32; margin:0.5rem 0 0.1rem;'>Create account 🎓</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; font-size:0.82em; margin-bottom:1rem;'>Sign up to get started with LearnMate</p>", unsafe_allow_html=True)

    signup_name  = st.text_input("Full Name", placeholder="e.g. Kanika", key="signup_name")
    signup_email = st.text_input("Email address", placeholder="you@example.com", key="signup_email")
    signup_pass  = st.text_input("Password", type="password", placeholder="Create a password (min 6 chars)", key="signup_pass")
    confirm_pass = st.text_input("Confirm Password", type="password", placeholder="Repeat your password", key="confirm_pass")

    if st.button("Create Account →", use_container_width=True, type="primary", key="signup_btn"):
        if not signup_name.strip() or not signup_email.strip() or not signup_pass.strip() or not confirm_pass.strip():
            st.error("Please fill all fields!")
        elif signup_pass != confirm_pass:
            st.error("❌ Passwords don't match!")
        elif len(signup_pass) < 6:
            st.error("❌ Password must be at least 6 characters!")
        else:
            try:
                existing = supabase.table("users").select("*").eq("email", signup_email).execute()
                if existing.data:
                    st.error("❌ Email already exists! Please sign in.")
                else:
                    hashed = bcrypt.hashpw(signup_pass.encode(), bcrypt.gensalt()).decode()
                    supabase.table("users").insert({
                        "email": signup_email,
                        "password": hashed,
                        "name": signup_name
                    }).execute()
                    st.success("✅ Account created! Please sign in.")
                    st.session_state["auth_mode"] = "login"
                    st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

    st.markdown("<div style='text-align:center; margin-top:1rem; font-size:0.8em; color:#888;'>Already have an account? Click <b>Sign In</b> above!</div>", unsafe_allow_html=True)