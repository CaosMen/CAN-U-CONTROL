import math
import numpy as np

def convert_message(message):
  # Break message into parts and remove the last one
  parts = message.split(',')[0:-1]
  
  # Games that player has won
  game = int(parts[0])

  # Count of skulls
  skulls_count = game

  # Game current map
  land = int(parts[1])

  # Game current level
  level = int(parts[2])

  # Player position is the first part
  player = (float(parts[3]), float(parts[4]))

  # Target position is the second part
  target = (float(parts[5]), float(parts[6]))

  # Boxes positions
  boxes = []
  for i in range(7, len(parts) - 2 * skulls_count, 2):
    boxes.append((float(parts[i]), float(parts[i + 1])))
  
  # Skulls positions
  skulls = []
  for i in range(len(parts) - 2 * skulls_count, len(parts), 2):
    skulls.append((float(parts[i]), float(parts[i + 1])))

  return land, level, player, target, boxes, skulls

def calculate_distance(player, target):
  return math.sqrt((player[0] - target[0]) ** 2 + (player[1] - target[1]) ** 2)

def get_best_input(map, breaks, step, player, target, skulls, previous=[], best_input = 0, best_distance = math.inf, iteration = 100, dt = 0.02):
  for u in np.arange(-1, 1 + step, step):
    if breaks > 1:
      best_input, best_distance = get_best_input(
        map,
        breaks - 1,
        step,
        player,
        target,
        skulls,
        previous + [u],
        best_input,
        best_distance
      )
    else:
      # Set possible inputs
      possibles_inputs = previous + [u]
      
      # Set initial state
      next_position = player
      
      # Set initial distance
      smallest_distance = math.inf
      is_path_valid = True
      for i in range(iteration):
        # Get next input
        next_i = math.floor(i / iteration * len(possibles_inputs))
        next_u = possibles_inputs[next_i]
        
        # Get a small portion of velocity
        next_contribution = map(next_position[0], next_position[1], next_u)
        next_contribution = (next_contribution[0] * dt, next_contribution[1] * dt)

        # Get next position
        next_position = (next_position[0] + next_contribution[0], next_position[1] + next_contribution[1])

        # Get distance to target
        distance = calculate_distance(next_position, target) + 0.001 * i
        
        # Check if has skulls in the way
        for skull in skulls:
          if calculate_distance(next_position, skull) < 0.20:
            is_path_valid = False
            break

        # Check if the distance is smaller than the current best distance
        if distance < smallest_distance and is_path_valid:
          smallest_distance = distance

      # Check if the distance is smaller than the current best distance
      if smallest_distance < best_distance:
        best_input = possibles_inputs[0]
        best_distance = smallest_distance

  return best_input, best_distance