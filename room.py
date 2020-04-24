class Room:

    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    '''Setting Name'''
    def set_name(self,room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    '''Setting Description'''
    def set_description(self,room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link

    '''Setting Enemy/Character'''
    def set_character(self,character):
        self.character = character

    def get_character(self):
        return self.character

    '''Setting Item'''
    def set_item(self,item_name):
        self.item = item_name

    def get_item(self):
        return self.item

    '''Gettting Detail Informations of each room'''
    def get_details(self):
        print("The" ,self.name)
        for i in range(10):
            print("-", end="")
        print("\n")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction] # return room name
            print("The " + room.get_name() + " is " + direction)
        print("\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self