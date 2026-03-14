# Generative AI SaaS

- Generative AI SaaS allows users to generate text, images, and videos from a textual description using state-of-the-art AI models. This project integrates GPT for text, Stable Diffusion for images, and Runway Gen-2 for video generation.

# Features

- Text Generation: Generate high-quality text using GPT API.

- Image Generation: Create images based on text prompts using gpt api .

- Video Generation: Produce short AI-generated videos from text prompts using Runway Gen-2.

- AWS S3 Integration: Automatically upload generated content to Amazon S3.

- Queue System: Handle heavy workloads using SQS (placeholder for future enhancements).

- Notifications: Send completion notifications to users (SNS placeholder).

- Secure API: JWT authentication for all generation endpoints.

- Automatic Deployment: CI/CD workflow with GitHub Actions to deploy backend Docker containers on AWS ECS/Fargate.

- Local Development: Full local environment using Docker Compose for both frontend and backend.


# Architecture Diagram

User (Frontend React)
       |
       v
FastAPI Backend (Endpoints: Text/Image/Video) with JWT Auth
       |
       v
Worker Services (Microservices for Text/Image/Video)
       |
       v
Pretrained Models:
   - GPT (Text)
   - Stable Diffusion (Images)
   - Runway Gen-2 (Videos)
       |
       v
S3 Storage (Output Files)
       |
       v
User (Download / View)

# How It Works

- 1. User Interaction: The user sends a text prompt from the React frontend.


- 2. Authentication: JWT is used to secure endpoints; users must log in to obtain an access token.


- 3. Request Processing: Backend routes call the respective worker functions.


- 4. AI Model Execution:

**Text: GPT generates content.**

**Image: GPT generates an image.**

**Video: Runway Gen-2 API generates a video file.**



- 5. Upload: Generated files are uploaded to AWS S3.


- 6. Response: Backend returns the S3 URL for the user to download/view the content.



# Running Locally

- 1. Set environment variables:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

BUCKET_NAME

OPENAI_API_KEY (for GPT)

RUNWAY_API_KEY (for Runway Gen-2 videos)



- 2. Start Docker Compose:



docker-compose up --build

- 3. Access the frontend at http://localhost:3000.



# Deployment

The project uses GitHub Actions for CI/CD.

Docker images for backend are pushed to AWS ECR.

Deployment is automated to AWS ECS/Fargate.


# Security

**All generation endpoints are JWT-protected.**

**Only authenticated users with a valid token can generate content.**


# Future Enhancements

- Add real SQS queue for async processing of heavy tasks.

- Integrate SNS for user notifications.

- Support multi-user collaboration and history tracking.

-Expand model options (more AI models for text, images, and videos).


# Created By:eng.Yassin Sanad 
 
