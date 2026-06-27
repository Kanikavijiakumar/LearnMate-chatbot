import streamlit as st
from backend import get_ai_response
from supabase import create_client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

st.set_page_config(page_title="LearnMate Chatbot", page_icon="🤖", layout="centered")

if "user_course" not in st.session_state:
    st.switch_page("main.py")
    st.stop()

course  = st.session_state["user_course"]
name    = st.session_state.get("user_name_form", "Student")
user_id = st.session_state.get("user_id", None)

if "show_history" not in st.session_state:
    st.session_state["show_history"] = False

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    if user_id:
        try:
            result = supabase.table("chat_history")\
                .select("*")\
                .eq("user_id", user_id)\
                .eq("course", course)\
                .order("timestamp")\
                .execute()
            for row in result.data:
                st.session_state["chat_history"].append({
                    "role": row["role"],
                    "content": row["message"]
                })
        except:
            pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: linear-gradient(160deg, #f0fff4 0%, #e8f5e9 40%, #fff8e1 100%); }
.block-container { max-width: 520px !important; padding-top: 1rem !important; }
div[data-testid="stButton"] > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────
st.markdown(f"""
<div style='background:linear-gradient(135deg,#1b5e20,#2e7d32);
border-radius:16px; padding:1rem 1.25rem; margin-bottom:0.5rem;
display:flex; align-items:center; gap:12px;'>
    <div style='width:44px;height:44px;background:white;border-radius:50%;
    display:flex;align-items:center;justify-content:center;font-size:1.4em;flex-shrink:0;'>🤖</div>
    <div style='flex:1;'>
        <div style='color:white;font-weight:700;font-size:0.95em;'>✨ LearnMate AI</div>
        <div style='color:#a5d6a7;font-size:0.75em;'>
        <span style='width:8px;height:8px;background:#69f0ae;border-radius:50%;
        display:inline-block;margin-right:5px;'></span>
        Online — Hi {name}! Ask me about {course}!</div>
    </div>
</div>
<div style='background:#fff8e1;border-left:4px solid #f5a623;padding:8px 14px;
font-size:0.78em;color:#e65100;font-weight:600;margin-bottom:0.75rem;border-radius:0 8px 8px 0;'>
    ⚠️ Technology & course-related questions only!
</div>
""", unsafe_allow_html=True)

# ── TOP BUTTONS ───────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Back", use_container_width=True):
        st.switch_page("pages/course_details.py")
with col2:
    hist_label = "❌ Close" if st.session_state["show_history"] else "🕐 History"
    if st.button(hist_label, use_container_width=True):
        st.session_state["show_history"] = not st.session_state["show_history"]
        st.rerun()
with col3:
    if st.button("💬 New Chat", use_container_width=True):
        st.session_state["chat_history"] = []
        st.rerun()

st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

# ── HISTORY PANEL ─────────────────────────────────────
if st.session_state["show_history"]:
    st.markdown(f"""
    <div style='background:linear-gradient(160deg,#1b5e20,#2e7d32);
    border-radius:16px; padding:1.25rem; margin-bottom:1rem;'>
        <div style='color:#a5d6a7; font-weight:700; font-size:0.85em;
        letter-spacing:1px; margin-bottom:1rem;'>🕐 {course} — CHAT HISTORY</div>
    """, unsafe_allow_html=True)

    if user_id:
        try:
            result = supabase.table("chat_history")\
                .select("*")\
                .eq("user_id", user_id)\
                .eq("course", course)\
                .order("timestamp")\
                .execute()
            all_history = result.data
        except:
            all_history = []
    else:
        all_history = [{"role": m["role"], "message": m["content"]}
                       for m in st.session_state["chat_history"]]

    if all_history:
        for row in all_history:
            role  = row.get("role", "user")
            msg   = row.get("message", row.get("content", ""))
            icon  = "👤" if role == "user" else "🤖"
            label = "You" if role == "user" else "LearnMate AI"
            bg    = "rgba(255,255,255,0.18)" if role == "user" else "rgba(0,0,0,0.15)"
            st.markdown(f"""
            <div style='background:{bg}; border-radius:10px; padding:8px 12px;
            margin-bottom:8px; font-size:0.8em;'>
                <div style='font-weight:700; color:#a5d6a7; margin-bottom:3px;'>{icon} {label}</div>
                <div style='color:white; line-height:1.5;'>{msg[:150]}{"..." if len(msg) > 150 else ""}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color:#a5d6a7; font-size:0.85em; text-align:center;'>No chat history for {course} yet!</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ── CHAT MESSAGES ─────────────────────────────────────
else:
    if not st.session_state["chat_history"]:
        st.markdown(f"""
        <div style='text-align:center; padding:2rem; color:#888;'>
            <div style='font-size:2.5em; margin-bottom:0.5rem;'>🤖</div>
            <div style='font-size:0.85em; font-weight:500;'>Hi {name}! Ask me anything about <b>{course}</b> or technology!</div>
        </div>
        """, unsafe_allow_html=True)

    for msg in st.session_state["chat_history"]:
        if msg["role"] == "user":
            st.markdown(f"""
            <div style='display:flex;justify-content:flex-end;gap:8px;
            align-items:flex-end;margin:10px 0;'>
                <div style='background:white;border:2px solid #f5a623;
                border-radius:18px 18px 4px 18px;padding:10px 14px;
                max-width:72%;font-size:0.85em;color:#2d2d2d;line-height:1.5;'>
                {msg["content"]}</div>
                <div style='width:32px;height:32px;flex-shrink:0;
                background:linear-gradient(135deg,#e65100,#f5a623);
                border-radius:50%;display:flex;align-items:center;justify-content:center;'>👤</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='display:flex;justify-content:flex-start;gap:8px;
            align-items:flex-end;margin:10px 0;'>
                <div style='width:32px;height:32px;flex-shrink:0;
                background:linear-gradient(135deg,#1b5e20,#2e7d32);
                border-radius:50%;display:flex;align-items:center;justify-content:center;'>🤖</div>
                <div style='background:white;border:2px solid #2e7d32;
                border-radius:18px 18px 18px 4px;padding:10px 14px;
                max-width:72%;font-size:0.85em;color:#1a2e1a;line-height:1.5;'>
                {msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── CHAT INPUT ────────────────────────────────────
    question = st.chat_input("💬 Ask about technology or courses...")

    if question:
        st.session_state["chat_history"].append({"role": "user", "content": question})
        if user_id:
            try:
                supabase.table("chat_history").insert({
                    "user_id": user_id,
                    "role": "user",
                    "message": question,
                    "course": course,
                    "timestamp": datetime.now().isoformat()
                }).execute()
            except:
                pass

        with st.spinner("🤖 Thinking..."):
            answer = get_ai_response(question, course)

        st.session_state["chat_history"].append({"role": "assistant", "content": answer})
        if user_id:
            try:
                supabase.table("chat_history").insert({
                    "user_id": user_id,
                    "role": "assistant",
                    "message": answer,
                    "course": course,
                    "timestamp": datetime.now().isoformat()
                }).execute()
            except:
                pass
        st.rerun()