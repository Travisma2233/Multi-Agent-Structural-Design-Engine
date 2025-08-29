from models.structural_models import BeamDesignParameters, CalculationResult
from calculation.bending import calculate_ultimate_moment

def perform_calculations(params: BeamDesignParameters) -> CalculationResult:
    """
    Orchestrates the structural calculations based on the design parameters.

    Args:
        params: The structured beam design parameters.

    Returns:
        A CalculationResult object containing the results.
    """
    print(f"[Calc Agent] Performing calculations for a beam of length {params.geometry.length}m.")

    # --- Bending Calculation ---
    ultimate_moment = calculate_ultimate_moment(params.loads, params.geometry)
    print(f"[Calc Agent] Calculated Ultimate Moment (Mu): {ultimate_moment:.2f} kN-m")

    # --- Shear Calculation (Placeholder) ---
    # nominal_shear = calculate_nominal_shear(...)

    # --- Collate results ---
    result = CalculationResult(
        ultimate_moment=ultimate_moment
    )

    print("[Calc Agent] Calculations complete.")
    return result
