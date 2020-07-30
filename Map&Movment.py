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

        the boardEmpty is the 'floor' of the room, it should only contain info
        about the actual floor.

        board holds things like items, characters, etc.
        """
        self.length = length
        self.width = width
        self.boardEmpty = [[Tile("floor", 0, ".") for x in range(self.width +
                            border)] for y in range(self.length+border)]
        self.board = [[Tile("null", 0, "#") for x in range(self.width +
                       border)]for y in range(self.length+border)]

        # Sets up walls for the room
        for j in range(self.width+border):
            for i in range(self.length+border):
                if((i == 0 or i == self.length+1) or
                        (j == 0 or j == self.width+1)):
                    self.boardEmpty[i][j] = Tile("wall", 1, "#")

    def ShowMap(self):
        """Prints out the map for the player to see"""
        for j in range(self.width+border):
            for i in range(self.length+border):
                print(self.boardEmpty[i][j].symbol, end=" ")
            print("")


class PlayerNavigator:
    def __init__(self, Character, map):
        self.Player = Character
        self.PosX = 1
        self.PosY = 1
        self.symbol = "@"
        map.boardEmpty[self.PosX][self.PosY] = self


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


if __name__ == "__main__":
    main()
