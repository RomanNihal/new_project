from langchain_core.messages import AIMessage
from app.services.providers.openai import get_llm
from app.api.schema.chat_state import ChatState

def generate_content(state: ChatState):
    llm = get_llm()
    # Invoke the LLM with the messages from the state
    result = llm.invoke(state["messages"])
    
    # Return the new message to be appended to the state
    return {"messages": [result]}
