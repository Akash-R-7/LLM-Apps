import torch
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "SkyR/linkedin-8bit-phi4"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    load_in_8bit=True,  # or use 8-bit
    torch_dtype=torch.float16
)

model = torch.compile(model)

def generate_response(history, user_input):
    # Ensure history is a list of tuples (user_input, response)
    if not isinstance(history, list):
        history = []
    # Filter out any items that are not tuples of length 2
    history = [item for item in history if isinstance(item, tuple) and len(item) == 2]

    user_input = "Create a linked post of around 120 words on this: " + user_input 

    prompt = f"<|user|>\n{user_input}\n<|assistant|>\n"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

    output_ids = model.generate(
        input_ids,
        max_new_tokens=175,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    # Assuming the model output starts with the prompt, remove it
    # A more robust approach might involve finding the start of the assistant's response
    if output_text.startswith(user_input):
        response = output_text[len(user_input):].strip()
    else:
        response = output_text.strip()

    # Append the user input and response as a tuple to history
    history.append((user_input, response))

    return history

# Function to clear the chat
def clear_chat():
    return [], "" # Return empty list for history and empty string for textbox


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(label="Ask me to generate a LinkedIn post...")
    submit_btn = gr.Button("Submit")
    clear_btn = gr.Button("Clear") # Added clear button

    # Link components and events
    submit_btn.click(
        generate_response,
        inputs=[chatbot, msg],
        outputs=[chatbot],
        queue=False
    )
    msg.submit(
        generate_response,
        inputs=[chatbot, msg],
        outputs=[chatbot],
        queue=False
    )
    clear_btn.click(
        clear_chat,
        inputs=[],
        outputs=[chatbot, msg],
        queue=False
    )


demo.launch()