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
            
            Format your response as a JSON object with these fields:
            {
              "interpretation": "main poetic interpretation of the dream",
              "psychological_insight": "overall psychological perspective",
              "life_application": "how this might relate to the dreamer's life",
              "guidance": "gentle advice or wisdom based on the dream"
            }
        """,
        description="Agent that creates final poetic dream interpretation"
    )

    input_message = f"Dream: {dream_text}\nSymbol Analysis: {symbols_analysis}"
    # Execute the agent
    interpretation = call_agent(dream_interpreter, input_message)
    return interpretation

# Main DreamInterpreter class that orchestrates the three agents
class DreamInterpreter:
    def __init__(self):
        # Load dream symbols database
        symbols_path = Path(__file__).parent / "symbols.json"
        with open(symbols_path, "r") as f:
            self.symbols_database = json.load(f)["symbols"]

    def interpret_dream(self, dream: str) -> Dict:
        """Interpret a dream using the three-agent system."""
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
            result = json.loads(final_interpretation_text)
        except json.JSONDecodeError:
            # If not valid JSON, create a structured response
            result = {
                "interpretation": final_interpretation_text,
                "psychological_insight": "See interpretation above",
                "life_application": "See interpretation above",
                "guidance": "See interpretation above"
            }
        
        # Add original dream text
        result["dream"] = dream
        
        # Add symbols analysis if not present
        if "symbols_analysis" not in result:
            result["symbols_analysis"] = symbols_analysis.get("symbols_analysis", [])
        
        return result 