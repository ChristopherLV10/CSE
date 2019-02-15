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
        'NAME': "Left Platform",
        'DESCRIPTION': "Here is one of the 2 platforms you need to go to so that the door could open",
        'PATHS': {
            'EAST': 'VOG Entrance'
        }
    },
    'Right Platform': {
        'NAME': "Right Platform",
        'DESCRIPTION': "Here is one of the 2 platforms you need to go to so that the door could open",
        'PATHS': {
            'WEST': 'VOG Entrance'
        }
    },
    'Path Into VOG': {
        'NAME': "Path Into VOG",
        'DESCRIPTION': "This path leads you to the inside of the vault of glass",
        'PATHS': {
            'SOUTH': 'VOG Entrance',
            'NORTH': 'Templar Room Entrance'
        }
    },
    'Templar Room Entrance': {
        'NAME': "Templar Room Entrance",
        'DESCRIPTION': "In front of you is the templar room",
        'PATHS': {
            'NORTH': 'South of Templar Room',
            'SOUTH': 'Path Into VOG'
        }
    },
    'South of Templar Room': {
        'NAME': "South of Templar Room",
        'DESCRIPTION': "South side of the templar room",
        'PATHS': {
            'WEST': 'West of Templar Room',
            'NORTH': 'North of Templar Room',
            'EAST': 'East of Templar Room',
            'SOUTH': 'Templar Room Entrance'
        }
    },
    'North of Templar Room': {
        'NAME': "North of Templar Room",
        'DESCRIPTION': "North side of the templar room",
        'PATHS': {
            'SOUTH': 'South of Templar Room',
            'North': 'Gorgon Maze'
        }
    },
    'East of Templar Room': {
        'NAME': "East of Templar Room",
        'DESCRIPTION': "East side of the templar room",
        'PATHS': {
            'WEST': 'South of Templar Room'
        }
    },
    'West of Templar Room': {
        'NAME': "West of Templar Room",
        'DESCRIPTION': "West side of the templar room",
        'PATHS': {
            'EAST': 'South of Templar Room'
        }
    },
    'Gorgon Maze': {
        'NAME': "Gorgon Maze",
        'DESCRIPTION': "You are at a maze, choose a path",
        'PATHS': {
            'SOUTH': 'North of Templar Room',
            'WEST': 'Path 1',
            'NORTH': 'Path 2',
            'EAST': 'Path 3'
        }
    },
    'Path 1': {
        'NAME': "Path 1",
        'DESCRIPTION': "1 of the 3 paths you can follow to try to get to the end of the maze.",
        'PATHS': {
            'EAST': 'Gorgon Maze'
        }
    },
    'Path 2': {
        'NAME': "Path 2",
        'DESCRIPTION': "1 of the 3 paths you can follow to try to get to the  end of the maze.",
        'PATHS': {
            'SOUTH': 'Gorgon Maze'
        }
    },
    'Path 3': {
        'NAME': "Path 3",
        'DESCRIPTION': "1 of the 3 paths you can follow to try to get to the  end of the maze.",
        'PATHS': {
            'WEST': 'Gorgon Maze',
            'NORTH': 'Path to Glass Throne'

        }
    },
    'Path to Glass Throne': {
        'NAME': "Path to Glass Throne",
        'DESCRIPTION': "Path that leads you to the glass throne",
        'PATHS': {
            'SOUTH': 'Path 3',
            'DOWN': 'Glass Throne Door'
        }
    },
    'Glass Throne Door': {
        'NAME': "Glass Throne Door",
        'DESCRIPTION': "..",
        'PATHS': {
            'NORTH': ''
        }
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

