#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
A general Character Class, and has interatctions with the inventory.
"""

import Inventory as inv

class Character: 

    """Character class, contains information on the character."""
       
    def __init__(self, name, race, symbol, inventory, health, level, exp):
        """
        Constructor for Item Class.
        
        Arguments:
            name (string): name of the Character
            race (string): Race of the Character
            symbol (string): Text Symbol for the character
            inventory (Inventory): storage 
            health (int): Health value
            level (int): level of the character
            exp (int): experince points
        """
        
        
        
        self.name = name
        self.race = race
        self.symbol = symbol
        self.inventory = inv.Inventory("null", 0)
        self.health = health
        self.level = level
        self.exp = exp


    def info(self):
    
        """Returns back information of the Character"""
        
        print("Their name is " + self.name + ".")
        print("They are a " + self.race + ".")
        print("Their Symbol is " + self.symbol + ".")
        print("Their health is at " + self.health + ".")
        print("They are level " + self.level+ ".")
        print("They are this experinced " + self.experince + ".")
        
    def equipInv(self, inv.Inventory):
        """ Equips a bag to the inventory slot if empty"""
        if(self.inventory.name == "null"):
            self.inventory = inv.Inventory
            print("Equipped the " + inv.Inventory.name + ".")
        else:
            print("Allready have a " + self.inventory.name + " equiped.")  



def main(): # more for testing than anything

if __name__ == "__main__":
    main()