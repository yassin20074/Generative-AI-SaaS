#Retrieve the required libraries 
import openai
import requests
from PIL import Image

openai.api_key = "YOUR_OPENAI_API_KEY" #Place your API here 

def generate_content(content_type: str, prompt: str): # Content generating function 
  #Text generation 
    if content_type == "text":
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=300
        )
        return response.choices[0].text
#Image generation 
    elif content_type == "image":
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        img_data = requests.get(image_url).content
        path = "image_output.png"
        with open(path, "wb") as f:
            f.write(img_data)
        return path #Return to the original path 
#Video generation 
    elif content_type == "video":

        API_KEY = "YOUR_RUNWAY_API_KEY"# Place your back API from the runway platform.
        url = "https://api.runwayml.com/v1/videos"

       payload = {
    "prompt": prompt,
    "model": "gen-2",      # A sample of the Runway platform 
    "length": 5,           # Video length in seconds 
    "fps": 15,             # Number of frames per second 
    "resolution": "512x512"
}

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    video_url = response.json()["video_url"]
    print("Video URL:", video_url)
else:
    print("Error:", response.text)
        path = "video_output.mp4"#An example of the runway platform 
        with open(path, "wb") as f:
            f.write(b"dummy video content")
        return path
