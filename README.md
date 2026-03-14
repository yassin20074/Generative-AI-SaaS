# Generative-AI-SaaS 

*Generative AI SaaS allows users to generate text, images, and videos from a textual description using state-of-the-art AI models*

# Features

- Generate text using GPT API

- Generate images using GPT API

- Generate short videos using Runway Gen-2 API

- Automatically upload outputs to AWS S3

- Queue system for processing heavy requests (SQS placeholder)

- User notifications upon completion (SNS placeholder)

- Automatic deployment to AWS ECS/Fargate via GitHub Actions

- Local development using Docker Compose


# Architecture Diagram

User (Frontend React)
       |
       v
FastAPI Backend (Endpoints: Text/Image/Video)
       |
       v
Worker Services (Microservices)
       |
       v
Pretrained Models (GPT, SDXL, Runway Gen-2)
       |
       v
S3 Storage (Output files)
       |
       v
User (Download / View)

# How to Run Locally

1. Set environment variables:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

BUCKET_NAME

OPENAI_API_KEY



*2. Run Docker Compose:*



docker-compose up --build

3. Open your browser at http://localhost:3000 to use the frontend interface.

# Created By:eng.Yassin Sanad 
 
