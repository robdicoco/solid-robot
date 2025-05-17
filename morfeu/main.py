from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from .dream_agent import DreamInterpreter
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify API key is present
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

app = FastAPI(
    title="Morfeu Dream Interpreter",
    description="An AI-powered dream interpretation API using multiple agents",
    version="1.0.0"
)

# Initialize the dream interpreter
interpreter = DreamInterpreter()

class DreamRequest(BaseModel):
    dream: str = Field(..., description="The dream text to be interpreted")

class Symbol(BaseModel):
    symbol: str
    meaning: str
    context: str = "neutral"

class DreamResponse(BaseModel):
    dream: str
    interpretation: str
    psychological_insight: str
    life_application: str
    guidance: str = ""
    symbols_analysis: List[Dict[str, Any]] = []

@app.post("/interpret", response_model=DreamResponse)
async def interpret_dream(request: DreamRequest):
    """
    Interpret a dream using the Morfeu multi-agent AI system.
    
    The system uses three specialized agents:
    1. Symbol Search agent - Identifies symbols and searches for meanings
    2. Symbol Analyzer - Analyzes symbols in context using psychology
    3. Dream Interpreter - Creates a poetic, insightful interpretation
    
    Args:
        request: DreamRequest containing the dream description
        
    Returns:
        DreamResponse containing the interpretation and analysis
    """
    try:
        if not request.dream.strip():
            raise HTTPException(status_code=400, detail="Dream text cannot be empty")
            
        interpretation = interpreter.interpret_dream(request.dream)
        return DreamResponse(**interpretation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "morfeu-dream-interpreter"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 