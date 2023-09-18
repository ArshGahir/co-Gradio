import cohere as co
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("COHERE_API_KEY")
co = co.Client(api_key)

personality = f"""You are a helpful and intelligent personal assistant. \
                Your job is to follow instructions to the best of your abilities in order to answer an questions or \
                complete any tasks. Assume you have full autonomy, and solve any issues that arise in order to achieve \
                the end goal of a task. In this case, full autonomy means that you are able to modify given instructions \
                as you see fit, in order to achieve the end goal."""

def summarize(input):
    response = co.summarize(text = input, 
                            length = "auto",
                            format = "bullets",
                            model = "command-nightly",
                            extractiveness = "medium",
                            temperature = 3,
                            additional_command = personality
                            )
    return(response.summary)

demo = gr.Interface(fn = summarize, 
                    inputs = [gr.Textbox(label = "Text to Summarize", lines = 5)], 
                    outputs = [gr.Textbox(label = "Summary", lines = 3)],
                    title = "Text Summarization with Cohere's co.summarize() Endpoint",
                    description = "Enter any text (250 words minimum) and get a concise summary!")

demo.launch()