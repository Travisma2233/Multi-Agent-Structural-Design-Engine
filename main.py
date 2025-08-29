from agents.task_agent import parse_design_task
from agents.code_agent import get_code_clause
from agents.calc_agent import perform_calculations
from agents.review_agent import review_results
from agents.report_agent import generate_report

def run_design_workflow(user_query: str):
    """Runs the full multi-agent design workflow."""
    
    # 1. Task Agent: Parse natural language
    try:
        task_params = parse_design_task(user_query)
        print("\n--- Task Parameters Extracted ---")
        print(task_params.model_dump_json(indent=2))
        print("-----------------------------------\n")
    except Exception as e:
        print(f"[Workflow] Error in Task Agent: {e}")
        return

    # 2. Code Agent: Retrieve relevant code clauses
    # For the MVP, we'll use a hardcoded topic based on a likely calculation.
    # A real version would have the Calc Agent or Review Agent flag which clauses are needed.
    governing_clause = get_code_clause(topic="minimum reinforcement")
    print("\n--- Code Clause Retrieved ---")
    print(governing_clause)
    print("-----------------------------\n")

    # 3. Calc Agent: Perform deterministic calculations
    calc_result = perform_calculations(task_params)
    print("\n--- Calculation Complete ---")
    print(calc_result.model_dump_json(indent=2))
    print("----------------------------\n")

    # 4. Review Agent: Cross-check results
    review_ok = review_results(calc_result)
    print("\n--- Review Complete ---")
    print(f"Review Passed: {review_ok}")
    print("-----------------------\n")

    if not review_ok:
        print("[Workflow] Halting due to review failure.")
        return

    # 5. Report Agent: Generate final report
    final_report = generate_report(task_params, calc_result, governing_clause)

    # Print the final output
    print("\n========= FINAL REPORT =========")
    print(final_report)
    print("==============================")


if __name__ == "__main__":
    # This is a sample query to test the full workflow.
    # Please replace the API key in `config.py` before running.
    sample_user_query = (
        "I need to design a simply supported rectangular beam. It has a span of 8 meters. "
        "The width is 300mm and the height is 500mm. "
        "It needs to support a dead load of 15 kN/m and a live load of 25 kN/m. "
        "Use concrete with f'c of 30 MPa and steel with fy of 420 MPa."
    )
    
    print("Starting design workflow for query:")
    print(f'"' + sample_user_query + '"\n')
    
    run_design_workflow(sample_user_query)
