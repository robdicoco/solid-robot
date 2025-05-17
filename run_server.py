#!/usr/bin/env python3
import os
import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY environment variable is not set.")
        print("Please create a .env file with your Google API key or set it in your environment.")
        exit(1)
    
    # Start the server
    print("🚀 Starting Morfeu Dream Interpreter API Server")
    uvicorn.run("morfeu.main:app", host="0.0.0.0", port=8000, reload=True) 