

class base_floor_object(): #inherit from base_special_object
    pickup_able = 0
    destructable = 0
    is_card = 0
    card_id = 0
    hp = 0
    
class base_wall(): #inherit from base_spatial_object
    image_ref = ""

class base_cell_state(): #inherit from base_spatial_object
    pass

class base_spatial_object():
    complete_name = ""
    hashed_name = 0
    game_ver = 0.0
    image_ref = ""
    blocks_LOS = 0
    blocks_movement = 0

class cell():
    y = 0
    x = 0
    n_wall = 0
    w_wall = 0

    e_wall = 0
    s_wall = 0
    
    cell_state = 0
    objects_on_floor = []

    def __init__(self,x,y):
        self.x = x
        self.y = y
        if(self.x!=0):
            n_wall = 0
        if(self.y!=0):
            w_wall = 0

    pass

class sector():
    cells = []
    
    pass

class board_state(object):
    sectors = []

    pass




