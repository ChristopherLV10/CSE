Red = '\033[31m'  # Red Text
Green = '\033[32m'  # Green Text
Yellow = '\033[33m'  # Yellow Text
Blue = '\033[34m'  # Blue Text
Purple = '\033[35m'  # Purple Text
Cyan = '\033[36m'  # Cyan Text


class Room(object):
    def __init__(self, name, description, object, character,
                 north=None, south=None, east=None, west=None, down=None):
        self.name = name
        self.object = object
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.description = description
        self.character = character

    def __str__(self):
        return self.name


class Consumable(object):
    def __init__(self, name):
        self.name = name


class Armor(object):
    def __init__(self, name):
        self.name = name


class Backpack(object):
    def __init__(self, name):
        self.name = name


class Bag(Backpack):
    def __init__(self, name):
        super(Bag, self).__init__(name)
        self.name = name


class Key(object):
    def __init__(self, name):
        self.name = name


class EntranceKey(Key):
    def __init__(self, name):
        super(EntranceKey, self).__init__(name)
        self.name = name


class VaultKey(Key):
    def __init__(self, name):
        super(VaultKey, self).__init__(name)
        self.name = name


class Map(object):
    def __init__(self, name):
        self.name = name


class VOG(Map):
    def __init__(self, name):
        super(VOG, self).__init__(name)


class Weapon(object):
    def __init__(self, name, damage: int):
        self.name = name
        self.damage = damage


class HealthPotion(Consumable):
    def __init__(self, name):
        super(HealthPotion, self).__init__(name)
        self.name = name
        self.health = 0

    def heal(self):
        print("I just gained 50 health")
        self.health += 50


class ShieldPotion(Consumable):
    def __init__(self, name):
        super(ShieldPotion, self).__init__(name)
        self.name = name
        self.shield = 0

    def use(self):
        self.shield += 50
        print("Now I have", self.shield, "shield")


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


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__(name, 150)
        self.durability = 5

    def slash(self):
        self.durability -= 1
        print("My sword's about to break, I can only slash", self.durability, "more times")


class Burst(Weapon):
    def __init__(self, name):
        super(Burst, self).__init__(name, 30)
        self.bullets_left = 30

    def press_trigger(self):
        self.bullets_left -= 3
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 30
        print("Now I have 30 bullets")


class DMR(Weapon):
    def __init__(self, name):
        super(DMR, self).__init__(name, 70)
        self.bullets_left = 12

    def press_trigger(self):
        self.bullets_left -= 1
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 12
        print("Now I have 12 bullets")


class Grenade(Weapon):
    def __init__(self, name):
        super(Grenade, self).__init__(name, 200)
        self.name = name


class character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage is done because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


burst = Burst("Blast Furnace")
dmr = DMR("Oxygen SR3")
sword = Sword("Raze Lighter")
Hobgoblin1 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin2 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin3 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin4 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin5 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin7 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin8 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin9 = character("Hobgoblin", 100, Burst, armor=50)
Hobgoblin10 = character("Hobgoblin", 100, Burst, armor=50)
Atheon = character("Atheon", 500, dmr, armor=100)


class Player(object):
    def __init__(self, starting_location, name: str, health: int, weapon, armor):
        self.current_location = starting_location
        self.bag = [burst, dmr, sword]
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage is done because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

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


Entrance = Room(Yellow + "Vault Entrance", "In front of the entrance to the vault.", None, None)
Left_Platform = Room(Yellow + "Left Platform",
                     "Here is one of the 2 platforms you need to go to so that the door could open",
                     EntranceKey, None)
Right_Platform = Room(Yellow + "Right Platform",
                      "Here is one of the 2 platforms you need to go to so that the door could open",
                      None, None)
Path_Into_VOG = Room(Yellow + "Path into VOG", "This path leads you to the inside of the vault of glass", None, None)
Templar_Room_Entrance = Room(Yellow + "Templar Room Entrance", "In front of you is the templar room", None, Hobgoblin1)
South_of_Templar_Room = Room(Yellow + "South of Templar Room", "South side of the templar room", None, None)
North_of_Templar_Room = Room(Yellow + "North of Templar Room", "North side of the templar room", None, None)
East_of_Templar_Room = Room(Yellow + "East of Templar Room", "East side of the templar room", VaultKey, Hobgoblin3)
West_of_Templar_Room = Room(Yellow + "West of Templar Room", "West side of the templar room", None, Hobgoblin2)
Gorgon_Maze = Room(Yellow + "Gorgon Maze", "You are at a maze, choose a path", None, None)
Path_1 = Room(Yellow + "Path 1", "The incorrect path.", None, Hobgoblin4)
Path_2 = Room(Yellow + "Path 2", "The incorrect path.", None, Hobgoblin5)
Path_3 = Room(Yellow + "Path 3", "The correct path.", None, None)
Path_to_Glass_Throne = Room(Yellow + "Path to Glass Throne", "Path that leads you to the glass throne", None, None)
Glass_Throne_Door = Room(Yellow + "Glass Throne Door", "The end of the Vault?", None, None)
Glass_Throne = Room(Yellow + "Glass Throne", "Atheon's room.", None, Atheon)
Entrance.east = Right_Platform
Entrance.west = Left_Platform
Entrance.north = Path_Into_VOG
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
Glass_Throne.south = Glass_Throne_Door
Glass_Throne_Door.north = Glass_Throne


print(Blue + "Welcome to The Vault of Glass!")

playing = True
directions = ['north', 'south', 'east', 'west', 'down']
player = Player(Entrance, "Titan", 100, burst, 200)

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(Blue + ">_")
    print()
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    elif command == "bag":
        print("You have the following items:")
        for item in player.bag:
            print(item.name)
    elif command == "look":
        print(Yellow + "You can go:", Yellow + Blue + "North:", player.current_location.north,
              Blue + "South:", player.current_location.south, Blue + "East:",
              player.current_location.east, Blue + "West:", player.current_location.west,
              Blue + "Down:", player.current_location.down)
        print("Item:", player.current_location.object)
        if player.current_location.character is not None:
            print("Enemy:", player.current_location.character.name)
    elif "shoot" in command:
        burst.press_trigger()
    elif "reload" in command:
        burst.reload()
    elif command == "take item":
        player.bag.append(player.current_location.object)
    else:
        print("Command Not Found")
    print()
