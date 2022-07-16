class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each instance variable
    
    def add_trick(self, trick):
        self.tricks.append(trick)



# Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            