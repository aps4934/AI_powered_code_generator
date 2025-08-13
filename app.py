from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create FastAPI app
app = FastAPI()

# Allow all origins for CORS (for local frontend testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class CodeRequest(BaseModel):
    prompt: str
    language: str

@app.post("/generate-code")
async def generate_code(request: CodeRequest):
    try:
        # Build prompt for AI
        full_prompt = f"Generate a {request.language} program for: {request.prompt}"

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI that writes clean, working code."},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7
        )

        # Extract generated code
        generated_code = response.choices[0].message.content

        return {"code": generated_code}

    except Exception as e:
        return {"error": str(e)}


@app.get("/")
async def root():
    return {"message": "AI Code Generator Backend is running"}
