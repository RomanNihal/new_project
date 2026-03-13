from langchain_core.messages import AIMessage
from app.services.providers.openai import get_llm
from app.api.schema.chat_state import ChatState

from langchain_core.messages import SystemMessage

def generate_content(state: ChatState):
    llm = get_llm()
    
    system_prompt = """You are a helpful assistant for booking services.
Your goal is to collect EXACTLY 4 pieces of information from the user:
1. What service they want
2. How much they want to spend (budget)
3. When they want to take the service (date/time)
4. Their preferred location

Guidelines:
- Ask one or two questions at a time in a conversational, friendly manner.
- Be polite and helpful.
- Do NOT make up information.
- Once you have successfully gathered ALL 4 pieces of information, you MUST output a raw JSON response (and no other text) in the exact following format:
{
  "status": "COMPLETED",
  "service": "<service>",
  "budget": "<budget>",
  "time": "<time>",
  "location": "<location>"
}
"""
    # Prepend the system prompt to the messages
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    
    # Invoke the LLM with the messages
    result = llm.invoke(messages)
    
    # Return the new message to be appended to the state
    return {"messages": [result]}
