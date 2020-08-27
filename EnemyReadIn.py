#!usr/bin/python3
# -*- coding: utf-8 -*-

import Character as Ch


class Enemy:

    def ScanFile(self, nameString):
        """
        Reads in a txt file to create an enemy character
        """
        splitChar = ":"
        docName = nameString + ".txt"
        enemyDoc = open(docName, "r")
        enemyInfo = enemyDoc.readlines()
        # There has to be a cleaner way of doing this, but I cant think of it
        # at the moment, my guess would be to have an info list that has 
        # the correct number of items
        self.name = enemyInfo[0].partition(splitChar)[2]
        self.race = enemyInfo[1].partition(splitChar)[2]
        self.symbol = enemyInfo[2].partition(splitChar)[2]
        self.health = enemyInfo[3].partition(splitChar)[2]
        self.level = enemyInfo[4].partition(splitChar)[2]
        self.exp = enemyInfo[5].partition(splitChar)[2]
        self.attack = enemyInfo[6].partition(splitChar)[2]
        self.armour = enemyInfo[7].partition(splitChar)[2]
        print(self.name)
        
def main():  # more for testing than anything
    
    Mork = Enemy()
    Orc = "Orc"
    Mork.ScanFile(Orc)


if __name__ == "__main__":
    main()