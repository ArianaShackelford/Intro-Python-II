# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []
        # self.directions = [
        self.n_to = None,
        self.s_to = None,
        self.e_to = None,
        self.w_to = None

    # __str__ to make display nicely --> less parsable
    # directions need to be assigned to rooms somehow