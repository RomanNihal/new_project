from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_llm():
    # Attempt to retrieve API key, defaulting to None if it isn't in environment
    api_key = getattr(settings, "XAI_API_KEY", None)
    
    # Grok works perfectly via OpenAI compatible endpoint
    return ChatOpenAI(
        base_url="https://api.x.ai/v1",
        model="grok-beta",
        api_key=api_key,
        temperature=0.7
    )
