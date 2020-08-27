#!usr/bin/python3
# -*- coding: utf-8 -*-

import Character as ch
import MapMovment as mm
import os

def choices(inp, player):
    """
    Player input is taken in by this function and then handled correctly
    
    """
    print(inp)
    
    if inp == "2" or inp == "4" or inp == "6" or inp == "8":
        #os.system('clear')
        player.playerMovment(int(inp))
    
    elif inp == "s":
        choice = input("Search in which direction?")
        result = player.search(int(choice))
        print(result)

    else:
        print("Nothing recognoized")
    
    

def main():  # more for testing than anything
    testMap3 = mm.Map(10, 4)
    James = ch.Character("James", "Human", "@", 10, 1, 0)
    player = mm.PlayerNavigator(James, testMap3)
    testMap3.ShowMap()
    
    choice = ''
    while choice is not 'q':
        choice = input("what is your choice? :")
        choices(choice,player)
        
    print("Good  Bye!")
    quit()
    
    



if __name__ == "__main__":
    main()