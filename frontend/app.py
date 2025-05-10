import gradio as gr
import requests

def chat_with_bot(user_input, model="gpt-3.5-turbo"):
    try:
        res = requests.post("http://localhost:8000/chat", json={"user_input": user_input, "model": model})
        
        if res.status_code == 200:
            if res.text:
                try:
                    return res.json()["response"]
                except ValueError:
                    return "Error: Response is not in valid JSON format"
            else:
                return "Error: Empty response received"
        else:
            return f"Error: Received status code {res.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type='messages')
    txt = gr.Textbox(placeholder="Ask something...")
    model_dd = gr.Dropdown(
        ["gpt-3.5-turbo", "gpt-4", "claude-3-opus-20240229", "gemini-pro"],
        value="gpt-3.5-turbo",
        label="Select Model"
    )

    def respond(user_input, chat_history, model):
        response = chat_with_bot(user_input, model)
        # Append as a dictionary with 'role' and 'content'
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response})
        return "", chat_history

    txt.submit(respond, [txt, chatbot, model_dd], [txt, chatbot])
    submit_btn = gr.Button("Send")
    submit_btn.click(respond, [txt, chatbot, model_dd], [txt, chatbot])

demo.launch()
