from mcp_server.llm_manager import get_llm_response
from mcp_server.config import get_default_model

class AIAgent:
    def __init__(self):
        self.history = []

    async def get_response(self, user_input, model_override=None):
        self.history.append({"role": "user", "content": user_input})
        model = model_override or get_default_model()
        response = await get_llm_response(user_input, model)
        self.history.append({"role": "assistant", "content": response})
        return response
