world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now."
                       " There are two doors on the north wall",
        'PATHS': {
            'North': "Parking_Lot"
        }
    },
    'Parking_Lot': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here",
        'PATHS': {
            'South': 'R19A'
        }
    }
}
playing = True
current_node = world_map['R19A']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
