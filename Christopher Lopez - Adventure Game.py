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
            'SOUTH': 'VOG Entrance'
        }
    }
}
