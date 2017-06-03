# Have a 'SHOW' command
# Have a 'HELP' command
# clare code up in general

shopping_list = []
def show_help():
	print("what should we pick out at the store?")
	print("""
	Enter 'DONE' to stop adding item
	Enter 'HELP' for this help
	Enter 'SHOW' to see your current list
	""")
def show_list():
	print("Here's your list:")
	for items in shopping_list:
		print(items)
def add_to_list(new_item):
	shopping_list.append(new_item)

	
show_help()
while True:
	new_item = input("> ")
	if new_item=="DONE":
		break
	elif new_item=="HELP":
		show_help()
		continue
	elif new_item=="SHOW":
		show_list()
		continue
	add_to_list(new_item)
	
show_list()