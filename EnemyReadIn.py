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
        print(enemyInfo)
        
def main():  # more for testing than anything
    
    Mork = Enemy()
    Orc = "Orc"
    Mork.ScanFile(Orc)


if __name__ == "__main__":
    main()