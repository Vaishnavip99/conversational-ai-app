import gradio as gr
import requests

def chat_with_bot(user_input, model="gpt-3.5-turbo"):
    res = requests.post("http://localhost:8000/chat", json={"user_input": user_input, "model": model})
    return res.json()["response"]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    txt = gr.Textbox(placeholder="Ask something...")
    model_dd = gr.Dropdown(
        ["gpt-3.5-turbo", "gpt-4", "claude-3-opus-20240229", "gemini-pro"],
        value="gpt-3.5-turbo", 
        label="Select Model"
    )

    def respond(user_input, chat_history, model):
        response = chat_with_bot(user_input, model)
        chat_history.append((user_input, response))
        return "", chat_history

    txt.submit(respond, [txt, chatbot, model_dd], [txt, chatbot])

demo.launch()
