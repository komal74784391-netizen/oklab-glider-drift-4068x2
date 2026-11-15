"""Dead-reckoning drift estimation from dive logs."""
from __future__ import annotations

import numpy as np


def estimate_drift(heading_deg: np.ndarray, speed: np.ndarray, dt: float = 60.0) -> np.ndarray:
    rad = np.deg2rad(heading_deg)
    east = np.cumsum(np.cos(rad) * speed * dt)
    north = np.cumsum(np.sin(rad) * speed * dt)
    return np.stack([east, north], axis=1)
