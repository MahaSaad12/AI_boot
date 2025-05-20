import gradio as gr
from transformers import pipeline

# Load the chatbot pipeline
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Chat function
def chat(prompt, history):
    response = chatbot(prompt, max_new_tokens=100)[0]['generated_text']
    history.append(("You: " + prompt, "🤖: " + response))
    return "", history

# Interface layout
with gr.Blocks(title="Custom FLAN-T5 Chatbot") as demo:
    gr.Markdown("## 🤖 Welcome to Your Custom FLAN-T5 Chatbot")
    gr.Markdown("Type a message and press Enter. Type `exit` or `quit` to stop chatting.")

    with gr.Row():
        with gr.Column(scale=1):
            chatbot_history = gr.Chatbot(label="Chat History")
            user_input = gr.Textbox(placeholder="Type your message here...", label="Your Message")
            clear_btn = gr.Button("Clear Chat")

    # Chat interaction
    user_input.submit(chat, [user_input, chatbot_history], [user_input, chatbot_history])
    clear_btn.click(lambda: [], None, chatbot_history)

# Run app
demo.launch()
