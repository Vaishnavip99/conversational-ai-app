# conversational-ai-app
conversational-ai-app/
├── mcp_server/
├── frontend/
├── llm_providers/
├── agent/
├── .env

# Conversational AI Application

## Setup

# Clone the repository:
   ```bash
   git clone https://github.com/your-repo/conversational-ai-app.git
   cd conversational-ai-app

# Create a Python virtual environment:
python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows

#Install initial dependencies:
pip install fastapi uvicorn gradio openai python-dotenv

#Initialize Git:
git init

# Install dependencies:
pip install -r requirements.txt

#Set up environment variables in .env:

OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GEMINI_API_KEY=your_gemini_api_key
ACTIVE_LLM=openai  # Switch between 'openai', 'gemini', or 'claude'

#Run the FastAPI server:

uvicorn mcp_server.server:app --reload

#Run the Gradio frontend:

python frontend/app.py

# deployment
The deployment here for the FastAPI server and Gradio interface can be done separately or together.
# Here it is done seperately.


