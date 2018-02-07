class hand(object):
    cards_list = []
    player_ref = 0
    tmp_hand_lim = 0
    tmp_draw_lim = 0
    default_hand_lim = 7 #can this be const somehow?
    default_draw_lim = 2 #ditto
    def __init__(self,player_ref):
        self.tmp_hand_lim = self.default_hand_lim
        self.tmp_draw_lim = self.default_draw_lim
        self.player_ref = player_ref
        self.cards_list = self.deck_ref().draw(self.tmp_hand_lim)
    def deck_ref(self):
        return self.player_ref.game_ref.deck[player_ref.deck_idx]
    def activate(self,card_idx):
        assert(card_idx>=0 and card_idx<len(cards_list))
        cards_list[card_idx].activate(self)
    def discard(self,card_idx):
        #Most cards will just use the base class discard function. But if a
            #card should drop an item or have other effect when discarded, 
            #allow for that
        assert(card_idx>=0 and card_idx<len(cards_list))
        self.deck_ref().discard(cards_list[card_idx]) #WARN: I'm not sure I can write to data this way
        cards_list.remove(card_idx) #WARN: I don't think this does what I intend it to

#decklib is a library of sorts that has unique card information. The cards it contains should have self-containing behavior
class deck_base(object):
    draw_cards_list = []
    discard_cards_list = []
    def __init__(self,decklib_list):
        for deck in decklib_list:
            self.draw_cards_list = self.draw_cards_list+deck.cards_list
        self.shuffle()
        pass
    def shuffle(self):
        #TODO: randomly sort self.cards_list
        pass
    def draw(self,count):
        new_cards = []
        for i in range(0,count):
            if(len(self.draw_cards_list)>0):
                new_cards.append(draw_cards_list.pop())
            else:
                #CONSIDER: sending some signal that the deck is empty
                pass
        return new_cards
    def discard(self,card):
        discard_cards_list.append(card)
        pass

