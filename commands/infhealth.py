import minescript
import sys

# Basic Variables
plrName = minescript.player_name()

def godplr():
    minescript.execute(f"/effect give {plrName} instant_health infinite")