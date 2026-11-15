"""Compass bias estimation from paired GPS fixes."""
from __future__ import annotations

import numpy as np


def compass_bias(gps_heading: np.ndarray, glider_heading: np.ndarray) -> float:
    diff = np.angle(np.exp(1j * np.deg2rad(gps_heading - glider_heading)))
    return float(np.rad2deg(np.mean(diff)))
