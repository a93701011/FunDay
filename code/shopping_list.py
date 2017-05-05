shopping_list = []
print("what should we pick out at the store?")
print("Enter 'Done' to stop adding item")

while True:
	new_item = input("> ")
	if new_item=="Done":
		break
	shopping_list.append(new_item)
print("Here's your list:")
for items in shopping_list:
	print(items)
