import minescript
import sys

# Sign Text
sign_text = "Hello world!"
    

# Get player's coords
player_x, player_y, player_z = minescript.player_position()
x, y, z = round(player_x), round(player_y), round(player_z)

minescript.execute(f"/setblock {x} {y} {z} minecraft:oak_sign")
minescript.execute(f"/data merge block {x} {y} {z} """"{front_text:{messages:['{"text":"Hi!","color":"green"}','{"text":""}','{"text":""}','{"text":""}']}}""")
