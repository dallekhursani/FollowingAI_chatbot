from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.services.llm_service import generate_llm_response
from app.utils.memory import ChatMemory

app = FastAPI(title="FollowingAI Chatbot API")

# Memory instance for conversation
memory = ChatMemory()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    memory.add_user_message(request.message)
    reply = generate_llm_response(memory.get_conversation())
    memory.add_bot_message(reply)
    return ChatResponse(reply=reply)
