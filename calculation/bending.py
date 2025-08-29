from models.structural_models import Loads, BeamGeometry

def calculate_ultimate_moment(loads: Loads, geometry: BeamGeometry) -> float:
    """
    Calculates the ultimate bending moment (Mu) for a simply supported beam.
    Uses the standard load combination 1.2D + 1.6L.

    Args:
        loads: The dead and live loads on the beam.
        geometry: The geometry of the beam.

    Returns:
        The ultimate bending moment (Mu) in kN-m.
    """
    # Load combination (e.g., ACI 318)
    factored_load = 1.2 * loads.dead_load + 1.6 * loads.live_load  # kN/m

    # Moment for a simply supported beam (w * L^2 / 8)
    ultimate_moment = (factored_load * (geometry.length ** 2)) / 8.0  # kN-m

    return ultimate_moment
