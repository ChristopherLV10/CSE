print("Welcome to The Vault of Glass!")

directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

world_map = {
    'VOG Entrance': {
        'NAME': "Entrance",
        'DESCRIPTION': "In front of the entrance to the vault.",
        'PATHS': {
            'WEST': "Left Button"

        }
    },
    'Left Button': {
        'NAME': "Left Button",
        'DESCRIPTION': "Here is one of the 2 buttons you need to press to open the door",
        'PATHS': {
            'EAST': 'VOG Entrance'
        }
    }
}
