import minescript
import sys
from time import sleep

# Get the player's position:
player_x, player_y, player_z = minescript.player_position()
x, y, z = round(player_x), round(player_y), round(player_z)

# Get the type of block directly beneath the player:
block_type = minescript.getblock(x, y - 1, z)
block_type = block_type.replace("minecraft:", "").split("[")[0]

sign_text = (
    """{Text1:'{"text":"%s"}',Text2:'{"text":"at"}',Text3:'{"text":"%d %d %d"}'}""" %
    (block_type, x, y - 1, z))

# Script argument, passed from Minecraft like "\example 5"
rotation = int(sys.argv[1]) if len(sys.argv) > 1 else 0
if rotation < 0 or rotation > 15:
  raise ValueError(f"Param not an integer between 0 and 15: {rotation}")

# Create a sign then set text on it:
minescript.execute(f"/setblock {x} {y} {z} minecraft:birch_sign[rotation={rotation}]")
minescript.execute(f"/data merge block {x} {y} {z} {sign_text}")

sleep(0.25)
# Text written to stderr appears locally in Minecraft chat GUI and is not visible
# to other players. To send a chat message that's visible to other players, remove
# the file=sys.stderr param (default is file=sys.stdout).
print(f"Created sign at {x} {y} {z} over {block_type}")
