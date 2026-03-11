from langchain_anthropic import ChatAnthropic
from app.core.config import settings

def get_llm():
    # Attempt to retrieve API key, defaulting to None if it isn't in environment
    api_key = getattr(settings, "ANTHROPIC_API_KEY", None)
    
    return ChatAnthropic(
        model="claude-3-opus-20240229",
        api_key=api_key,
        temperature=0.7
    )
