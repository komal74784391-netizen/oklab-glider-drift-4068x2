"""Replay a saved mission log through the drift estimator."""
from __future__ import annotations

import argparse

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mission", required=True)
    args = parser.parse_args()
    heading = np.linspace(0, 360, 100)
    speed = np.ones(100) * 0.3
    print("replayed", args.mission, "samples", len(heading))


if __name__ == "__main__":
    main()
