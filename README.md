# Underwater glider trajectory drift analysis

Tools for estimating along-track drift and compass bias from underwater glider
navigation logs. This is engineering support for the 2023 glider deployment
campaign.

**This repository does not contain the hydrophone calibration analysis and is
unrelated to the calibration-drift manuscript.** It holds no acoustic data
processing code.

## Contents

- `src/gdrift/estimator.py` - dead-reckoning drift estimator
- `src/gdrift/compass.py` - compass bias correction
- `scripts/replay_mission.py`
- `configs/mission_2023.yaml`
