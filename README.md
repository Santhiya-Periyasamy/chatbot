 Chatbot with FastAPI & Gemini API

A simple prototype chatbot built using **FastAPI**, **Google Generative AI (Gemini API)**, and **LangGraph** for managing conversation states.  
This project is experimental and primarily intended for **learning, testing, and reference purposes**.

 Features
- Accepts user messages via HTTP **POST** requests.
- Generates responses using **Google Gemini API**.
- (Experimental) Conversation state management with **LangGraph**.
- Secure configuration using `.env`.

 Requirements
- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Google Generative AI SDK](https://ai.google.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

 Installation

1. Clone the repository
   git clone https://github.com/Santhiya-Periyasamy/chatbot.git
   cd chatbot
   cd chatbot
2.Create and activate a virtual environment
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
3.Install dependencies
   pip install -r requirements.txt
   Set up environment variables
4.Create a .env file in the project root and add your Gemini API key:
   GEMINI_API_KEY=your_api_key_here

Usage

1.Start the FastAPI server
   uvicorn main:app --reload
2.Send a chat request
   Example JSON payload:
   {
     "message": "Hello, chatbot!"
   }
   Example using curl:
   curl -X POST "http://127.0.0.1:8000/chat" \
   -H "Content-Type: application/json" \
   -d '{"message":"Hello!"}'


Project Details
Backend Framework: FastAPI

AI Model: Google Gemini API

State Management: LangGraph (for multi-turn conversations)

Environment Configuration: .env for sensitive keys

Extensibility: Can be expanded with custom flows, context handling, and better error handling

