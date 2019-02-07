print("Welcome to The Vault of Glass!")

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
    }
}
