import json
import os
from typing import Dict, List
from pathlib import Path
from datetime import date

from .base_agent import call_agent
from google import genai
from google.adk.agents import Agent
from google.adk.tools import google_search

# Agent 1: Symbol Search Agent - Searches for dream symbols online
def agent_symbol_search(dream_text):
    symbol_search = Agent(
        name="agent_symbol_search",
        model="gemini-2.0-flash",
        instruction="""
          You are a dream symbol researcher.
          Your task is to identify potential dream symbols in the provided dream text 
          and search for their meanings using (google_search).
          Focus on identifying traditional dream symbols (like water, flying, falling, teeth, etc.)
          and searching for their psychological and spiritual interpretations.
          
          Present your findings as a JSON object with this structure:
          {
            "identified_symbols": [
              {
                "symbol": "symbol_name",
                "meaning": "general meaning based on search",
                "context": "how it appeared in the dream"
              }
            ]
          }
        """,
        description="Agent that searches for dream symbol meanings",
        tools=[google_search]
    )

    input_message = f"Dream: {dream_text}"
    # Execute the agent
    symbols_found = call_agent(symbol_search, input_message)
    return symbols_found

# Agent 2: Symbol Analyzer - Analyzes symbols using internal database and search results
def agent_symbol_analyzer(dream_text, symbols_found, symbols_database):
    symbol_analyzer = Agent(
        name="agent_symbol_analyzer",
        model="gemini-2.0-flash",
        instruction=f"""
            You are a dream symbols analyst specializing in psychological interpretations.
            Your task is to analyze the dream symbols identified in the previous stage
            and provide deeper insights on their meaning in the context of the dream.
            
            You have access to this database of archetypal symbols:
            {json.dumps(symbols_database, indent=2)}
            
            Compare the symbols found through search with this database and 
            create a comprehensive analysis of each symbol's potential meaning in the dream.
            
            Format your response as a JSON object with these fields:
            {{
              "symbols_analysis": [
                {{
                  "symbol": "symbol_name",
                  "archetypal_meaning": "meaning from database if available",
                  "context_in_dream": "specific context in this dream",
                  "psychological_interpretation": "what this might mean psychologically"
                }}
              ]
            }}
        """,
        description="Agent that analyzes dream symbols in detail"
    )

    input_message = f"Dream: {dream_text}\nSymbols found: {symbols_found}"
    # Execute the agent
    analysis = call_agent(symbol_analyzer, input_message)
    return analysis

# Agent 3: Dream Interpreter - Creates final poetic interpretation
def agent_dream_interpreter(dream_text, symbols_analysis):
    dream_interpreter = Agent(
        name="agent_dream_interpreter",
        model="gemini-2.0-flash",
        instruction="""
            You are Morfeu, a poetic dream interpreter with deep knowledge of psychology and symbolism.
            Your task is to take the detailed symbol analysis and create a meaningful, 
            insightful interpretation of the dream as a whole.
            
            The interpretation should:
            1. Connect the various symbols into a cohesive narrative
            2. Offer psychological insights about the dreamer's potential state of mind
            3. Suggest possible meanings or messages in the dreamer's life
            4. Maintain a poetic and mystical tone throughout
            5. Be encouraging and positive in overall outlook
            
            YOU MUST RETURN ONLY A VALID JSON object with these fields (and NO additional text or markdown):
            {
              "interpretation": "main poetic interpretation of the dream",
              "psychological_insight": "overall psychological perspective",
              "life_application": "how this might relate to the dreamer's life",
              "guidance": "gentle advice or wisdom based on the dream"
            }
            
            DO NOT wrap your response in ```json or any other markdown code blocks. 
            Return ONLY the JSON object.
        """,
        description="Agent that creates final poetic dream interpretation"
    )

    input_message = f"Dream: {dream_text}\nSymbol Analysis: {symbols_analysis}"
    # Execute the agent
    interpretation = call_agent(dream_interpreter, input_message)
    return interpretation

# Agent 4: Quality & Language Verifier - Checks quality and language match
def agent_quality_language_verifier(dream_text, interpretation_json):
    quality_verifier = Agent(
        name="agent_quality_verifier",
        model="gemini-2.0-flash",
        instruction="""
            You are a quality assurance expert and language specialist for dream interpretations.
            Your task is to:
            
            1. Verify the quality of the dream interpretation:
               - Ensure it is poetic and insightful
               - Check that it addresses the key elements in the dream
               - Verify it's encouraging and positive in tone
            
            2. Identify the language of the user's dream text
            
            3. Check if the interpretation is in the same language as the user's dream text
            
            4. If the language doesn't match, translate the interpretation to the user's language
               
            YOU MUST RETURN ONLY A VALID JSON object with these fields (and NO additional text or markdown):
            {
              "quality_assessment": "Your assessment of the interpretation quality", 
              "source_language": "language of the original dream text",
              "interpretation_language": "language of the interpretation",
              "language_match": true/false,
              "refined_interpretation": {
                "interpretation": "translated/refined interpretation if needed, otherwise keep original",
                "psychological_insight": "translated/refined insight if needed, otherwise keep original",
                "life_application": "translated/refined application if needed, otherwise keep original",
                "guidance": "translated/refined guidance if needed, otherwise keep original"
              }
            }
            
            DO NOT wrap your response in ```json or any other markdown code blocks.
            Return ONLY the JSON object.
        """,
        description="Agent that verifies quality and language match",
        tools=[google_search]
    )

    input_message = f"Dream Text: {dream_text}\nInterpretation: {interpretation_json}"
    # Execute the agent
    verification = call_agent(quality_verifier, input_message)
    return verification

# Main DreamInterpreter class that orchestrates the four agents
class DreamInterpreter:
    def __init__(self):
        # Load dream symbols database
        symbols_path = Path(__file__).parent / "symbols.json"
        with open(symbols_path, "r") as f:
            self.symbols_database = json.load(f)["symbols"]

    def interpret_dream(self, dream: str) -> Dict:
        """Interpret a dream using the four-agent system."""
        print("🔍 Searching for symbols in the dream...")
        symbols_found_text = agent_symbol_search(dream)
        
        # Try to parse symbols_found as JSON
        try:
            symbols_found = json.loads(symbols_found_text)
        except json.JSONDecodeError:
            # If parsing fails, create a basic structure
            symbols_found = {
                "identified_symbols": [
                    {
                        "symbol": "unknown",
                        "meaning": "Could not parse symbols",
                        "context": "See raw text"
                    }
                ],
                "raw_text": symbols_found_text
            }
        
        print("🧠 Analyzing symbols in context...")
        symbols_analysis_text = agent_symbol_analyzer(dream, json.dumps(symbols_found), self.symbols_database)
        
        # Try to parse symbols_analysis as JSON
        try:
            symbols_analysis = json.loads(symbols_analysis_text)
        except json.JSONDecodeError:
            # If parsing fails, create a basic structure
            symbols_analysis = {
                "symbols_analysis": [
                    {
                        "symbol": "unknown",
                        "archetypal_meaning": "Could not parse analysis",
                        "context_in_dream": "See raw text",
                        "psychological_interpretation": "See raw text"
                    }
                ],
                "raw_text": symbols_analysis_text
            }
        
        print("✨ Creating poetic interpretation...")
        final_interpretation_text = agent_dream_interpreter(dream, json.dumps(symbols_analysis))
        
        # Try to parse the final interpretation as JSON
        try:
            # First attempt direct parsing
            interpretation_result = json.loads(final_interpretation_text)
        except json.JSONDecodeError:
            # Check if the response might contain a JSON string (common with LLM responses)
            try:
                # Look for JSON-like content in the text
                if "```json" in final_interpretation_text:
                    # Extract JSON from code blocks
                    json_content = final_interpretation_text.split("```json")[1].split("```")[0].strip()
                    interpretation_result = json.loads(json_content)
                else:
                    # Try to find JSON formatted content within the text
                    import re
                    json_matches = re.findall(r'(\{.*\})', final_interpretation_text, re.DOTALL)
                    if json_matches:
                        interpretation_result = json.loads(json_matches[0])
                    else:
                        raise ValueError("No JSON content found")
            except (json.JSONDecodeError, ValueError, IndexError):
                # If all parsing attempts fail, create a structured response
                interpretation_result = {
                    "interpretation": final_interpretation_text,
                    "psychological_insight": "Unable to extract structured content",
                    "life_application": "Unable to extract structured content",
                    "guidance": "Unable to extract structured content"
                }
        
        # Ensure the result is properly structured
        for key in ["interpretation", "psychological_insight", "life_application", "guidance"]:
            if key in interpretation_result:
                # Clean up the value by removing any JSON or code formatting artifacts
                if isinstance(interpretation_result[key], str):
                    interpretation_result[key] = interpretation_result[key].replace("```json", "").replace("```", "").strip()
                    # Remove any escaped newlines or quotes
                    interpretation_result[key] = interpretation_result[key].replace("\\n", "\n").replace('\\"', '"')
        
        print("🔍 Verifying quality and language match...")
        verification_text = agent_quality_language_verifier(dream, json.dumps(interpretation_result))
        
        # Try to parse the verification as JSON
        try:
            verification_result = json.loads(verification_text)
        except json.JSONDecodeError:
            try:
                # Handle possible code blocks or embedded JSON
                if "```json" in verification_text:
                    json_content = verification_text.split("```json")[1].split("```")[0].strip()
                    verification_result = json.loads(json_content)
                else:
                    import re
                    json_matches = re.findall(r'(\{.*\})', verification_text, re.DOTALL)
                    if json_matches:
                        verification_result = json.loads(json_matches[0])
                    else:
                        raise ValueError("No JSON content found")
            except (json.JSONDecodeError, ValueError, IndexError):
                # If parsing fails, use original interpretation
                verification_result = {
                    "quality_assessment": "Could not verify quality",
                    "source_language": "unknown",
                    "interpretation_language": "unknown",
                    "language_match": True,
                    "refined_interpretation": interpretation_result
                }
        
        # Build the final result
        result = {}
        
        # Use the refined interpretation if available, otherwise use the original
        if "refined_interpretation" in verification_result and verification_result["refined_interpretation"]:
            for key in ["interpretation", "psychological_insight", "life_application", "guidance"]:
                if key in verification_result["refined_interpretation"]:
                    result[key] = verification_result["refined_interpretation"][key]
                elif key in interpretation_result:
                    result[key] = interpretation_result[key]
        else:
            # Use original interpretation
            for key in ["interpretation", "psychological_insight", "life_application", "guidance"]:
                if key in interpretation_result:
                    result[key] = interpretation_result[key]
        
        # Add original dream text
        result["dream"] = dream
        
        # Add symbols analysis
        result["symbols_analysis"] = symbols_analysis.get("symbols_analysis", [])
        
        # Add language information
        result["source_language"] = verification_result.get("source_language", "unknown")
        result["interpretation_language"] = verification_result.get("interpretation_language", "unknown")
        result["language_match"] = verification_result.get("language_match", True)
        result["quality_assessment"] = verification_result.get("quality_assessment", "No quality assessment available")
        
        return result 