from pathlib import Path

KNOWLEDGE_BASE_PATH = Path(__file__).parent.parent / "knowledge" / "aci_318_simplified.txt"

def get_code_clause(topic: str) -> str:
    """
    Retrieves a specific code clause from the knowledge base based on a topic.

    Args:
        topic: A string describing the topic, e.g., "minimum reinforcement".

    Returns:
        The relevant code clause as a string, or an error message if not found.
    """
    print(f"[Code Agent] Searching for clause related to: '{topic}'")
    try:
        with open(KNOWLEDGE_BASE_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Simple keyword search
        for i, line in enumerate(lines):
            if topic.lower() in line.lower():
                # Return the clause and the next few lines for context
                clause = "".join(lines[i:i+4]) # Return the line and next 3 lines
                print(f"[Code Agent] Found clause: {clause.strip()}")
                return clause

        return f"[Code Agent] No clause found for topic: {topic}"
    except FileNotFoundError:
        return f"[Code Agent] Error: Knowledge base file not found at {KNOWLEDGE_BASE_PATH}"

