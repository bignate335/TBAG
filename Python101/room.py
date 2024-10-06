class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.locked_rooms = {}

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description

    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.name = room_name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def lock_room(self, direction):
        self.locked_rooms[direction] = True

    def unlock_room(self, direction):
        self.locked_rooms[direction] = False
        print(f"You unlocked the door to the {self.linked_rooms[direction].get_name()}")

    def get_details(self):
        print(self.name)
        print("----------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
    
    def move(self, direction, current_item):
        if direction in self.locked_rooms:
            if current_item is not None and current_item.get_name() == "Golden Key" and self.name is not "Kitchen":
                self.unlock_room(direction)
                return self.linked_rooms[direction]
            elif current_item is not None and current_item.get_name() == "Vampire's Treasure":
                self.unlock_room(direction)
                return self.linked_rooms[direction]
            else:
                print("The door is locked")
                return self
        elif direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self