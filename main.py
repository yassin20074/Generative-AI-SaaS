# FastAPI with JWT Authentication
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from workers import generate_content
from utils import upload_to_s3

SECRET_KEY = "YOUR_SUPER_SECRET_KEY"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

app = FastAPI(title="AI Content Studio")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = jwt.encode({"sub": form_data.username}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/generate-text/")
async def generate_text(prompt: str = Form(...), user: str = Depends(get_current_user)):
    result = generate_content("text", prompt)
    url = upload_to_s3(result, "text_output.txt")
    return {"user": user, "s3_url": url}

@app.post("/generate-image/")
async def generate_image(prompt: str = Form(...), user: str = Depends(get_current_user)):
    result_path = generate_content("image", prompt)
    url = upload_to_s3(result_path, "image_output.png")
    return {"user": user, "s3_url": url}

@app.post("/generate-video/")
async def generate_video(prompt: str = Form(...), user: str = Depends(get_current_user)):
    result_path = generate_content("video", prompt)
    url = upload_to_s3(result_path, "video_output.mp4")
    return {"user": user, "s3_url": url}
