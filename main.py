import requests
import gradio as gr
import io
from PIL import Image

# API URL and authorization using API key (Bearer token)
API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
# your api key 
headers = {"Authorization": "Bearer hf_XXXXX"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# To generate image on given prompt
def generate_image(prompt):
    image_bytes = query({"inputs": prompt})
    image = Image.open(io.BytesIO(image_bytes))
    return image

# Interface
demo = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image"
)

demo.launch(share=True)
