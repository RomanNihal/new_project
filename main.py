from fastapi import FastAPI
from app.api.endpoints.chat import router as chat_router
from app.middleware.setup import add_cors_middleware

app = FastAPI(title="LangChain Psychotherapy Chatbot")

# Add middleware
add_cors_middleware(app)

app.include_router(chat_router)

@app.get('/')
def root():
    return {
        'msg': 'Welcome'
    }
