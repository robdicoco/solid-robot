# Morfeu Dream Interpreter

An AI-powered dream interpretation system built with Python, FastAPI, and Google's Generative AI.

## Overview

Morfeu is a sophisticated dream interpretation system that uses multiple AI agents to analyze and interpret dreams:

1. **Symbol Search Agent**: Identifies potential dream symbols and searches for their meanings
2. **Symbol Analyzer**: Analyzes symbols in the context of the dream and database
3. **Dream Interpreter**: Creates a poetic, insightful interpretation connecting all elements

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```
4. Create a `.env` file in the project root with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

### Command Line Interface

Run the dream interpreter from the command line:

```bash
python test_dream_client.py --interactive
```

Or provide a dream directly:

```bash
python test_dream_client.py --dream "I was flying over a clear blue ocean, feeling free and peaceful."
```

### API Server

Start the API server:

```bash
cd morfeu
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` with the following endpoints:
- `POST /interpret` - Interpret a dream
- `GET /health` - Health check endpoint
- `GET /docs` - API documentation (provided by FastAPI)

#### Example API Request

```bash
curl -X POST "http://localhost:8000/interpret" \
     -H "Content-Type: application/json" \
     -d '{"dream": "I was flying over a clear blue ocean, feeling free and peaceful."}'
```

## Project Structure

```
morfeu/
├── __init__.py
├── base_agent.py     # Helper functions for agents
├── dream_agent.py    # Dream interpretation agents
├── main.py           # FastAPI application
└── symbols.json      # Dream symbols database
tests/
└── test_dream_interpreter.py  # Unit tests
```

## Dream Symbol Database

The system includes a curated database of common dream symbols with their archetypal meanings and contextual interpretations. The agents use this database along with online searches to provide comprehensive dream analyses.