from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["bread", "walking stick", "small rock"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


print(room['outside'].items)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def blocked():
    print("Nothing to see here!")

def player_update():
    print(f'Before you lays the {player.location.name}. {player.location.description} ')

# Make a new player object that is currently in the 'outside' room.
player = Player('Traveler', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# print(player.location)

while True:
    cmd = input()
    location = player.location

    if cmd == 'q':
        print('Safe travels!')
        break

    if cmd == 'n' and player.location != None:
        player.location = location.n_to
        print('You moved north:')
        player_update() 
    elif player.location == None:
        blocked()

    if cmd == 's'and player.location != None:
        player.location = player.location.s_to
        print('You moved south:')
        player_update()

    elif player.location == None:
        blocked()    

    if cmd == 'e'and player.location != None:
        player.location = player.location.e_to
        print('You moved east:')
        player_update()

    elif player.location == None:
        blocked()

    if cmd == 'w'and player.location != None:
        player.location = player.location.w_to
        print('You moved west:')
        player_update()

    elif player.location == None:
        blocked()


