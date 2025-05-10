import os
from dotenv import load_dotenv
import openai
import anthropic
import google.generativeai as genai

load_dotenv()

# Initialize API clients
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

# Main LLM router
async def get_llm_response(prompt, model_name="gpt-3.5-turbo"):
    try:
        if model_name.startswith("gpt"):
            return await _get_openai_response(prompt, model_name)
        elif model_name.startswith("claude"):
            return await _get_claude_response(prompt, model_name)
        elif model_name.startswith("gemini"):
            return await _get_gemini_response(prompt, model_name)
        else:
            return f"Model {model_name} not supported."
    except Exception as e:
        return f"Error occurred while getting response from {model_name}: {str(e)}"

# OpenAI (new API ≥ 1.0.0)
async def _get_openai_response(prompt, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI API error: {str(e)}"

# Anthropic Claude
async def _get_claude_response(prompt, model):
    try:
        message = anthropic_client.messages.create(
            model=model,
            max_tokens=512,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"Claude API error: {str(e)}"

# Google Gemini
async def _get_gemini_response(prompt, model):
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API error: {str(e)}"
