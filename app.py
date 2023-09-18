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

def summarize(text, length, format, model, extractiveness, temperature, additional_command):
    response = co.summarize(text = text, 
                            length = length,
                            format = format,
                            model = model,
                            extractiveness = extractiveness,
                            temperature = temperature,
                            additional_command = additional_command
                            )
    return(response.summary)

#Summarize Endpoint Parameters
## https://docs.cohere.com/reference/summarize-2

length_choice = ["short", "medium", "long", "auto"]
format_choice = ["paragraph", "bullets", "auto"]
model_choice = ["command", "command-nightly", "command-light", "command-light-nightly"]
extractiveness_choice = ["low", "medium", "high", "auto"]
temperature_choice = [0,1,2,3,4,5]
examples = ["At the fall of Troy, Cassandra sought shelter in the temple of Athena. There she embraced the wooden statue of Athena in supplication for her protection, but was abducted and brutally raped by Ajax the Lesser. Cassandra clung so tightly to the statue of the goddess that Ajax knocked it from its stand as he dragged her away. The actions of Ajax were a sacrilege because Cassandra was a supplicant at the sanctuary, and under the protection of the goddess Athena and Ajax further defiled the temple by raping Cassandra. In Apollodorus chapter 6, section 6, Ajax's death comes at the hands of both Athena and Poseidon \"Athena threw a thunderbolt at the ship of Ajax; and when the ship went to pieces he made his way safe to a rock, and declared that he was saved in spite of the intention of Athena. But Poseidon smote the rock with his trident and split it, and Ajax fell into the sea and perished; and his body, being washed up, was buried by Thetis in Myconos\".",
            "Hi Cassandra I am a big fan of your blog. You share a lot of useful tips here. I especially like your post \“How to Eat Apples with Long Nails\”. It’s both well written and useful. I would like to contribute a unique post for your blog as well. I have read your guidelines and will follow them while writing the post. If you’re interested, I would love to work with you on the topics and formats that best meet your needs for the blog. Would you prefer sample topics, a draft outline, or a complete post?Thank you,Zuko"]

demo = gr.Interface(fn = summarize, 
                    inputs = [gr.components.Textbox(label = "Text to Summarize", lines = 5, placeholder = "Write/Paste Text Here"),
                              gr.components.Dropdown(label = "Summary Length", choices = length_choice),
                              gr.components.Dropdown(label = "Format", choices = format_choice),
                              gr.components.Dropdown(label = "Model", choices = model_choice),
                              gr.components.Dropdown(label = "Quoting", choices = extractiveness_choice),
                              gr.Slider(label = "Temperature", minimum = temperature_choice[0], maximum = temperature_choice[-1],
                                        value = temperature_choice[round(len(temperature_choice)/2)], step = 1)], 
                    outputs = [gr.Textbox(label = "Summary", lines = 3)],
                    title = "Text Summarization with Cohere's co.summarize() Endpoint",
                    description = "Enter any text (250 words minimum) and get a concise summary!")

demo.launch()