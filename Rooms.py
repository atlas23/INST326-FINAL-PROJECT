from random import choice

class Rooms:
    """
    
    This class lets the player choose what battle rooms they want to start
    and it randomly selects the next room for the player to go. The player
    will have a selection of 3 numbers 0,1,2 that represent the battle room
    that the player
    
    
    Attributes:
        self: default value
        player(str): player chosen for the game
        input(int): the number the player selects the room to start in
    """
    
    def __init__(self,player, room_num):
        """sets the attributes"""
        self.player = player
        self.room_num = room_num
        
        
    def room_selection (self,choice):
        """This method decides the battle room that the player will start 
        the game from. The player will have 3 choices of number to pick from 
        where:
        0 is the Diamond Battle Room selection
        1 is the Platinum Battle Room selection
        2 is the Emerald Battle Room selection

        Args:
            choice (int): The players selection for the starting room
        """
        
        print("Select a room number: 0,1 or 2")
        
        room_num = input()
        
        
        # selection = choice(0,1,2)
        
        if room_num == 0:
            print("You will start in the Diamond Room!")
            
        elif room_num == 1:
            print("You will start in the Platinum Room!")
        
        elif room_num == 2:
            print("You will start in the Emerald Room!")
        
        else:
            print("Room number is incorrect. Try again!")
            
        
        
    def diamond_room(self):
        """ The first choice of rooms the player will land in. 
        """
        
        print ("Welcome to the Diamond Battle Room!")
        
    
    def platinum_room(self):
        
        print ("Welcome to the Platinum Battle Room!")

    def emerald_room(self):
        
         print ("Welcome to the Emerald Battle Room!")     
        
        
    
    
    