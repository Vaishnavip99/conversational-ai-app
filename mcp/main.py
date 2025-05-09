from fastapi import FastAPI, Request
from pydantic import BaseModel
from mcp_server.llm_manager import get_llm_response
from ai_agent.agent import AIAgent

app = FastAPI()
agent = AIAgent()

class ChatInput(BaseModel):
    user_input: str
    model: str = None

@app.post("/chat")
async def chat(input: ChatInput):
    response = await agent.get_response(input.user_input, input.model)
    return {"response": response}
