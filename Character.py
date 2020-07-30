#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
A general Character Class, and has interatctions with the inventory.
"""

import Inventory as inv

class Character: 

    """Character class, contains information on the character."""
       
    def __init__(self, name, race, symbol, health, level, exp):
        """
        Constructor for Item Class.
        
        Arguments:
            name (string): name of the Character
            race (string): Race of the Character
            symbol (string): Text Symbol for the character 
            health (int): Health value
            level (int): level of the character
            exp (int): experince points
        """
        
        nullBag = inv.Inventory("null", 0)
        
        self.name = name
        self.race = race
        self.symbol = symbol
        
        self.bag = nullBag
        self.health = health
        self.level = level
        self.exp = exp


    def info(self):
    
        """Returns back information of the Character"""
        
        print("Their name is " + self.name + ".")
        print("They are a " + self.race + ".")
        print("Their Symbol is " + self.symbol + ".")
        print("Their health is at " + str(self.health) + ".")
        print("They are level " + str(self.level) + ".")
        print("They are this experinced " + str(self.exp) + ".")
        
    def equipInv(self, inventory):
         """ Equips a bag to the inventory slot if empty"""
         if(self.bag.name == "null"):
             self.bag = inventory
             print("Equipped the " + inventory.name + ".")
         else:
             print("Allready have a " + self.bag.name + " equiped.")  



def main(): # more for testing than anything
    Player = Character("James", "Human", "@", 10, 1, 0)
    Player.info()
    
    satchel = inv.Inventory("satchel", 5)
    Player.equipInv(satchel)
    purse = inv.Inventory("purse", 4)
    Player.equipInv(purse)
    

if __name__ == "__main__":
    main()
    