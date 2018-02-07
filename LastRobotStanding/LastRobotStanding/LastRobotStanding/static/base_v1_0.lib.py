#note: when importing a library, check for any name conflicts. Maybe somehow 
#have libraries indicate which items they are looking for

#########
##WALLS##
#########

class wall_firewall_destroyed(): #inherit from base_wall
    game_ver = 1.0
    name = "destroyed_fire_wall"
    image_ref = "tiles/fire_wall_destroyed.png"
    blocks_LOS = False
    blocks_movement = False


class wall_normal_destroyed(): #inherit from base_wall
    game_ver = 1.0
    name = "destroyed_wall"
    image_ref = "tiles/wall_destroyed.png"
    blocks_LOS = False
    blocks_movement = False

class wall_firewall(): #inherit from base_wall
    game_ver = 1.0
    name = "fire_wall"
    image_ref = "tiles/firewall.png"
    blocks_LOS = False
    blocks_movement = False
    ##should have exit/enter/pass events
    #these events should apply to projectiles as well

class wall_normal(): #inherit from base_wall
    game_ver = 1.0
    name = "normal_wall"
    image_ref = "tiles/wall.png"
    blocks_LOS = True
    blocks_movement = True

#########
##CELLS##
#########

class cell_empty(): #inherit from base_cell_state
    game_ver = 1.0
    name = "empty_cell"
    image_ref = "tiles/tile_map.png"
    blocks_LOS = False
    blocks_movement = False

class power_supply(): #inherit from base_floor_object
    game_ver = 1.0
    name = "power_supply"
    color = 0
    pickup_able = 1
    is_card = 0

class melted_hallway(): #inherit from base_cell_state
    game_ver = 1.0
    name = "melted_hallway"
    image_ref = "tiles/fused.png"
    blocks_LOS = True
    blocks_movement = True

class oil_slick(): #inherit from base_cell_state
    game_ver = 1.0
    name = "oil_slick"
    image_ref = "tiles/oil_slick.png"
    blocks_LOS = False
    blocks_movement = False
    ##some methods here to generically handle "action upon entering/exiting" events?

class player_homebase(): #inherit from base_cell_state
    game_ver = 1.0
    name = "homebase"
    color = 0
    blocks_LOS=False
    blocks_movement = False
    def __init__(self,color): ##WARN: We have a contradiction here. Artwork is fixed but colors are RGB.
        #In the meantime, we'll use fixed colors for here
        if(color==0):
            image_ref = "tiles/base_1.png"
        if(color==1):
            image_ref = "tiles/base_2.png"
        if(color==2):
            image_ref = "tiles/base_3.png"
        if(color==3):
            image_ref = "tiles/base_4.png"
        self.color = color

###########
##OBJECTS##
###########

class fire_turret():
    game_ver = 1.0
    name = "fire_turret"
    owner = 0
    pickup_able = False
    blocks_LOS = False
    blocks_movement = False
    ##take damage method (reflect damage, cause event upon death etc)
    hp = 5#made up number

class water_turret():
    game_ver = 1.0
    name = "water_turret"
    owner = 0 #so that the owner is not subject to friendly fire
    pickup_able = False
    blocks_LOS = False
    blocks_movement = False
    ##take damage method (reflect damage, cause event upon death etc)
    hp = 5#made up number


##################
##PLAYER EFFECTS##
##################

#magnetic restraint
#stunned
#dead
#carbon
#big
#little