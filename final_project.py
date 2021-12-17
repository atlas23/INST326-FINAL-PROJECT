import time
import random
import pandas as pd
import csv
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys
"""
Our inspiration for the program derives from the following source:

Thecodingpie. (n.d.). 
Make your own text based adventure game in python3: Thecodingpie.
thecodingpie RSS. 
Retrieved December 15, 2021, from 
https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3
"""
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
        Asks a series of questions to the user to determine their player 
        attributes and confrontation with a monster element.
        
        Side effects: 
        prints to console
        """
        print("\n Choose your name.")
        choice=input()
        self.player=choice
        print("\n Choose your Element: FIRE, WATER, or GRASS")
        
        ans= input().upper()
        
        if ans== "FIRE":
            self.element= "FIRE"
            print(f"""\n You have chosen {self.element}.
                       \n You have an advantage against GRASS.
                        \n You have a disadvantage against WATER.\n """)
            self.hp=random.randint(10,50)
            self.strength=random.randint(5,30)
        elif ans== "WATER":
            self.element="WATER"
            print(f"""\n You have chosen {self.element}.
                       \n You have an advantage against FIRE.
                        \n You have a disadvantage against GRASS.\n """)
            self.hp=random.randint(10,50)
            self.strength=random.randint(5,30)
        elif ans== "GRASS":
            self.element="GRASS"
            print(f"""\n You have chosen {self.element}.
                       \n You have an advantage against WATER.
                        \n You have a disadvantage against FIRE.\n """)
            
            self.hp=random.randint(10,50)
            self.strength=random.randint(5,30)
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
            bars=plt.bar(X,Y)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .05, yval)
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
            bars=plt.bar(X2,Y2)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .05, yval)
            plt.show()
            print("Here's how you compare to your other opponents...")
            self.survey_method()
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
            bars=plt.bar(X,Y)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .05, yval)
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
            bars=plt.bar(X2,Y2)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .05, yval)
            plt.show()
            print("Here's how you compare to your other opponents...")
            self.survey_method()
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
            bars=plt.bar(X,Y)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .05, yval)
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
            bars=plt.bar(X2,Y2)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .05, yval)
            plt.show()
            print("Here's how you compare to your other opponents...")
            self.survey_method()
    def survey_method(self):
        """
            This method will decide whether the player or opponent will move
            on to the next room. They will be asked a series of triva 
            questions to 
            answer and if they get them right,  
            
            Side effects: prints to console
        """ 
        player_pts = 0
        print(f"\nWelcome to the {self.room} room! You will answer a series of trivia questions to determine which room you'll go next")
        print("\n You must answer all 3 questions right to move on to the next room")
         
        print("\nPlease choose number: 1,2 or 3: ") 
        
        player_choice = input() 
        
        if player_choice == "1" or player_choice == "2" or player_choice =="3": 
            

            print("\nSelect a category number: 1)Technology 2) Pop Culture 3) Cars 4)Geography ")
            
            category = input().upper()
            
            if category == "1":
                print("\nTechnology Question #1: What was Twitter's original name? ")
                ans = input().upper()
                
                if ans == "TWTTR":
                    print("\nCorrect! Next Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: TWTTR") 
                    print("Your points:"+ str(player_pts))   
                
                    
                ans2 = input("\nTechnology Question #2: What's the shortcut for the “copy” function on most computers? ").upper()
        
                if ans2 == "CTRL C":
                    print("\nCorrect Again! Final Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: CTRL C") 
                    print("Your points:"+ str(player_pts))   
                    
                print("\nTechnology Question #3: Name an electric vehicle that is popular today: ")
                ans3 = input().upper()                
                if ans3 == "TESLA":
                    print("\n Correct!.\n")
                    player_pts +=1
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: TESLA") 
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))

                            
             
            elif category == "2":
                print("\nPop Culture Question #1: Which Avenger is the only one who could calm the Hulk down? ")
                a1 = input().upper()
                
                if a1 == "BLACK WIDOW":
                    print("\nCorrect! Next Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: Black Widow") 
                    print("Your points:"+ str(player_pts))   
                    
                a2 = input("\nPop Culture Question #2: What does DC stand for? ").upper()
                    
                if a2 == "DETECTIVE COMICS":
                    print("\nCorrect! Final Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    print("Wrong. Hint: DECTECTIVE COMICS") 
                    player_pts-=1
                    print("Your points:"+ str(player_pts))    
                    
                a3 = input("\nPop Culture Question #3: Which actor appeared in films “Face Off” and “Ghost Rider”? ").upper()
                
                if a3 == "NICHOLAS CAGE":
                    print("\n Correct!\n")
                    player_pts +=1
                    print(f"Total player points: {player_pts}\n")
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))
                else:
                    print("Wrong. Hint: Nicholas Cage")
                    player_pts-=1
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts)) 

                        
            elif category == "3":
                print("\nCar Question #1: What animal is found on the car logo of a Ford Mustang: ")
                c1 = input().upper()
                
                if c1 == "HORSE":
                    print("\nCorrect! Next Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: Horse") 
                    print("Your points:"+ str(player_pts)) 
                    
                c2 = input("\nCar Question #2: Which company owns Bugatti, Lamborghini. Audi, Porsche, and Ducati? ").upper()
                    
                if c2 == "VOLKSWAGEN":
                    print("\nCorrect! Final Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: VOLKSWAGEN") 
                    print("Your points:"+ str(player_pts)) 
                    
                c3 = input("What does BMW stand for (in English)? ").upper()
                
                if c3 == "BAVARIAN MOTOR WORKS":
                    print("\n Correct!\n")
                    player_pts +=1
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: BAVARIAN MOTOR WORKS") 
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))  
                            
                            
                        
            elif category == "4": 
                print("\nGeography Question #1: What is the name of the world's longest river? ")
                g1 = input().upper()
                
                if g1 == "NILE":
                    print("\nCorrect! Next Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: Nile") 
                    print("Your points:"+ str(player_pts))
                    
                g2 = input("\nWhich American state is the largest (by area)? ").upper()
                
                if g2 == "ALASKA":
                    print("\nCorrect! Final Question")
                    player_pts +=1
                    print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: ALASKA") 
                    print("Your points:"+ str(player_pts))
                        
                g3 = input("\nWhat is the capital of New Zealand? ").upper()
                
                if g3 == "WELLINGTON":
                    print("\n Correct!\n")
                    player_pts +=1
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))
                else:
                    player_pts-=1
                    print("Wrong. Hint: Wellington") 
                    if player_pts>=3:
                        print("You win!")
                        print("Your points:"+ str(player_pts)) 
                    else:
                        print("you lose! You need 3 points.")
                        print("Your points:"+ str(player_pts))  
                                
                        
                        
            else:
                print("\n Incorrect Number! Try Again! ")          
    
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
        opponent_list = list()
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                opponent= line.strip().split(",")
                opponent_list.append(opponent)  
        
        opponent_choice = random.choice(opponent_list)
        self.opponent= opponent_choice[0]
        self.element = opponent_choice[1]
        self.hp = opponent_choice[2]
        self.strength =opponent_choice[3] 
        
    def __repr__(self):
        return f'Monster Name: {self.opponent}\n Element type: {self.element}\n Hitpoints: {self.hp}\n Strength: {self.strength}\n '
        
        
def main(path):
    """
    Simulates a confrontation between two element types.
    python final_project.py Opponent_List.csv  (for Windows) 
    python3 final_project.py Opponent_List.csv (for Mac)
    
    Args:
    path(Element): an instance of the element class that is being passed in

    """
    Element.choose_player(path)
    

x=Element()
main(x)
    