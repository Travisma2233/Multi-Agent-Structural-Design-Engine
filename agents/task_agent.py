import instructor
from openai import OpenAI
from models.structural_models import BeamDesignParameters
from config import DEEPSEEK_API_KEY

# Patch the OpenAI client with instructor
# This enables response_model keyword argument to get structured output
client = instructor.patch(OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
))

def parse_design_task(user_query: str) -> BeamDesignParameters:
    """
    Uses an LLM to parse a natural language query into a structured BeamDesignParameters object.

    Args:
        user_query: The natural language query from the user.

    Returns:
        A BeamDesignParameters object populated with extracted data.
    """
    print(f"[Task Agent] Parsing user query: '{user_query}'")

    # Use the instructor-patched client to get a structured response
    task_parameters = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are an expert civil engineering assistant. Your role is to extract beam design parameters from the user's query and format them into a structured JSON object. The user is providing details for a structural beam. Identify all the geometric properties, material properties, and loads. Default units are MPa for strength, mm for dimensions, meters for length, and kN/m for distributed loads."
            },
            {
                "role": "user",
                "content": user_query
            }
        ],
        response_model=BeamDesignParameters,
        max_retries=3,
    )

    print("[Task Agent] Successfully parsed query.")
    return task_parameters
