class Element:
    def __init__(self, element, hp, strength):
        self.element=element
        self.hp=hp
        self.strength=strength
        
    def choose_player(self,ans):
        print("\n Choose your player")
        ans= input("").upper
        if ans=="FIRE":
            print("\n You have chosen fire. You have an advantage against grass")
            self.element= "FIRE"
            self.hp= 100
            self.strength=10
        elif ans== "ICE":
            print("\n You have chosen ice. You have an advantage against fire")
            self.element="ICE"
            self.hp=100
            self.strength=10
        elif ans== "GRASS":
            print("\n You have chosen grass. You have an advantages against water.")
            self.element="GRASS"
            self.hp=100
            self.hp=10
        else:
            raise KeyError("Invalid Player." 
                           +" Please select from the following:"
                           +" FIRE, WATER, GRASS")

    