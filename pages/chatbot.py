import streamlit as st
from backend import get_ai_response

st.set_page_config(page_title="LearnMate Chatbot", page_icon="🤖", layout="wide")

# ✅ Guard: send back if no session data
if "user_course" not in st.session_state:
    st.error("Please fill the registration form first.")
    st.switch_page("app.py")
    st.stop()

course = st.session_state["user_course"]
name   = st.session_state["user_name"]

st.title(f"🤖 LearnMate Chatbot")
st.markdown(f"Hi **{name}**! Ask me anything about **{course}** or any other course. I'm here to help!")

# Back button
if st.button("⬅️ Back to Course Details"):
    st.switch_page("pages/course_details.py")

st.divider()

# ✅ FIX: Initialize chat history in session so messages persist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Display previous messages
for msg in st.session_state["chat_history"]:
    st.chat_message(msg["role"]).write(msg["content"])

# New message input
question = st.chat_input("Ask your question here...")

if question:
    # Show user message
    st.chat_message("user").write(question)
    st.session_state["chat_history"].append({"role": "user", "content": question})

    # Get AI response with course context
    with st.spinner("Thinking..."):
        answer = get_ai_response(question, course)

    # Show AI response
    st.chat_message("assistant").write(answer)
    st.session_state["chat_history"].append({"role": "assistant", "content": answer})