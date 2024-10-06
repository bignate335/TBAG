from room import Room
from character import Character
from character import Enemy
from character import Ally
from item import Item

kitchen = Room("Kitchen")
dining_hall = Room("Dining Hall")
ballroom = Room("Ballroom")
treasure_room = Room("Treasure Room")
exit = Room("Exit")

kitchen.set_description("A dark and dirty room buzzing with flies")
dining_hall.set_description("A large room with a long table, fireplace and chairs")
ballroom.set_description("A vast room with a chandelier on the ceiling")
treasure_room.set_description("A room glittering with gold and jewels")

kitchen_knife = Item("Kitchen Knife")
kitchen_knife.set_description("A rusty kitchen knife. It's close to breaking")
kitchen.set_item(kitchen_knife)

wooden_stake = Item("Wooden Stake")
wooden_stake.set_description("A hastily carved stake with a single bloody fingerprint")
dining_hall.set_item(wooden_stake)

golden_key = Item("Golden Key")
golden_key.set_description("A shiny golden key")
ballroom.set_item(golden_key)

vampire_treasure = Item("Vampire's Treasure")
vampire_treasure.set_description("More gold than you could ever count, and the key to the exit")
treasure_room.set_item(vampire_treasure)

prisoner = Ally("Prisoner", "A chained prisoner covered in cuts and bruises")
prisoner.set_conversation("*splutters* run away before it's too late")
crazed_guest = Enemy("Crazed Guest", "A crazed dinner guest, wielding a carving knife")
crazed_guest.set_weakness(kitchen_knife)
vampire = Enemy("Vampire", "A pale vampire with a long black cloak")
vampire.set_weakness(wooden_stake)

kitchen.set_character(prisoner)
dining_hall.set_character(crazed_guest)
ballroom.set_character(vampire)

kitchen.link_room(exit, "north")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(treasure_room, "west")
treasure_room.link_room(ballroom, "east")

kitchen.lock_room("north")
ballroom.lock_room("west")

current_item = None

current_room = kitchen

game_running = True
secret_ending = False

while game_running and current_room is not exit:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    command = command.lower()
    if command in ("north", "east", "south", "west"):
        current_room = current_room.move(command, current_item)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("You mumble to yourself")
    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                if inhabitant.fight(current_item):
                    print(f"The {inhabitant.get_name()} was no match for your {current_item.get_name()}")
                    current_room.set_character(None)
                else:
                    if current_item is not None:
                        print(f"Your {current_item.get_name()} did nothing against the {inhabitant.get_name()}")
                    else:
                        print(f"You have no weapon! You have no chance against the {inhabitant.get_name()}")
                    print("YOU DIED! Better luck next time!")
                    game_running = False
            else:
                print(f"{inhabitant.get_name()} does not want to fight you!")
        else:
            print("There is nobody to fight")
    elif command == "search":
        if current_room.item is not None:
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                print(f"The {inhabitant.get_name()} lunges at you, knocking you over before you can look around")
            else:
                current_item = current_room.get_item()
                print(f"You found a {current_item.get_name()}!")
                current_room.item = None
        else:
            print("You look around and find nothing")
    elif command == "hug":
        if isinstance(inhabitant, Ally):
            inhabitant.hug()
        elif inhabitant is not None:
            print(f"{inhabitant.get_name()} does not want to hug you")
        else:
            print("There is nobody to hug")
    elif command == "gift":
            if isinstance(inhabitant, Ally):
                secret_ending = inhabitant.gift(current_item)
                current_item = None
            elif inhabitant is not None:
                print(f"You don't want to give {inhabitant.get_name()} a gift")
            else:
                print("There is nobody to give a gift to")
    else:
        print("Do you want to move, fight, talk, or search?")
    if secret_ending:
        game_running = False

if secret_ending == False:
    print("You win, but at what cost?")
    print("You take one look back as you walk down the gravel, and you watch the prisoner take one final breath")
input("Press enter to end game ")