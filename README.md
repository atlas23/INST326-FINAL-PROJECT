# INST326-FINAL-PROJECT
## Paul Rozario, Michael Okeno

## Purpose of each file:

final_project.py: contains the final project script with the Element and Opponent classes, and runs the program.


Opponent_list.csv: contains the different monsters that the user is up against alongside their stats. Used in choose_player and Opponent class to determine who the player is facing.


## Instructions for Running the code at the command line

1) In terminal, type the command "python3 final_project.py" on mac or 
"python final_project.py" on windows

2) The prompt will ask you to enter your input and the game will start.

3) Enter "Y or N" if you want to roll the dice. If you do roll the dice 
it should print the amount of luck out 

4) Choose a room number that you want to start with and enter a value

5) Some graphs should display comparing the stats of your hp and strength
 to the opponents. Close the graphs to continue with the game

6) You will be asked a couple of trivia questions to move on to the next room.
The prompt will ask you to select a number

7) After the number is chosen, choose one of the  numbers that represents the
different types of categories

8) Once the category is selected, you will answer a series of questions to 
decide on whether you move on to the next room.

## How to interpret the results
There are a series of inputs which monitor your progress throughout the game. There are also bar graph visuals which compare the player's stats versus the opponent stats. Health and Strength for the player are determined randomly while the monster's stats are fixed, in order to provide a unique experience for each confrontation.You will know when you win once you obtain 3 points from the survey_method() function, otherwise you will lose.

## Attribution
Paul is responsible for the init and choose_player functions in the Element class, as well as the entire Opponent class. I also assisted in portions of the survey_method class. Michael is responsible for the survey method class and portions of the choose_player function and Opponent class.

## Annotated Bibliography
Thecodingpie. (n.d.). Make your own text based adventure game in python3: Thecodingpie. thecodingpie RSS. Retrieved December 15, 2021, from https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3 

Our inspiration for our program derives from the following source. We derived our idea from the picture that is used to depict the adventure game, which is a series of rooms with different monsters.
