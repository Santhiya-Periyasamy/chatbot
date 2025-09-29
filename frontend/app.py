import streamlit as st
import requests

st.set_page_config(page_title="Productivity Mentor", page_icon="🤖", layout="centered")

st.title("🤖 Productivity Mentor Chatbot")
st.write("Your AI mentor to stay motivated and break down goals into tasks.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input
if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    response = requests.post("http://127.0.0.1:8000/chat", json={"message": prompt}).json()
    bot_reply = response["response"]

    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").markdown(bot_reply)
