import streamlit as st
from backend import get_ai_response

st.set_page_config(page_title="LearnMate Chatbot", page_icon="🤖", layout="centered")

# Guard
if "user_course" not in st.session_state:
    st.error("Please fill the registration form first.")
    st.switch_page("app.py")
    st.stop()

course = st.session_state["user_course"]
name   = st.session_state["user_name"]

# ── CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #e8f5e9 0%, #f1f8f1 100%);
}

/* Chat header */
.chat-header {
    background: linear-gradient(135deg, #2e7d32, #1b5e20);
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
}
.robot-icon {
    width: 55px;
    height: 55px;
    background: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8em;
}
.chat-header-text h2 {
    color: white;
    margin: 0;
    font-size: 1.3em;
    font-weight: 700;
}
.chat-header-text p {
    color: #c8e6c9;
    margin: 0;
    font-size: 0.85em;
}

/* User bubble - RIGHT side */
.user-bubble-row {
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    gap: 10px;
    margin: 12px 0;
}
.user-bubble {
    background: white;
    color: #1a1a2e;
    padding: 12px 18px;
    border-radius: 20px 20px 4px 20px;
    max-width: 70%;
    font-size: 0.97em;
    line-height: 1.5;
    box-shadow: 0 2px 8px rgba(230,81,0,0.15);
    border: 2px solid #f5a623;
}
.user-avatar {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #e65100, #f5a623);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1em;
    flex-shrink: 0;
}

/* AI bubble - LEFT side */
.ai-bubble-row {
    display: flex;
    justify-content: flex-start;
    align-items: flex-end;
    gap: 10px;
    margin: 12px 0;
}
.ai-bubble {
    background: white;
    color: #1a1a2e;
    padding: 12px 18px;
    border-radius: 20px 20px 20px 4px;
    max-width: 70%;
    font-size: 0.97em;
    line-height: 1.5;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border: 2px solid #2e7d32;
}
.ai-avatar {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #2e7d32, #1b5e20);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1em;
    flex-shrink: 0;
}

/* Chat input */
.stChatInput > div {
    border-radius: 16px !important;
    border: 2px solid #c8e6c9 !important;
    background: white !important;
}

/* Back button */
div.stButton > button {
    background: white !important;
    color: #2e7d32 !important;
    border: 2px solid #2e7d32 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 8px 20px !important;
    width: auto !important;
}
div.stButton > button:hover {
    background: #2e7d32 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ── Chat Header ───────────────────────────────────────────────
st.markdown(f"""
<div class="chat-header">
    <div class="robot-icon">🤖</div>
    <div class="chat-header-text">
        <h2>LearnMate AI Assistant</h2>
        <p>Hi {name}! Ask me anything about {course} 💬</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Back button
if st.button("⬅️ Back to Course Details"):
    st.switch_page("pages/course_details.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── Chat History ──────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Display messages as bubbles
for msg in st.session_state["chat_history"]:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="user-bubble-row">
            <div class="user-bubble">{msg["content"]}</div>
            <div class="user-avatar">👤</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="ai-bubble-row">
            <div class="ai-avatar">🤖</div>
            <div class="ai-bubble">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Chat Input ────────────────────────────────────────────────
question = st.chat_input("Ask your question here...")

if question:
    st.session_state["chat_history"].append({
        "role": "user",
        "content": question
    })

    with st.spinner("🤖 Thinking..."):
        answer = get_ai_response(question, course)

    st.session_state["chat_history"].append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; color:#aaa; font-size:0.8em; margin-top:20px;">
    🤖 Powered by LearnMate AI | SkilzLearn 🎓
</div>
""", unsafe_allow_html=True)