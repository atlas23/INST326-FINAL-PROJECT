import time
import random
class Element:
    def __init__(self, element, hp, strength, luck, room):
        self.element=element
        self.hp=hp
        self.strength=strength
        self.luck=luck
        self.room=room
        self.opp=Opponent("Opponent_List.csv")
        
    def choose_player(self):
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
            print("Playing it safe I see.\n ")
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
            
        print("Select your room number, (1, 2, or 3)")
        b=input()
        if b == "1":
            self.room="DIAMOND"
            print(f"You will start in the {self.room} Room!\n")
            opp=Opponent("Opponent_List.csv")
            print("The monster you are facing has the following stats:\n " + str(opp))
            if self.luck!= None:
                x=random.randint(0,self.luck)
                print(x)
            else:
                x=random.randint(0,1)
                print(x)
            
        elif b == "2":
            self.room= "PLATINUM"
            print(f"You will start in the {self.room} Room!")
            
        elif b== "3":
            self.room="EMERALD"
            print(f"You will start in the {self.room} Room!")
        
#     def attack(self, player):
#         x=randint(0,self.luck)
#         print(x)
        
            
class Opponent:
    """
    Enemies player faces when selecting rooms
    
    attributes:
    filename(str) path to csv file containing opponent element, hp, and strength
    """
    
    def __init__(self, path="C:\\Users\\Henry\\Documents\\GitHub\\INST326-FINAL-PROJECT\\Opponent_List"):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                opponent= line.strip().split(",")
        self.opponent=opponent[0]
        self.element = opponent[1]
        self.hp = opponent[2]
        self.strength =opponent[3] 
        
    def __repr__(self):
        return f'Monster Name: {self.opponent}\n Element type: {self.element}\n Hitpoints: {self.hp}\n Strength: {self.strength}\n Your Luck: {self.luck}\n'
        
    
    def attack_method(self, player):
        """
        method for opponent to attack player
        
        args:
            player(Player object)
        side effect;
        """
    def element_advantage(self, player):
        if self.opponent=="FireFox" and player.element =="FIRE":
            self.strength*=1
            player.strength*=1
        elif self.opponent== "FireFox" and player.element=="WATER":
            self.strength*= 0.5
            player.strength*=1
        elif self.opponent== "FireFox" and player.element=="GRASS":
            self.strength*= 1.5
            player.strength*=1
        elif self.opponent =="WaterWeasel" and player.element=="FIRE":
            self.strength*=1.5
            player.strength*=1
        elif self.opponent=="WaterWeasel" and player.element=="WATER":
            self.strength*=1
            player.strength*=1
        elif self.opponent== "WaterWeasel" and player.element=="GRASS":
            self.strength*=0.5
            player.strength*=1
        elif self.opponent =="LeafEnt" and player.element=="FIRE":
            self.strength*=0.5
            player.strength*=1
        elif self.opponent=="LeafEnt" and player.element=="WATER":
            self.strength*=1.5
            player.strength*=1
        elif self.opponent== "LeafEnt" and player.element=="GRASS":
            self.strength*=1
            player.strength*=1
            