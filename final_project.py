import time
import random
class Element:
    """
    Represents an element that the player can choose from
    
    Attributes:
    element(str):the name of the element
    hp(int): health points
    strength(int): power level
    luck(int): amount of luck for the hero
    """
    def __init__(self, element, hp, strength, luck):
        self.element=element
        self.hp=hp
        self.strength=strength
        self.luck=luck
        
    def choose_player(self):
        """
        Chooses a player for the class.
        
        Args:
        self(Element): an instantiated element.
        
        Raises:
        KeyError: invalid input
        
        Side effects:
        prints to console
        """
        print("\n Choose your Element: FIRE, WATER, or GRASS")
        
        ans= input().upper()
        string= ""
        if ans== "FIRE":
            self.element= "FIRE"
            print(f"""\n You have chosen {self.element}.
                       \n You have an advantage against GRASS.
                        \n You have a disadvantage against WATER.\n """)
            self.hp=100
            self.strength=10
        elif ans== "WATER":
            self.element="WATER"
            print(f"""\n You have chosen {self.element}.
                       \n You have an advantage against FIRE.
                        \n You have a disadvantage against GRASS.\n """)
            self.hp=100
            self.strength=10
        elif ans== "GRASS":
            self.element="GRASS"
            print(f"""\n You have chosen {self.element}.
                       \n You have an advantage against WATER.
                        \n You have a disadvantage against FIRE.\n """)
            
            self.hp=100
            self.hp=10
        else:
            raise KeyError("Invalid Player." 
                           +" Please select from the following:"
                           +" FIRE, WATER, GRASS")
        x= input("Feeling lucky? Y/N to roll the dice.\n").upper()
        if x=="N":
            print("Playing it safe I see. ")
        elif x=="Y":   
            time.sleep(.3)
            print("Let's see what you get! We roll the dice.\n ")
            time.sleep(2)
            print("Still rolling...\n")
            time.sleep(2)
            self.luck=random.randint(0,3)
            print(f"Your player has {self.luck} luck out of 3 \n")
        else:
            raise KeyError("Invalid input. Type 'Y' for Yes, or 'N' for No.")
        
            