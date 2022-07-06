import enum
class DogSize(enum.Enum):
    small = "small"
    medium = "medium"
    large = "large"

class Dog:
    def __init__(self, size):
        self.uuid = random() 
        self.size = size

class Hotel:
    def __init__(self):
        self.smallRoomsNum = 0

    def checkIn(self, dog):
        pass

    def checkOut(self, dog):
        pass 