from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm():
    # Attempt to retrieve API key, defaulting to None if it isn't in environment
    api_key = getattr(settings, "GOOGLE_API_KEY", getattr(settings, "GEMINI_API_KEY", None))
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        api_key=api_key,
        temperature=0.7
    )
