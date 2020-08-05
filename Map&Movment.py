#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
Handles creation and the state of the map, as well as the movment of the
player.
"""

import Character as Ch

border = 2  # This allows for the walls to be placed around the room's floor


class Tile:
    """Standard movment tile, basiclly acts just as a floor"""
    def __init__(self, type, state, symbol):
        """
        Sets up the infor for a tile

        Arugments:
            type (string): the type of floor it is
            state (int): 0 is passable, 1 is impassable
        """
        self.type = type
        self.state = state
        self.symbol = symbol


class Map:
    """ The Map class, creates itself and manages such"""
    def __init__(self, length, width):
        """
        Initializes the map witha  length and a width

        Arguments:
            length (int): defines the x direction of the room
            width (int): defines the y direction of the room

        Creates a empty floor space with a given width and length, and then
        fills in the outside area with a impassable wall

        the boardFloor is the 'floor' of the room, it should only contain info
        about the actual floor as well as the walls.
        
        boardItem holds items, obsticals, etc, anthing that is not alive, and 
        not a floor

        boardChar holds characters, etc.
        """
        self.length = length
        self.width = width
        self.boardFloor = [[Tile("floor", 0, ".") for x in range(self.width +
                            border)] for y in range(self.length+border)]
        self.boardItem = [[Tile("null", 0, "#") for x in range(self.width +
                          border)]for y in range(self.length+border)]
        self.boardChar = [[Tile("null", 0, "#") for x in range(self.width +
                          border)]for y in range(self.length+border)]

        # Sets up walls for the room
        for j in range(self.width+border):
            for i in range(self.length+border):
                if((i == 0 or i == self.length+1) or
                        (j == 0 or j == self.width+1)):
                    self.boardFloor[i][j] = Tile("wall", 1, "#")

    def ShowMap(self):
        """
        Prints out the map for the player to see
        
        This prints out the symbol acording to layer priority in this order,
        Walls, Chars, Items/Interactables, floor       
        """
        for j in reversed(range(self.width+border)):
        
            for i in range(self.length+border):
                if((self.boardChar[i][j].type == "null" and
                        self.boardItem[i][j].type == "null")
                        or self.boardChar[i][j].type == "wall"):
                    print(self.boardFloor[i][j].symbol, end=" ")
                    
                elif(self.boardChar[i][j].type == "null" and 
                        self.boardItem[i][j].type != "null"):
                    print(self.boardItem[i][j].symbol, end=" ")
                
                else:
                    print(self.boardChar[i][j].symbol, end=" ")
                    
            print("")


class PlayerNavigator:
    def __init__(self, Character, map):
        self.type = "Character"
        self.PosX = 1
        self.PosY = 1
        self.symbol = "@"

        map.boardChar[self.PosX][self.PosY] = self
        self.map = map

    def playerMovment(self, direction):
        if(direction == 8):  # Up
            self.map.boardChar[self.PosX][self.PosY] = Tile("null", 0, "#")
            self.PosY += 1
            self.map.boardChar[self.PosX][self.PosY] = self

        if(direction == 4):  # Left
            self.map.boardChar[self.PosX][self.PosY] = Tile("null", 0, "#")
            self.PosX -= 1
            self.map.boardChar[self.PosX][self.PosY] = self

        if(direction == 6):  # Right
            self.map.boardChar[self.PosX][self.PosY] = Tile("null", 0, "#")
            self.PosX += 1
            self.map.boardChar[self.PosX][self.PosY] = self

        if(direction == 2):  # Down
            self.map.boardChar[self.PosX][self.PosY] = Tile("null", 0, "#")
            self.PosY -= 1
            self.map.boardChar[self.PosX][self.PosY] = self
        self.map.ShowMap()


def main():  # more for testing than anything
    print("Testing out map&movemnt")

    print("Testing out Map Creation and Presentation")
    testMap = Map(4, 4)
    testMap.ShowMap()
    testMap2 = Map(6, 8)
    testMap2.ShowMap()
    testMap3 = Map(10, 4)
    testMap3.ShowMap()
    print("")
    print("Testing out adding the navigator to the map")
    James = Ch.Character("James", "Human", "@", 10, 1, 0)
    nav = PlayerNavigator(James, testMap3)
    testMap3.ShowMap()
    nav.playerMovment(8)
    nav.playerMovment(6)


if __name__ == "__main__":
    main()
