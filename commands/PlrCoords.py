import minescript
import sys

# Get the player's name and coordinates
username = minescript.player_name()
player_x, player_y, player_z = minescript.player_position()
x, y, z = round(player_x), round(player_y), round(player_z)

print(f"{username} is located at {x}, {y}, {z}!")
