"""
Class for Opponent
"""

class Opponent:
    """
    Enemies player faces when selecting rooms
    
    attributes:
    filename(str) path to csv file containing opponent element, hp, and strength
    """
    
    def __init__(self, element, hp, strength, luck):
        self.element = element
        self.hp = hp
        self.strength = strength
        self.luck = luck
    
    def attack_method(self, player):
        """
        method for opponent to attack player
        
        args:
            player(Player object)
        side effect;
        """
        