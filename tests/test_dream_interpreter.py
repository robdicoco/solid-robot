import pytest
from fastapi.testclient import TestClient
from morfeu.main import app
from morfeu.dream_agent import DreamInterpreter

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "morfeu-dream-interpreter"}

def test_interpret_dream():
    test_dream = "I was flying over a clear blue ocean, feeling free and peaceful."
    response = client.post(
        "/interpret",
        json={"dream": test_dream}
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "interpretation" in data
    assert "symbols_analysis" in data
    assert "psychological_insight" in data
    assert "life_application" in data
    assert "detected_symbols" in data
    
    # Check that flying and water symbols were detected
    symbols = [s["symbol"] for s in data["detected_symbols"]]
    assert "flying" in symbols
    assert "water" in symbols

def test_empty_dream():
    response = client.post(
        "/interpret",
        json={"dream": ""}
    )
    assert response.status_code == 422  # Validation error

def test_dream_interpreter_class():
    interpreter = DreamInterpreter()
    test_dream = "I was flying over a clear blue ocean"
    
    result = interpreter.interpret_dream(test_dream)
    
    assert isinstance(result, dict)
    assert "interpretation" in result
    assert "detected_symbols" in result
    assert len(result["detected_symbols"]) > 0 