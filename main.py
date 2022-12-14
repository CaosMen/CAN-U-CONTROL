from websocket_server import WebsocketServer

# import maps
from maps import maps
from calibration import calibration

# import control
from control import convert_message, get_best_input

# Create a websocket server in port 6660
ws = WebsocketServer(port=6660)

# Global variables
last_input = 0

# Create a function to handle the connection
def new_client(client, server):
  print('New client connected and was given id: %d!' % client['id'])
  
  # Send a first input to the client
  server.send_message(client, str(0))

# Create a function to handle the disconnection
def client_left(client, server):
  print('Client (%d) disconnected!' % client['id'])

# Create a function to handle the message
def message_received(client, server, message):
  # Use global variables
  global last_input

  # Get the game, land, level, player, target, boxes, skulls
  land, level, player, target, boxes, skulls = convert_message(message)

  # Get the current map equation
  current_i = (land - 1) * 4 + (level - 1)
  current_map_eq = maps[current_i]
  current_map_calibration = calibration[current_i]

  # Set current target
  current_target = target

  # Get best input
  filter_input = current_map_calibration[0]
  breaks = current_map_calibration[1]
  step = current_map_calibration[2]
  
  best_input, best_distance = get_best_input(current_map_eq, breaks, step, player, current_target, skulls)
  filtered_input = filter_input * last_input + (1 - filter_input) * best_input

  # Set last input
  last_input = filtered_input

  server.send_message(client, str(filtered_input))

# Set the function to handle the connection
ws.set_fn_new_client(new_client)
ws.set_fn_client_left(client_left)
ws.set_fn_message_received(message_received)

# Run the websocket server
ws.run_forever()