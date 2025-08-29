from pydantic import BaseModel, Field
from typing import Optional

class MaterialProperties(BaseModel):
    """Defines the material properties for concrete and steel."""
    compressive_strength_concrete: float = Field(..., description="Concrete compressive strength (f'c) in MPa")
    yield_strength_steel: float = Field(..., description="Steel yield strength (fy) in MPa")

class BeamGeometry(BaseModel):
    """Defines the geometry of the beam."""
    width: float = Field(..., description="Width of the beam (bw) in mm")
    height: float = Field(..., description="Total height of the beam (h) in mm")
    length: float = Field(..., description="Length of the beam span in meters")
    effective_depth: Optional[float] = Field(None, description="Effective depth of the beam (d) in mm. Can be calculated if not provided.")

class Loads(BaseModel):
    """Defines the loads acting on the beam."""
    dead_load: float = Field(..., description="Distributed dead load (wD) in kN/m")
    live_load: float = Field(..., description="Distributed live load (wL) in kN/m")

class BeamDesignParameters(BaseModel):
    """The structured parameters for a beam design task, extracted from natural language."""
    materials: MaterialProperties
    geometry: BeamGeometry
    loads: Loads
    design_intent: str = Field("design", description="The user's intent, e.g., 'design', 'check'.")

class CalculationResult(BaseModel):
    """Stores the results from a calculation step."""
    ultimate_moment: float = Field(..., description="Ultimate bending moment (Mu) in kN-m")
    nominal_shear_strength: Optional[float] = Field(None, description="Nominal shear strength (Vc) in kN")
    # ... other results can be added here
