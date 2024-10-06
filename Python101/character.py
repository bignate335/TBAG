class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def get_name(self):
        return self.name

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you!")
        
    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight you")
        return None
    

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == None:
            print(f"You have nothing to fight with! The {self.name} kills you instantly")
            return False
        elif combat_item == self.weakness:
            return True
        else:
            return False
        

class Ally(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print(f"You hug the {(self.name).lower()}")

    def gift(self, gift_item):
        if gift_item == None:
            print(f"You have nothing to give the {(self.name).lower()}")
            return False
        if self.name == "Prisoner" and gift_item.get_name() == "Vampire's Treasure":
            print("SECRET ENDING:")
            print("You hand the treasure to the prisoner")
            print("The prisoner gets up and does a jolly dance")
            print("\"Thankyou!\" says the prisoner, and you both live happily ever after in the vampire's castle")
            print("YOU WIN!")
            return True
        else:
            print(f"{self.name} says thankyou for the {(gift_item.get_name()).lower()}!")
            return False
