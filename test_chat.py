import requests
import uuid

def main():
    url = "http://127.0.0.1:8000/chat"
    
    # Generate a random session ID for this chat instance
    session_id = str(uuid.uuid4())
    print("==================================")
    print("Service Booking Chatbot Test")
    print("Type 'quit' or 'exit' to stop.")
    print("==================================\n")
    
    while True:
        user_message = input("You: ")
        if user_message.strip().lower() in ["quit", "exit"]:
            print("Exiting...")
            break
            
        payload = {
            "session_id": session_id,
            "message": user_message
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            
            print(f"\nAI: {data.get('message')}")
            
            # If a professional ID was generated (meaning completion)
            if data.get('professionalId'):
                print(f"\n✨ [Task Complete! Assigned Professional IDs: {data.get('professionalId')}] ✨\n")
                
        except requests.exceptions.RequestException as e:
            print(f"\nError connecting to the API: {e}")
            print("Make sure your FastAPI server is running! (uvicorn main:app --reload)")
            
if __name__ == "__main__":
    main()
