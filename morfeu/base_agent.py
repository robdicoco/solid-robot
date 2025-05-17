from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # To create content (Content and Part)

import textwrap # To better format text output
# from IPython.display import display, Markdown  # To make HTTP requests
import warnings


# Helper function that sends a message to an agent via Runner and returns the final response
def call_agent(agent: Agent, message_text: str) -> str:
    # Creates an in-memory session service
    session_service = InMemorySessionService()
    # Creates a new session (you can customize IDs as needed)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Creates a Runner for the agent
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Creates the input message content
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Asynchronously iterates through the events returned during agent execution
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response