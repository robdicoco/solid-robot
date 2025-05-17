#!/usr/bin/env python3
import os
import json
import argparse
import re
from dotenv import load_dotenv
from morfeu.dream_agent import DreamInterpreter

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

def main():
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY environment variable is not set.")
        print("Please create a .env file with your Google API key or set it in your environment.")
        return
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Morfeu Dream Interpreter")
    parser.add_argument(
        "--dream",
        type=str,
        help="The dream text to interpret",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode (prompt for dream text)",
    )
    args = parser.parse_args()
    
    # Get dream text
    dream_text = ""
    if args.interactive or not args.dream:
        print("🌙 Welcome to Morfeu Dream Interpreter 🌙")
        print("Please enter your dream description (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if not line and lines:
                break
            lines.append(line)
        dream_text = "\n".join(lines)
    else:
        dream_text = args.dream
    
    if not dream_text.strip():
        print("❌ Error: Dream text cannot be empty.")
        return
    
    # Initialize interpreter
    interpreter = DreamInterpreter()
    
    # Process the dream
    print("\n🔮 Interpreting your dream...")
    print("This may take a moment as our AI agents analyze your dream...")
    
    # Call the interpreter
    result = interpreter.interpret_dream(dream_text)
    
    # Display results
    print("\n✨ Dream Interpretation ✨")
    print("=" * 60)
    print(f"💭 Your Dream: {dream_text[:100]}..." if len(dream_text) > 100 else f"💭 Your Dream: {dream_text}")
    print("=" * 60)
    
    # Display language information
    source_lang = result.get("source_language", "unknown")
    interp_lang = result.get("interpretation_language", "unknown")
    lang_match = result.get("language_match", True)
    
    print(f"\n🌐 Language: {source_lang.capitalize()} (Dream) → {interp_lang.capitalize()} (Interpretation)")
    
    if not lang_match:
        print("⚠️  Note: The interpretation has been translated to match your dream's language.")
    
    # Display quality assessment
    quality = result.get("quality_assessment", "No quality assessment available")
    print(f"\n💯 Quality Assessment: {quality}")
    
    print("\n📜 Interpretation:")
    print(clean_text(result.get("interpretation", "")))
    
    print("\n🧠 Psychological Insight:")
    print(clean_text(result.get("psychological_insight", "")))
    
    print("\n🌱 Life Application:")
    print(clean_text(result.get("life_application", "")))
    
    if "guidance" in result and result["guidance"]:
        print("\n🔆 Guidance:")
        print(clean_text(result.get("guidance", "")))
    
    # Write the full result to a file
    with open("dream_interpretation.json", "w") as f:
        json.dump(result, f, indent=2)
    
    print("\n💾 Full interpretation saved to dream_interpretation.json")

if __name__ == "__main__":
    main() 