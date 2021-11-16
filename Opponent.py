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
    class Opponent:
        """
    Enemies player faces when selecting rooms

    attributes:
    filename(str) path to csv file containing opponent element, hp, and strength
    """

    def init(self, path="/Users/anto/Documents/GitHub/Text-Based_Game/INST326-FINAL-PROJECT/Opponent_List.csv"):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                opponent= line.strip().split(",")
        self.opponent=opponent[0]
        self.element = opponent[1]
        self.hp = opponent[2]
        self.strength =opponent[3] 
        self.luck = opponent[4]

    def element_advantage(self, player):
        """
        Creates element advantage function to apply damage multipliers based on identifying element for the player and opponent
        
        args:
            strength(int): base strength of player and the multiplier added based on elemental matchup
            element(str): player and opponent's identifying element
        """
        if self.opponent=="FireFox" and player.element =="FIRE":
            self.strength=1
            player.strength=1
        elif self.opponent== "FireFox" and player.element=="WATER":
            self.strength= 0.5
            player.strength=1
        elif self.opponent== "FireFox" and player.element=="GRASS":
            self.strength= 1.5
            player.strength=1
        elif self.opponent =="WaterWeasel" and player.element=="FIRE":
            self.strength=1.5
            player.strength=1
        elif self.opponent=="WaterWeasel" and player.element=="WATER":
            self.strength=1
            player.strength=1
        elif self.opponent== "WaterWeasel" and player.element=="GRASS":
            self.strength=0.5
            player.strength=1
        elif self.opponent =="LeafEnt" and player.element=="FIRE":
            self.strength=0.5
            player.strength=1
        elif self.opponent=="LeafEnt" and player.element=="WATER":
            self.strength=1.5
            player.strength=1
        elif self.opponent== "LeafEnt" and player.element=="GRASS":
            self.strength=1
            player.strength=1
    
    def attack_method(self, player):
        """
        method for opponent to attack player
        
        args:
            player(Player object)
        side effect:
        """
    
        