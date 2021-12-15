import time
import random
import pandas as pd
import csv
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys
class Element:
    """
    Represents an Element player.
    
    Attributes:
    player(str): the name of the player
    element(str): the name of the element
    hp(int): the amount of hitpoints of the player
    strength(int): the strength level of the player
    room(int): the room number that the player chooses.
    luck(int): a random number from 0-3 if the player chooses to roll the dice.
    """
    def __init__(self):
        self.player=str()
        self.element=str()
        self.hp=int()
        self.strength=int()
        self.luck=int()
        self.room=int()
        
    def choose_player(self):
        """
        Provides a series of inputs asking the user about their desired 
        attributes in order to compare against their enemy type. Creates a 
        bar graph comparing the player's stats to the enemy's stats.
        
        Raises:
        ValueError(): incorrect input 
        """
        print("\n Choose your name.")
        self.player=input()
        
        
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
            print("The monster you are facing has the following stats:\n " + str(opp) + f'Your Luck: {self.luck}')
            if self.luck== 0:
                print("You are either really unlucky, or you should have rolled the dice.")
            else:
                print("Fortune favors the bold. Good thing you rolled the dice.")

            csvfile=pd.read_csv("Opponent_List.csv")
            df=pd.DataFrame(csvfile)
            df.loc[4, "Opponent"]= self.player
            df.loc[4, "Element"]=self.element
            df.loc[4, "HP"]= int(self.hp)
            df.loc[4,"Strength"]=int(self.strength)
            X=list(df["Opponent"])
            Y=list(df["HP"])
            plt.title("Opponent HP")
            plt.xlabel("Elements: Fire, Water, or Grass")
            plt.ylabel("HP")
            plt.bar(X,Y)
            plt.show()


            df2=pd.DataFrame(csvfile)
            df2.loc[4, "Opponent"]= self.player
            df2.loc[4, "Element"]=self.element
            df2.loc[4, "HP"]= int(self.hp)
            df2.loc[4,"Strength"]=int(self.strength)
            X2=list(df["Opponent"])
            Y2=list(df["Strength"])
            plt.title("Opponent Strength")
            plt.xlabel("Elements: Fire, Water, or Grass")
            plt.ylabel("Strength")
            plt.bar(X2,Y2)
            plt.show()
            print("Here's how you compare to your other opponents...")
            
        elif b == "2":
            self.room= "PLATINUM"
            print(f"You will start in the {self.room} Room!")
            opp=Opponent("Opponent_List.csv")
            print("The monster you are facing has the following stats:\n " + "Monster Name: FireFox \n Element Type: Fire \n HitPoints: 12 \n Strength: 22 \n" + f' Your Luck: {self.luck}')            
            if self.luck== 0:
                print("You are either really unlucky, or you should have rolled the dice.")
            else:
                print("Fortune favors the bold.")
            csvfile=pd.read_csv("Opponent_List.csv")
            df=pd.DataFrame(csvfile)
            df.loc[4, "Opponent"]= self.player
            df.loc[4, "Element"]=self.element
            df.loc[4, "HP"]= int(self.hp)
            df.loc[4,"Strength"]=int(self.strength)
            X=list(df["Opponent"])
            Y=list(df["HP"])
            plt.title("Opponent HP")
            plt.xlabel("Elements: Fire, Water, or Grass")
            plt.ylabel("HP")
            plt.bar(X,Y)
            plt.show()


            df2=pd.DataFrame(csvfile)
            df2.loc[4, "Opponent"]= self.player
            df2.loc[4, "Element"]=self.element
            df2.loc[4, "HP"]= int(self.hp)
            df2.loc[4,"Strength"]=int(self.strength)
            X2=list(df["Opponent"])
            Y2=list(df["Strength"])
            plt.title("Opponent Strength")
            plt.xlabel("Elements: Fire, Water, or Grass")
            plt.ylabel("Strength")
            plt.bar(X2,Y2)
            plt.show()
            print("Here's how you compare to your other opponents...")
            
        elif b== "3":
            self.room="EMERALD"
            print(f"You will start in the {self.room} Room!")
            opp=Opponent("Opponent_List.csv")
            print("The monster you are facing has the following stats:\n " + "Monster Name: WaterWeasel \n Element Type: Water \n HitPoints: 20 \n Strength: 14 \n" + f' Your Luck: {self.luck}')            
            if self.luck== 0:
                print("You are either really unlucky, or you should have rolled the dice.")
            else:
                print("Fortune favors the bold.")
            csvfile=pd.read_csv("Opponent_List.csv")
            df=pd.DataFrame(csvfile)
            df.loc[4, "Opponent"]= self.player
            df.loc[4, "Element"]=self.element
            df.loc[4, "HP"]= int(self.hp)
            df.loc[4,"Strength"]=int(self.strength)
            X=list(df["Opponent"])
            Y=list(df["HP"])
            plt.title("Opponent HP")
            plt.xlabel("Elements: Fire, Water, or Grass")
            plt.ylabel("HP")
            plt.bar(X,Y)
            plt.show()


            df2=pd.DataFrame(csvfile)
            df2.loc[4, "Opponent"]= self.player
            df2.loc[4, "Element"]=self.element
            df2.loc[4, "HP"]= int(self.hp)
            df2.loc[4,"Strength"]=int(self.strength)
            X2=list(df["Opponent"])
            Y2=list(df["Strength"])
            plt.title("Opponent Strength")
            plt.xlabel("Elements: Fire, Water, or Grass")
            plt.ylabel("Strength")
            plt.bar(X2,Y2)
            plt.show()
            print("Here's how you compare to your other opponents...")
           

        
        
            
class Opponent:
    """
    Represents an enemy for the Element class to fight.
    
    attributes:
    opponent(str): the name of the opponent monster
    element(str): the name of the monster's element
    hp(str): the amount of health of the monster
    strength(str): the strength of the monster
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
        return f'Monster Name: {self.opponent}\n Element type: {self.element}\n Hitpoints: {self.hp}\n Strength: {self.strength}\n '
        
        
def main(path):
    Element.choose_player(path)
    

x=Element()
main(x)
    