#Requesting the required libraries 

from fastapi import FastAPI, Form
from workers import generate_content
from utils import upload_to_s3

app = FastAPI(title="Generative AI SaaS")

#Creating the endpoint 
@app.post("/generate-text/")
async def generate_text(prompt: str = Form(...)):# Text generation function 
    result = generate_content("text", prompt)
    url = upload_to_s3(result, "text_output.txt") #Save the reply to the cloud 
    return {"s3_url": url}

@app.post("/generate-image/")
async def generate_image(prompt: str = Form(...)):#Image generation function 
    result_path = generate_content("image", prompt)
    url = upload_to_s3(result_path, "image_output.png")
    return {"s3_url": url}

@app.post("/generate-video/")
async def generate_video(prompt: str = Form(...)): #Video generation function 
    result_path = generate_content("video", prompt)
    url = upload_to_s3(result_path, "video_output.mp4")
    return {"s3_url": url}
