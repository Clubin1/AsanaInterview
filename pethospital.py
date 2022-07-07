from random import randint


class Dog:
    def __init__(self, size):
        self.size = size
        self.uid = randint(0, 10000)

class Hotel:
    def __init__(self, smallRoomCount, mediumRoomCount, largeRoomCount):
        self.__smallRoomCount = smallRoomCount
        self.__mediumRoomCount = mediumRoomCount
        self.__largeRoomCount = largeRoomCount
        self.__smallRooms, self.__mediumRooms, self.__largeRooms = dict(), dict(), dict() 
        # {"room number" : dog Object}

    def buildHotel(self):
        # populates room maps with string IDS and empty Dog Object
        pass
    
    def checkIn(self, dog):
        if dog.size == enum.small and len

    def checkOut(self):
        pass


