import os
# Have a 'SHOW' command
# Have a 'HELP' command
# clare code up in general


shopping_list = []
def clear():
		os.system('cls' if os.name =='nt' else 'clear')
		
def show_help():
		
		print("""
Enter 'DONE' to stop adding item
Enter 'Q' to leave the app
Enter 'HELP' for this help
Enter 'SHOW' to see your current list
Enter 'REMOVE' to remove item from lise
		""")
		
def show_list():
		clear()
		print("Here's your list:")
		
		for index, items in enumerate(shopping_list):
				print("{}.{}".format(index+1,items))
		
		print("-"*10)
def remove_from_list():
		show_list()
		remove_item = input("What would you like to remove?\n> ")
		try:
				shopping_list.remove(remove_item)
		except ValueError:
				pass
		show_list()
		
def add_to_list(new_item):
		show_list()
		if len(shopping_list):
				position = input("where should I add {}?".format(new_item))
		
		else:
				position = 0
		try :
				position = abs(int(position))
		except ValueError:
				position = None
				
		if position is not None:
				shopping_list.insert(position-1,new_item)
		else:
				shopping_list.append(new_item)
		show_list()
	
show_help()
while True:
		print("what should we pick out at the store?")
		new_item = input("> ")
		if new_item =='':
				print("You can not ENTER the blank")
		elif new_item.upper()=="DONE" or new_item.upper()=="Q":
				break
		elif new_item.upper()=="HELP":
				show_help()
				continue
		elif new_item.upper()=="SHOW":
				show_list()
				continue
		elif new_item.upper()=="REMOVE":
				remove_from_list()
				continue
		else:
				add_to_list(new_item)
	
