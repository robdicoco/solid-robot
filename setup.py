from setuptools import setup, find_packages

setup(
    name="morfeu",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.115.12",
        "uvicorn>=0.34.2",
        "google-genai>=1.15.0",
        "pydantic>=2.11.4",
        "python-dotenv>=1.1.0",
        "httpx>=0.28.1",
        "google-adk>=0.5.0",
    ],
    python_requires=">=3.8",
) 