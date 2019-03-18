class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.description = description
        self.characters = []


shield = 0


class Consumable(object):
    def __init__(self, name):
        self.name = name


class HealthPotion(Consumable):
    def __init__(self, name):
        super(HealthPotion, self).__init__(name)
        self.name = name
        self.health = 0

    def heal(self):
        print("I just gained 50 health")
        self.health += 50


class Armor(object):
    def __init__(self, name):
        self.name = name


class Helmet(Armor):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.name = name
        self.shield = 12.5


class Chest(Armor):
    def __init__(self, name):
        super(Chest, self).__init__(name)
        self.name = name
        self.shield = 12.5


class Greaves(Armor):
    def __init__(self, name):
        super(Greaves, self).__init__(name)
        self.name = name
        self.shield = 12.5


class Gauntlets(Armor):
    def __init__(self, name):
        super(Gauntlets, self).__init__(name)
        self.name = name
        self.shield = 12.5


class ShieldPotion(Consumable):
    def __init__(self, name):
        super(ShieldPotion, self).__init__(name)
        self.name = name
        self.shield = 0

    def use(self):
        self.shield += 50
        print("Now I have", self.shield, "shield")


class Weapon(object):
    def __init__(self, name):
        self.name = name


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.durability = 5

    def slash(self):
        self.durability = 5
        print("My sword's about to break, I can only slash", self.durability, "more times")


class Burst(Weapon):
    def __init__(self, name):
        super(Burst, self).__init__(name)
        self.bullets_left = 30

    def press_trigger(self):
        self.bullets_left -= 3
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 30
        print("Now I have 30 bullets")


class DMR(Weapon):
    def __init__(self, name):
        super(DMR, self).__init__(name)
        self.bullets_left = 12

    def press_trigger(self):
        self.bullets_left -= 1
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 12
        print("Now I have 12 bullets")


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room exists in that direction

        :param direction:
        :return: The Room object if it exists, or None if it does not
        """
        return getattr(self.current_location, direction)


Entrance = Room("Vault Entrance", None)
Left_Platform = Room("Left Platform", None)
Right_Platform = Room("Right Platform", None)
Path_Into_VOG = Room("Path into VOG", None)
Templar_Room_Entrance = Room("Templar Room Entrance", None)
South_of_Templar_Room = Room("South of Templar Room", None)
North_of_Templar_Room = Room("North of Templar Room", None)
East_of_Templar_Room = Room("East of Templar Room", None)
West_of_Templar_Room = Room("West of Templar Room", None)
Gorgon_Maze = Room("Gorgon Maze", None)
Path_1 = Room("Path 1", None)
Path_2 = Room("Path 2", None)
Path_3 = Room("Path 3", None)
Path_to_Glass_Throne = Room("Path to Glass Throne", None)
Glass_Throne_Door = Room("Glass Throne Door", None)
Entrance.east = Right_Platform
Entrance.west = Left_Platform
Right_Platform.west = Entrance
Left_Platform.east = Entrance
Path_Into_VOG.south = Entrance
Path_Into_VOG.north = Templar_Room_Entrance
Templar_Room_Entrance.south = Path_Into_VOG
Templar_Room_Entrance.north = South_of_Templar_Room
South_of_Templar_Room.north = North_of_Templar_Room
South_of_Templar_Room.south = Templar_Room_Entrance
South_of_Templar_Room.east = East_of_Templar_Room
South_of_Templar_Room.west = West_of_Templar_Room
North_of_Templar_Room.south = South_of_Templar_Room
North_of_Templar_Room.north = Gorgon_Maze
West_of_Templar_Room.east = South_of_Templar_Room
East_of_Templar_Room.west = South_of_Templar_Room
Gorgon_Maze.south = North_of_Templar_Room
Gorgon_Maze.west = Path_1
Gorgon_Maze.north = Path_2
Gorgon_Maze.east = Path_3
Path_3.west = Gorgon_Maze
Path_3.north = Path_to_Glass_Throne
Path_2.south = Gorgon_Maze
Path_1.east = Gorgon_Maze
Path_to_Glass_Throne.south = Path_3
Path_to_Glass_Throne.down = Glass_Throne_Door
print("Welcome to The Vault of Glass!")
playing = True

directions = ['north', 'south', 'east', 'west', 'down']
player = Player(Entrance)


while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
