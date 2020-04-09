# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location


#needs super() to pass down rooms
#give player name?

#current_room attributes ---- need to figure out how to set 'current room' to display