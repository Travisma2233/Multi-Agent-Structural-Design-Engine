# Multi-Agent Structural Design Engine

This project is a prototype of a structural design engine based on a "multi-agent + code knowledge" architecture. It aims to explore a workflow that combines the natural language understanding capabilities of Large Language Models (LLMs) with the precision of deterministic engineering calculations.

## Core Concepts

- **Code-First**: Engineering design codes (e.g., ACI 318, Eurocode) are treated as the source of truth. The role of AI agents is to understand intent, plan workflows, and interpret results, while all core calculations are performed by validated, deterministic modules.
- **Traceability**: Every step of the design process—from parameter extraction to final calculations—is transparent and backed by a clear source, including references to specific code clauses and formulas.
- **Extensibility**: The system is designed to be modular, allowing for the easy addition of new calculation modules (e.g., for columns, slabs, foundations) or new design code systems.

## How It Works

The engine processes user requests through a collaborative pipeline of five distinct agents:

`User's Natural Language Query` -> `[1. Task Agent]` -> `[2. Code Agent]` -> `[3. Calc Agent]` -> `[4. Review Agent]` -> `[5. Report Agent]` -> `Final Design Report`

1.  **Task Agent**: Parses the user's natural language query and converts it into a structured set of design parameters (e.g., materials, geometry, loads).
2.  **Code Agent**: Retrieves relevant design code clauses from a knowledge base based on the current design task.
3.  **Calc Agent**: Executes deterministic calculation functions using the structured parameters, strictly adhering to engineering formulas (e.g., for bending moment, shear force).
4.  **Review Agent**: Cross-checks the calculation results for reasonableness and flags any potential issues or values that fall outside of standard limits.
5.  **Report Agent**: Assembles the inputs, calculation results, and code citations into a clean, human-readable engineering report.

## Project Structure

```
.
├── agents/                 # Contains the logic for each agent
│   ├── task_agent.py
│   ├── code_agent.py
│   ├── calc_agent.py
│   ├── review_agent.py
│   └── report_agent.py
├── calculation/            # Deterministic engineering calculation modules
│   └── bending.py
├── knowledge/              # Knowledge base for design codes
│   └── aci_318_simplified.txt
├── models/                 # Pydantic data models for structured data
│   └── structural_models.py
├── .gitignore              # Specifies files for Git to ignore
├── config.py               # Configuration file (for API keys)
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/design-agent.git
cd design-agent
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then, run the following command to install the necessary packages:
```bash
pip install -r requirements.txt
```

### 3. Configure the API Key
This project requires an LLM API key to power the `Task Agent`.

1.  Create a new file named `config.py`.
2.  In this file, add your API key as follows:

```python
# config.py
DEEPSEEK_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx" # Replace with your valid API key
```
**Important**: The `config.py` file is listed in `.gitignore` to prevent your secret key from being committed to a public repository.

### 4. Run the Engine
Once everything is set up, run the main script from your terminal:
```bash
python main.py
```
You will see logs from each agent as they work, followed by a final, formatted design report printed to the console.

## Roadmap

- [ ] **Enhance Calculation Capabilities**:
    - [ ] Implement shear design calculations (`Vc`, `Vs`).
    - [ ] Implement calculation for required reinforcement area (`As`).
    - [ ] Add serviceability checks for deflection and crack width.
- [ ] **Upgrade Code Retrieval**:
    - [ ] Implement a full RAG (Retrieval-Augmented Generation) system using a vector database (e.g., FAISS) for more accurate and semantic code clause retrieval.
- [ ] **Improve Robustness**:
    - [ ] Write unit tests (`pytest`) for the `calculation` module to ensure accuracy.
    - [ ] Add support for a "Check" mode, where the user provides the design and the engine verifies its compliance.
- [ ] **Expand Knowledge Base**:
    - [ ] Ingest more comprehensive versions of design codes.
    - [ ] Add support for other code systems (e.g., Eurocode, GB).

## Contributing

Contributions are welcome! If you have ideas, suggestions, or code improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).