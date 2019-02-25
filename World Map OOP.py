class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down


# Option 1 - Define as we go
Entrance = Room("Mr. Wiebe's Room")
Left_Platform = Room("Left Platform", None, Entrance)
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

directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']


world_map = {
    'VOG Entrance': {
        'NAME': "Entrance",
        'DESCRIPTION': "In front of the entrance to the vault.",
        'PATHS': {
            'WEST': "Left Platform",
            'EAST': "Right Platform",
            'NORTH': "Path Into VOG"

        }
    },
    'Left Platform': {
        'NAME': "Left_Platform",
        'DESCRIPTION': "Here is one of the 2 platforms you need to go to so that the door could open",
        'PATHS': {
            'EAST': 'VOG Entrance'
        }
    },
    'Right Platform': {
        'NAME': "Right_Platform",
        'DESCRIPTION': "Here is one of the 2 platforms you need to go to so that the door could open",
        'PATHS': {
            'WEST': 'VOG Entrance'
        }
    },
    'Path Into VOG': {
        'NAME': "Path_Into_VOG",
        'DESCRIPTION': "This path leads you to the inside of the vault of glass",
        'PATHS': {
            'SOUTH': 'VOG Entrance',
            'NORTH': 'Templar Room Entrance'
        }
    },
    'Templar Room Entrance': {
        'NAME': "Templar_Room_Entrance",
        'DESCRIPTION': "In front of you is the templar room",
        'PATHS': {
            'NORTH': 'South of Templar Room',
            'SOUTH': 'Path Into VOG'
        }
    },
    'South of Templar Room': {
        'NAME': "South_of_Templar_Room",
        'DESCRIPTION': "South side of the templar room",
        'PATHS': {
            'WEST': 'West of Templar Room',
            'NORTH': 'North of Templar Room',
            'EAST': 'East of Templar Room',
            'SOUTH': 'Templar Room Entrance'
        }
    },
    'North of Templar Room': {
        'NAME': "North_of_Templar_Room",
        'DESCRIPTION': "North side of the templar room",
        'PATHS': {
            'SOUTH': 'South of Templar Room',
            'NORTH': 'Gorgon Maze'
        }
    },
    'East of Templar Room': {
        'NAME': "East_of_Templar_Room",
        'DESCRIPTION': "East side of the templar room",
        'PATHS': {
            'WEST': 'South of Templar Room'
        }
    },
    'West of Templar Room': {
        'NAME': "West_of_Templar_Room",
        'DESCRIPTION': "West side of the templar room",
        'PATHS': {
            'EAST': 'South of Templar Room'
        }
    },
    'Gorgon Maze': {
        'NAME': "Gorgon_Maze",
        'DESCRIPTION': "You are at a maze, choose a path",
        'PATHS': {
            'SOUTH': 'North of Templar Room',
            'WEST': 'Path 1',
            'NORTH': 'Path 2',
            'EAST': 'Path 3'
        }
    },
    'Path 1': {
        'NAME': "Path_1",
        'DESCRIPTION': "The incorrect path. You should go back",
        'PATHS': {
            'EAST': 'Gorgon Maze'
        }
    },
    'Path 2': {
        'NAME': "Path_2",
        'DESCRIPTION': "The incorrect path. You should go back",
        'PATHS': {
            'SOUTH': 'Gorgon Maze'
        }
    },
    'Path 3': {
        'NAME': "Path_3",
        'DESCRIPTION': "The path that leads to the end of the maze.",
        'PATHS': {
            'WEST': 'Gorgon Maze',
            'NORTH': 'Path to Glass Throne'

        }
    },
    'Path to Glass Throne': {
        'NAME': "Path_to_Glass_Throne",
        'DESCRIPTION': "Path that leads you to the glass throne",
        'PATHS': {
            'SOUTH': 'Path 3',
            'DOWN': 'Glass Throne Door'
        }
    },
    'Glass Throne Door': {
        'NAME': "Glass_Throne_Door",
        'DESCRIPTION': "The end of the Vault",
    }
}
current_node = world_map['VOG Entrance']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
