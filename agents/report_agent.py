from models.structural_models import BeamDesignParameters, CalculationResult

def generate_report(params: BeamDesignParameters, result: CalculationResult, clause: str) -> str:
    """
    Generates a human-readable report from the design and calculation data.

    Args:
        params: The original design parameters.
        result: The calculation results.
        clause: The relevant code clause.

    Returns:
        A formatted string containing the final report.
    """
    print("[Report Agent] Generating final report...")

    report = f"""
    ==============================================
    STRUCTURAL DESIGN REPORT (PRELIMINARY)
    ==============================================

    1. INPUT PARAMETERS
    ----------------------------------------------
    Design Intent: {params.design_intent}

    1.1. Geometry:
    - Beam Length: {params.geometry.length} m
    - Beam Width (bw): {params.geometry.width} mm
    - Beam Height (h): {params.geometry.height} mm

    1.2. Materials:
    - Concrete Strength (f'c): {params.materials.compressive_strength_concrete} MPa
    - Steel Yield Strength (fy): {params.materials.yield_strength_steel} MPa

    1.3. Loads:
    - Dead Load: {params.loads.dead_load} kN/m
    - Live Load: {params.loads.live_load} kN/m

    2. CALCULATION RESULTS
    ----------------------------------------------
    - Ultimate Bending Moment (Mu): {result.ultimate_moment:.2f} kN-m

    3. GOVERNING CODE CLAUSE
    ----------------------------------------------
    {clause.strip()}

    ==============================================
    Disclaimer: This is an automated, preliminary report.
    Always verify with a qualified professional engineer.
    ==============================================
    """
    print("[Report Agent] Report generation complete.")
    return report
