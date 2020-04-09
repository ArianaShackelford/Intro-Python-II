# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room = 'outside'):
        self.name = name
        self.current_room = current_room
        self.direction = direction

    def show_room(name,current_room):
        print(f' {name} is in {current_room.name}. {current_room.description} ')

    # def move(self, current_room, direction):
    #     if direction in (rooms[player.current_room].exists):
    #         player.current_room = rooms[player.current_room].exists.[direction]
    #         # basically outputs player.current_room = room['curentroom'].n_to = room['new-current-room']
    #         show_room() 
    #     else:
    #         print("There's nothing to see here")      




#give player name? -> "name", input name when creating character

#current_room attributes ---- need to figure out how to set 'current room' to display