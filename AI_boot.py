from transformers import pipeline

chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

def chat(prompt):
    response = chatbot(prompt, max_new_tokens=100)[0]['generated_text']
    print("🤖:", response)

if __name__ == "__main__":
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        chat(prompt)
