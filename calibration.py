import numpy as np

calibration = [
  # (filter, breaks, step) for each world
  # filter is the fraction of the last input that is used
  # breaks is the number of breaks in simulated path
  # step is the size of the step to vary between (-1, 1) for each break
  (0.85, 2, 1/2), # World 1, land 1
  (0.70, 3, 2/3), # World 1, land 2
  (0.85, 2, 1/4), # World 1, land 3
  (0.80, 3, 2/3), # World 1, land 4
  (0.95, 3, 2/3), # World 2, land 1
  (0.85, 2, 1/2), # World 2, land 2
  (0.35, 2, 1/4), # World 2, land 3
  (0.25, 2, 1/10), # World 2, land 4
  (0.95, 3, 2/3), # World 3, land 1
  (0.95, 3, 2/3), # World 3, land 2
  (0.95, 3, 2/3), # World 3, land 3
  (0.95, 3, 2/3), # World 3, land 4
  (0.95, 3, 2/3), # World 4, land 1
  (0.85, 3, 2/3), # World 4, land 2
  (0.1, 2, 1/5), # World 4, land 3
  (0.95, 3, 2/3), # World 4, land 4
]