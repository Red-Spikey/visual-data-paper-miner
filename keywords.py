"""
keywords.py

This module contains the domain-specific keyword vocabulary used by the 
Figure-Centered Literature Mining Pipeline for both Stage 1 (Caption Filtering) 
and Stage 2 (OCR Validation).

Current Domain: Aerodynamics, Fluid Mechanics, and Computational Fluid Dynamics (CFD)
"""

TARGET_KEYWORDS = [
    # Flow & regime
    'mach', 'mach number', 'reynolds', 'reynolds number',
    'compressible', 'incompressible',
    'supersonic', 'hypersonic', 'subsonic',

    # Aerodynamic quantities
    'lift', 'drag', 'lift coefficient', 'drag coefficient',
    'pressure', 'pressure coefficient', 'cp',
    'skin friction', 'shear stress',

    # Flow physics
    'boundary layer', 'flow separation', 'reattachment',
    'shock', 'shock wave',
    'wake', 'vortex', 'vorticity',
    'turbulence', 'laminar',

    # Geometry / bodies
    'airfoil', 'aerofoil', 'wing', 'delta wing',
    'nozzle', 'inlet', 'jet',

    # CFD / simulation
    'cfd', 'numerical simulation',
    'rans', 'les', 'dns',
    'k-epsilon', 'k-omega',
    'mesh', 'grid', 'solver',

    # Visualization / plots
    'contour', 'streamline', 'velocity field',
    'pressure field', 'mach contour',
    'velocity profile',

    # Experimental
    'wind tunnel', 'experimental validation'
]

# Optional: Convert to lowercase in advance to ensure the filtering logic 
# remains strictly case-insensitive during execution.
TARGET_KEYWORDS = [keyword.lower() for keyword in TARGET_KEYWORDS]
