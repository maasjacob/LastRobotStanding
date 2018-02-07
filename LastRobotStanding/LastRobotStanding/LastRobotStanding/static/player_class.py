class user_customization_info(object):
    color = [0.0,0.0,0.0]
    name = ""
    def __init__(self,color,name):
        self.color = color
        self.name = name
    pass

class public_game_state(object):
    board = 0
    player_states = []

    def __init__(self,customization_info):
        pid = 0
        for new_player_info in customization_info:
            new_player = public_player_state(new_player_info.color,
                                             pid,
                                             new_player_info.name)
            pid = pid+1
        board = board_state()#TODO: Update this once board_state is defined
        pass
    pass

class private_game_state(object):
    pub_game_ref = 0
    prv_player_state = 0
    def __init__(self,color,deck_idx,pub_game_ref):
        self.prv_player_state = private_player_state(color,self,deck_idx)
        self.pub_game_ref = pub_game_ref

class private_player_state(object):
    deck_idx = 0
    game_ref = 0

    pub_state = 0
    prv_hand = 0

    def __init__(self,color,game_ref,deck_idx):
        self.pub_state = public_player_state(color)
        self.prv_hand = hand(self)
        self.game_ref = game_ref
        self.deck_idx = deck_idx
        pass
    def deck_ref():
        return self.game_ref.deck[self.deck_idx]
    pass

class public_player_state(object):
    default_max_hp = 20
    default_init_hp = 15 #TODO: make these const if possible

    player_id = 0
    name = ""
    color = [0.5,0.0,0.0]
    hp = 0
    active_mods = [] #How do we make it so that a modifier and a card that don't know each other can interact?
    carried_items = []
    def __init__(self,color,pid,name):
        self.hp = self.default_init_hp
        self.color = color
        self.player_id = pid
        self.name = name
        pass
    pass