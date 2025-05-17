from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from .dream_agent import DreamInterpreter
import os
import json
import re
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

class SymbolAnalysis(BaseModel):
    symbol: str
    archetypal_meaning: Optional[str] = None
    context_in_dream: Optional[str] = None
    psychological_interpretation: Optional[str] = None

class DreamResponse(BaseModel):
    dream: str
    interpretation: str
    psychological_insight: str
    life_application: str
    guidance: Optional[str] = None
    symbols_analysis: List[Dict[str, Any]] = []
    source_language: Optional[str] = "unknown"
    interpretation_language: Optional[str] = "unknown"
    language_match: Optional[bool] = True
    quality_assessment: Optional[str] = "No quality assessment available"

def clean_text(text):
    """Clean up text from JSON artifacts and code blocks."""
    if text is None:
        return "No content available"
    
    # Remove JSON code blocks
    text = text.replace("```json", "").replace("```", "").strip()
    # Remove escaped characters
    text = text.replace("\\n", "\n").replace('\\"', '"')
    # Handle the case where "See interpretation above" is present
    if text in ["See interpretation above", "Unable to extract structured content"]:
        return "No specific content extracted. Please see the main interpretation."
    
    return text

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
        
        # Clean up text fields to ensure they're user-friendly
        for key in ["interpretation", "psychological_insight", "life_application", "guidance"]:
            if key in interpretation:
                interpretation[key] = clean_text(interpretation[key])
        
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