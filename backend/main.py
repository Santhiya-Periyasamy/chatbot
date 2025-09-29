from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langgraph.graph import StateGraph
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

print("Gemini API Key Loaded:", os.getenv("GEMINI_API_KEY") is not None)

# Init FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Currently
state = ChatState(messages=[{"role": "user", "content": user_message}])

class ChatState:
    def __init__(self, messages=None):
        if messages is None:
            messages = []
        self.messages = messages


graph = StateGraph(ChatState)

def process_message(state: ChatState):
    user_input = state.messages[-1]["content"]

    if "goal" in user_input.lower():
        reply = "Great! Let's break your goal into smaller steps. What's the first task?"
    elif "motivate" in user_input.lower():
        reply = "Remember: progress, not perfection! 🚀 Keep going."
    else:
        response = model.generate_content(user_input)
        reply = response.text

    state.messages.append({"role": "assistant", "content": reply})
    return state

graph.add_node("process", process_message)
graph.set_entry_point("process")


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    
    state = ChatState(messages=[{"role": "user", "content": user_message}])
    result = graph.compile().invoke(state)
    
    return {"response": result.messages[-1]["content"]}
