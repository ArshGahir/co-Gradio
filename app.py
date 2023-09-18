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

def generate(input):
    response = co.generate(input)
    return(response)

demo = gr.Interface(fn = generate, inputs = "text", outputs = "text")
demo.launch()