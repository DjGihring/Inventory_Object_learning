#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
Handles creation and the state of the map, as well as the movment of the player.
"""

border = 2

class Tile:
    """Standard movment tile, basiclly acts just as a floor"""
    def __init__(self,type,state,symbol):
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
        """ Initializes the map witha  length and a width"""
        self.length = length
        self.width = width
        self.board = [[Tile("floor",0,".") for x in range(self.width+border)]
                            for y in range (self.length+border)]
        # Sets up walls for the room
        for j in range(self.width+2):
            for i in range(self.length+2):
                if((i == 0 or i == self.length+1) or
                    (j == 0 or j == self.width+1)):
                    self.board[i][j] = Tile("wall",1,"#")
        
    def ShowMap(self):
        """Prints out the map for the player to see"""
        for j in range(self.width+border):
            for i in range(self.length+border):
                print(self.board[i][j].symbol, end = " ")
            print("")
        
        
        
        

        
    
    
def main(): # more for testing than anything
    print("Testing out map&movemnt")
    
    print("Testing out Map Creation and Presentation")
    testMap = Map(4,4)
    testMap.ShowMap()
    testMap2 = Map(6,8)
    testMap2.ShowMap()
    testMap3 = Map(10,4)
    testMap3.ShowMap()
    

if __name__ == "__main__":
    main()