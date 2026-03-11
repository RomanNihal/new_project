from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_llm():
    # Attempt to retrieve API key, defaulting to None if it isn't in environment
    api_key = getattr(settings, "OPENAI_API_KEY", None)
    
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
        temperature=0.7
    )
