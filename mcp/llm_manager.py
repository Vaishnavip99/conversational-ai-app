import os
import openai
import anthropic
import google.generativeai as genai

# Load keys
openai.api_key = os.getenv("OPENAI_API_KEY")
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def get_llm_response(prompt, model_name="gpt-3.5-turbo"):
    if model_name.startswith("gpt"):
        return await _get_openai_response(prompt, model_name)
    elif model_name.startswith("claude"):
        return await _get_claude_response(prompt, model_name)
    elif model_name.startswith("gemini"):
        return await _get_gemini_response(prompt, model_name)
    else:
        return f"Model {model_name} not supported."

async def _get_openai_response(prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

async def _get_claude_response(prompt, model):
    message = anthropic_client.messages.create(
        model=model,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

async def _get_gemini_response(prompt, model):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text
