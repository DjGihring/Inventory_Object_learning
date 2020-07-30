#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
A simple Inventory System, containing a class for items and a class for the
bag.
"""



# Item Class
class Item:
    """Item, contains information on the object."""
    def __init__(self, name, symbol, disc, type, value, num):
        """
        Constructor for Item Class.

        Arguments:
            name(string): name of the Item
            symbol(string): Text Symbol for the Item
            disc(string): Item description
            type(string): type of item, food, gem, weapon, etc
            value(int): Monetary value of the Iten
            num(int): number of items
        """
        self.name = name
        self.symbol = symbol
        self.disc = disc
        self.type = type
        self.value = value
        self.num = num

class Inventory:
    """ Inventory Class for a character, uses nxn maxtrix as representation"""
    def __init__(self, name, size): #intializes the Inventory
        """
        Inventory object constructor

        Arguments:
            name(string): name of the Bag
            size(int): n in the nxn array which is just a list
        """
        self.name = name
        self.size = size
        self.space = 0
        self.nullItem = Item("null", str(
            0), "nothing here", "zzzzzzzz", -1, -1)
        self.inven = [self.nullItem for i in range(self.size*self.size)]

    def check(self): #Displays the inventory
        """Displays the inventory of the bag given in a nxn array."""
        print(self.name + ":")
        print('[', end = '')
        for i in range(self.size*self.size):
            print(self.inven[i].symbol, end = '')
            if((i+1)%self.size == 0):
                print(']')
                if (i+1) != (self.size*self.size):
                    print('[',end = '')
            else:
                print(' ,',end='')


    def insert(self, Item): #Inserts Item closest to the front
        """Given Item is inserted into the Bag as closest to 1x1."""
        for i in range(self.size*self.size):
            if(self.inven[i] == self.nullItem):
                self.inven[i] = Item
                print(Item.name + " was Inserted at " + str(i+1)
                        + 'x' + str(int(i/4)+1))
                return()

    def remove(self, ItemName):
        """Takes given Item and returns it as an Item object"""
        for i in range(len(self.inven)):
            if ItemName == self.inven[i].name:
                x = self.inven[i]
                self.inven[i] = self.nullItem
                return(x)

    def swap(self, p1, p2): #swaps two Items positions
        """Swaps the Items in the two Given positions."""
        item1 = self.inven[p1]
        item2 = self.inven[p2]
        self.inven[p1] = item2
        self.inven[p2] = item1

    def arrange(self, type): # Sort inven with lowest values first
        """
        Arranges the inventory according to the given instruction.

        Arguments:
            type(int): Corresponds the the value you want to compare, such as
            Alphabetical or value.

        Both Algorithms use a simple insertion sort to solve out what goes in
        the propper place.
        """
        if(type == 1): #Alphabetical
            for i in range(1 , len(self.inven)):
                key = self.inven[i]
                j = i - 1
                while j >= 0 and self.inven[j].name > key.name:
                    self.inven[j + 1] = self.inven[j]
                    j -= 1
                self.inven[j + 1] = key
    
        if(type == 2): #Value
            for i in range(1 , len(self.inven)):
                key = self.inven[i]
                j = i - 1
                while j >= 0 and self.inven[j].value > key.value:
                    self.inven[j + 1] = self.inven[j]
                    j -= 1
                self.inven[j + 1] = key

# This is just for testing, kind gross I know
def main():
    print("Testing Inventory stuff")
    Bottle = Item("bottle", "B", "A Water Bottle", "Misc", "5", "1")
    print("This is a " + Bottle.name)
    purse = Inventory("purse", 4)
    print("This is a " + purse.name)
    print("It's Size is " + str(purse.size))
    print("Here is it's contentes")
    purse.check();
    backPack = Inventory("backPack", 6)
    print("This is a " + backPack.name)
    print("It's Size is " + str(backPack.size))
    print("Here is it's contentes")
    backPack.check()
    backPack.insert(Bottle)
    backPack.check()
    Candy = Item("candy", "C", "A hard candy", "Misc", "7", "2")
    Apple = Item("apple", "a", "A red apple", "Food", "3", "1")
    backPack.insert(Candy)
    backPack.insert(Apple)
    backPack.check()
    print()
    backPack.arrange(1)
    backPack.check()
    x = backPack.remove("bottle")
    print("Just pulled out the " + x.name)
    backPack.check()
    input("press enter to exit")
    
if __name__ == "__main__":
    main()
