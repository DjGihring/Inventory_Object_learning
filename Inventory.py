# BackBack test code
# Author: DJ Gihring


#Item Class
class Item: 
	def __init__(self, name, symbol, disc, type, value, num): #initializes the Item
		self.name = name
		self.symbol = symbol
		self.disc = disc
		self.type = type
		self.value = value
		self.num = num
		
class Inventory:
	def __init__(self, name, size): #intializes the Inventory
		self.name = name
		self.size = size
		self.space = 0
		self.nullItem = Item("null", str(0), "nothing here", "null", -1, -1)
		self.inven = [[self.nullItem for i in range(self.size)] for j in range(self.size)]  # nxn array
		
	def check(self): #Displays the inventory
		for j in range(self.size):
			print('[', end = '')
			for i in range(self.size):
					x = self.inven[i][j]
					print(x.symbol,end = ''),
					if(i+1 != self.size):
						print(", ", end = '')
			print(']')
		
	def insert(self, Item): #Inserts Item closest to the front
		for j in range(self.size):
			for i in range(self.size):
				if(self.inven[i][j] == self.nullItem):
					self.inven[i][j] = Item
					print(Item.name + " was Inserted at " + str(i+1) + 'x' + str(j+1))
					return()
	
	def swap(self, x1, y1, x2, y2): #swaps two Items positions
		item1 = self.inven[x1][y1]
		item2 = self.inven[x2][y2]
		self.inven[x1][y1] = item2
		self.inven[x2][y2] = item1
	
	# def arrange(self, type): # Sort inven with lowest values first
		# if(type == 1): #Alphabetical
			
		# if(type == 2): #Value


print("hello")
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